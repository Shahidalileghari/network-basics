# Network Architecture and System Design

A production system may contain DNS/CDN at the edge, WAF and load balancer, API gateway/ingress, private application services, private database/cache subnets, outbound egress controls, and centralized telemetry.

Ask: which components must be internet-reachable? Which tier-to-tier connections are allowed? Where does TLS terminate? How are certificates rotated? How are health checks and failover handled? How will latency and errors be observed?

Document trust boundaries and data flows; do not assume every service should communicate freely.
