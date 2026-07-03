// Builder pattern in Java.
//
// The classic home of the pattern: a static nested Builder producing an
// immutable product (compare java.net.http.HttpRequest.newBuilder()).

import java.util.LinkedHashMap;
import java.util.Map;

public class builder {

    /** Immutable product. */
    static final class HttpRequest {
        private final String method;
        private final String url;
        private final Map<String, String> headers;
        private final String body; // nullable
        private final double timeoutSeconds;

        private HttpRequest(Builder b) {
            this.method = b.method;
            this.url = b.url;
            this.headers = Map.copyOf(b.headers);
            this.body = b.body;
            this.timeoutSeconds = b.timeoutSeconds;
        }

        static Builder newBuilder(String method, String url) {
            return new Builder(method, url);
        }

        static final class Builder {
            private final String method;
            private final String url;
            private final Map<String, String> headers = new LinkedHashMap<>();
            private String body;
            private double timeoutSeconds = 30.0;

            private Builder(String method, String url) {
                this.method = method.toUpperCase();
                this.url = url;
            }

            Builder header(String name, String value) {
                headers.put(name, value);
                return this;
            }

            Builder body(String body) {
                this.body = body;
                return this;
            }

            Builder timeout(double seconds) {
                this.timeoutSeconds = seconds;
                return this;
            }

            HttpRequest build() {
                if (body != null && (method.equals("GET") || method.equals("HEAD"))) {
                    throw new IllegalStateException(method + " requests cannot have a body");
                }
                return new HttpRequest(this);
            }
        }

        @Override
        public String toString() {
            return method + " " + url + " (timeout " + timeoutSeconds + "s) headers=" + headers
                    + (body != null ? " body=" + body : "");
        }
    }

    public static void main(String[] args) {
        HttpRequest request = HttpRequest.newBuilder("POST", "https://api.example.com/users")
                .header("Content-Type", "application/json")
                .header("Authorization", "Bearer token123")
                .body("{\"name\": \"Ada\"}")
                .timeout(5.0)
                .build();

        System.out.println(request);
    }
}
