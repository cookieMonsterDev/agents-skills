// Builder pattern in JavaScript.
//
// Note: an options object with destructuring is usually more idiomatic for
// simple cases. Use a builder for multi-stage construction with validation.

class HttpRequest {
  constructor({ method, url, headers, body, timeoutSeconds }) {
    this.method = method;
    this.url = url;
    this.headers = headers;
    this.body = body;
    this.timeoutSeconds = timeoutSeconds;
    Object.freeze(this.headers);
    Object.freeze(this); // immutable product
  }
}

class HttpRequestBuilder {
  #method;
  #url;
  #headers = {};
  #body = null;
  #timeoutSeconds = 30;

  constructor(method, url) {
    this.#method = method.toUpperCase();
    this.#url = url;
  }

  header(name, value) {
    this.#headers[name] = value;
    return this;
  }

  body(body) {
    this.#body = body;
    return this;
  }

  timeout(seconds) {
    this.#timeoutSeconds = seconds;
    return this;
  }

  build() {
    if (this.#body !== null && ["GET", "HEAD"].includes(this.#method)) {
      throw new Error(`${this.#method} requests cannot have a body`);
    }
    return new HttpRequest({
      method: this.#method,
      url: this.#url,
      headers: { ...this.#headers },
      body: this.#body,
      timeoutSeconds: this.#timeoutSeconds,
    });
  }
}

const request = new HttpRequestBuilder("POST", "https://api.example.com/users")
  .header("Content-Type", "application/json")
  .header("Authorization", "Bearer token123")
  .body(JSON.stringify({ name: "Ada" }))
  .timeout(5)
  .build();

console.log(request);
