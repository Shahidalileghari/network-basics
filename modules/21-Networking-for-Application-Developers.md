# Networking for Application Developers

For a Flutter client calling a Node.js API:
1. Client obtains hostname from configuration.
2. DNS resolves it to an address.
3. Client establishes TCP and TLS for HTTPS.
4. HTTP carries method, path, headers, and JSON body.
5. Backend authenticates and validates the request.
6. API calls the database over its own connection.
7. Backend returns an HTTP response.

Engineering concerns: set timeouts; retry only appropriate transient failures; use exponential backoff with jitter; distinguish DNS, connection, TLS, timeout, HTTP, and application errors; never ship server secrets in clients; enforce authorization server-side; validate certificates.

Local example: `curl -i http://localhost:3000/health`.
