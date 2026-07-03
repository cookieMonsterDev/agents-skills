// Builder pattern in Rust.
//
// The idiomatic way to construct complex structs (compare
// std::process::Command). The consuming builder (self by value) lets
// build() move accumulated state into the product without cloning.

use std::collections::BTreeMap;

/// Immutable product.
#[derive(Debug)]
pub struct HttpRequest {
    pub method: String,
    pub url: String,
    pub headers: BTreeMap<String, String>,
    pub body: Option<String>,
    pub timeout_seconds: f64,
}

pub struct HttpRequestBuilder {
    method: String,
    url: String,
    headers: BTreeMap<String, String>,
    body: Option<String>,
    timeout_seconds: f64,
}

impl HttpRequestBuilder {
    pub fn new(method: &str, url: &str) -> Self {
        Self {
            method: method.to_uppercase(),
            url: url.to_string(),
            headers: BTreeMap::new(),
            body: None,
            timeout_seconds: 30.0,
        }
    }

    pub fn header(mut self, name: &str, value: &str) -> Self {
        self.headers.insert(name.to_string(), value.to_string());
        self
    }

    pub fn body(mut self, body: &str) -> Self {
        self.body = Some(body.to_string());
        self
    }

    pub fn timeout(mut self, seconds: f64) -> Self {
        self.timeout_seconds = seconds;
        self
    }

    pub fn build(self) -> Result<HttpRequest, String> {
        if self.body.is_some() && matches!(self.method.as_str(), "GET" | "HEAD") {
            return Err(format!("{} requests cannot have a body", self.method));
        }
        Ok(HttpRequest {
            method: self.method,
            url: self.url,
            headers: self.headers,
            body: self.body,
            timeout_seconds: self.timeout_seconds,
        })
    }
}

fn main() {
    let request = HttpRequestBuilder::new("POST", "https://api.example.com/users")
        .header("Content-Type", "application/json")
        .header("Authorization", "Bearer token123")
        .body(r#"{"name": "Ada"}"#)
        .timeout(5.0)
        .build()
        .expect("valid request");

    println!("{request:#?}");
}
