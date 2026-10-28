// Builder pattern in C++.
//
// The builder accumulates state and returns *this by reference for chaining;
// build() validates and returns an immutable product.

#include <iostream>
#include <map>
#include <optional>
#include <stdexcept>
#include <string>
#include <utility>

class HttpRequest {  // product: immutable after construction
public:
    HttpRequest(std::string method, std::string url,
                std::map<std::string, std::string> headers,
                std::optional<std::string> body, double timeoutSeconds)
        : method_(std::move(method)), url_(std::move(url)),
          headers_(std::move(headers)), body_(std::move(body)),
          timeoutSeconds_(timeoutSeconds) {}

    const std::string& method() const { return method_; }
    const std::string& url() const { return url_; }
    const std::map<std::string, std::string>& headers() const { return headers_; }
    const std::optional<std::string>& body() const { return body_; }
    double timeoutSeconds() const { return timeoutSeconds_; }

private:
    std::string method_;
    std::string url_;
    std::map<std::string, std::string> headers_;
    std::optional<std::string> body_;
    double timeoutSeconds_;
};

class HttpRequestBuilder {
public:
    HttpRequestBuilder(std::string method, std::string url)
        : method_(std::move(method)), url_(std::move(url)) {}

    HttpRequestBuilder& header(const std::string& name, const std::string& value) {
        headers_[name] = value;
        return *this;
    }

    HttpRequestBuilder& body(std::string body) {
        body_ = std::move(body);
        return *this;
    }

    HttpRequestBuilder& timeout(double seconds) {
        timeoutSeconds_ = seconds;
        return *this;
    }

    HttpRequest build() const {
        if (body_ && (method_ == "GET" || method_ == "HEAD")) {
            throw std::invalid_argument(method_ + " requests cannot have a body");
        }
        return HttpRequest(method_, url_, headers_, body_, timeoutSeconds_);
    }

private:
    std::string method_;
    std::string url_;
    std::map<std::string, std::string> headers_;
    std::optional<std::string> body_;
    double timeoutSeconds_ = 30.0;
};

int main() {
    HttpRequest request = HttpRequestBuilder("POST", "https://api.example.com/users")
                              .header("Content-Type", "application/json")
                              .header("Authorization", "Bearer token123")
                              .body(R"({"name": "Ada"})")
                              .timeout(5.0)
                              .build();

    std::cout << request.method() << ' ' << request.url()
              << " (timeout " << request.timeoutSeconds() << "s)\n";
    for (const auto& [name, value] : request.headers()) {
        std::cout << name << ": " << value << '\n';
    }
    if (request.body()) {
        std::cout << *request.body() << '\n';
    }
    return 0;
}
