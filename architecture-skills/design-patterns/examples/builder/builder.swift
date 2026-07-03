// Builder pattern in Swift.
//
// Note: memberwise initializers with default values cover simple cases,
// and result builders (@resultBuilder, as in SwiftUI) are the language-
// native form for declarative trees. Use an explicit builder for
// multi-stage construction with validation.

import Foundation

/// Immutable product.
struct HttpRequest {
    let method: String
    let url: String
    let headers: [String: String]
    let body: String?
    let timeoutSeconds: Double
}

enum BuildError: Error {
    case bodyNotAllowed(method: String)
}

final class HttpRequestBuilder {
    private let method: String
    private let url: String
    private var headers: [String: String] = [:]
    private var body: String?
    private var timeoutSeconds: Double = 30

    init(method: String, url: String) {
        self.method = method.uppercased()
        self.url = url
    }

    @discardableResult
    func header(_ name: String, _ value: String) -> HttpRequestBuilder {
        headers[name] = value
        return self
    }

    @discardableResult
    func body(_ body: String) -> HttpRequestBuilder {
        self.body = body
        return self
    }

    @discardableResult
    func timeout(_ seconds: Double) -> HttpRequestBuilder {
        timeoutSeconds = seconds
        return self
    }

    func build() throws -> HttpRequest {
        if body != nil, method == "GET" || method == "HEAD" {
            throw BuildError.bodyNotAllowed(method: method)
        }
        return HttpRequest(
            method: method,
            url: url,
            headers: headers,
            body: body,
            timeoutSeconds: timeoutSeconds
        )
    }
}

let request = try HttpRequestBuilder(method: "POST", url: "https://api.example.com/users")
    .header("Content-Type", "application/json")
    .header("Authorization", "Bearer token123")
    .body(#"{"name": "Ada"}"#)
    .timeout(5)
    .build()

print(request)
