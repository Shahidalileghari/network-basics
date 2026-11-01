# Lab 04 — Diagnose an API with curl

For a local API you own, try `curl -i http://localhost:3000/health` and `curl -v --connect-timeout 3 http://localhost:3000/health`.

Compare DNS failure, connection refused, timeout, TLS verification failure, and HTTP 4xx/5xx. They occur at different stages; identify the stage before changing configuration.
