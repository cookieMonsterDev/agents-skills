// Builder pattern in Go.
//
// Go code often prefers functional options over a builder struct; both
// are shown here. Pick one per API, not both.

package main

import (
	"errors"
	"fmt"
)

// HttpRequest is the product.
type HttpRequest struct {
	Method         string
	URL            string
	Headers        map[string]string
	Body           string
	TimeoutSeconds float64
}

// --- Variant 1: builder struct with chaining ---

type HttpRequestBuilder struct {
	request HttpRequest
	hasBody bool
}

func NewHttpRequestBuilder(method, url string) *HttpRequestBuilder {
	return &HttpRequestBuilder{
		request: HttpRequest{
			Method:         method,
			URL:            url,
			Headers:        map[string]string{},
			TimeoutSeconds: 30,
		},
	}
}

func (b *HttpRequestBuilder) Header(name, value string) *HttpRequestBuilder {
	b.request.Headers[name] = value
	return b
}

func (b *HttpRequestBuilder) Body(body string) *HttpRequestBuilder {
	b.request.Body = body
	b.hasBody = true
	return b
}

func (b *HttpRequestBuilder) Timeout(seconds float64) *HttpRequestBuilder {
	b.request.TimeoutSeconds = seconds
	return b
}

func (b *HttpRequestBuilder) Build() (HttpRequest, error) {
	if b.hasBody && (b.request.Method == "GET" || b.request.Method == "HEAD") {
		return HttpRequest{}, errors.New(b.request.Method + " requests cannot have a body")
	}
	return b.request, nil
}

// --- Variant 2: functional options (often preferred in Go) ---

type Option func(*HttpRequest)

func WithHeader(name, value string) Option {
	return func(r *HttpRequest) { r.Headers[name] = value }
}

func WithBody(body string) Option {
	return func(r *HttpRequest) { r.Body = body }
}

func WithTimeout(seconds float64) Option {
	return func(r *HttpRequest) { r.TimeoutSeconds = seconds }
}

func NewHttpRequest(method, url string, opts ...Option) HttpRequest {
	r := HttpRequest{Method: method, URL: url, Headers: map[string]string{}, TimeoutSeconds: 30}
	for _, opt := range opts {
		opt(&r)
	}
	return r
}

func main() {
	request, err := NewHttpRequestBuilder("POST", "https://api.example.com/users").
		Header("Content-Type", "application/json").
		Body(`{"name": "Ada"}`).
		Timeout(5).
		Build()
	if err != nil {
		panic(err)
	}
	fmt.Printf("builder:            %+v\n", request)

	request2 := NewHttpRequest("POST", "https://api.example.com/users",
		WithHeader("Content-Type", "application/json"),
		WithBody(`{"name": "Ada"}`),
		WithTimeout(5),
	)
	fmt.Printf("functional options: %+v\n", request2)
}
