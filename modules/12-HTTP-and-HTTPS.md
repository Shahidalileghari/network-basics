# HTTP and HTTPS

HTTP uses requests and responses. A request includes method, target, headers, and optional body; a response includes status, headers, and optional body.

Methods include GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS. Status classes: 2xx success, 3xx redirection, 4xx client-side issue, 5xx server-side issue.

HTTP is stateless at protocol level; cookies, tokens, and application storage can maintain session state. HTTPS is HTTP protected by TLS, providing encryption in transit, integrity, and server authentication when certificate validation succeeds.

Try `curl -i https://example.com` and `curl -v http://localhost:3000/health`.

Checkpoint: why doesn't HTTPS automatically fix an insecure backend authorization design?
