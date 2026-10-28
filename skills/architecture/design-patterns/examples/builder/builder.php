<?php
// Builder pattern in PHP.
//
// Note: named arguments (PHP 8+) cover simple cases; use a builder for
// multi-stage construction with validation.

declare(strict_types=1);

/** Immutable product. */
final class HttpRequest
{
    /** @param array<string, string> $headers */
    public function __construct(
        public readonly string $method,
        public readonly string $url,
        public readonly array $headers,
        public readonly ?string $body,
        public readonly float $timeoutSeconds,
    ) {
    }
}

final class HttpRequestBuilder
{
    /** @var array<string, string> */
    private array $headers = [];
    private ?string $body = null;
    private float $timeoutSeconds = 30.0;

    public function __construct(
        private readonly string $method,
        private readonly string $url,
    ) {
    }

    public function header(string $name, string $value): self
    {
        $this->headers[$name] = $value;
        return $this;
    }

    public function body(string $body): self
    {
        $this->body = $body;
        return $this;
    }

    public function timeout(float $seconds): self
    {
        $this->timeoutSeconds = $seconds;
        return $this;
    }

    public function build(): HttpRequest
    {
        $method = strtoupper($this->method);
        if ($this->body !== null && in_array($method, ['GET', 'HEAD'], true)) {
            throw new InvalidArgumentException("$method requests cannot have a body");
        }
        return new HttpRequest($method, $this->url, $this->headers, $this->body, $this->timeoutSeconds);
    }
}

$request = (new HttpRequestBuilder('POST', 'https://api.example.com/users'))
    ->header('Content-Type', 'application/json')
    ->header('Authorization', 'Bearer token123')
    ->body('{"name": "Ada"}')
    ->timeout(5.0)
    ->build();

var_dump($request);
