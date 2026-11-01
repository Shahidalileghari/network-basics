# ICMP and Diagnostics

ICMP supports IP-layer error reporting and diagnostics. `ping` commonly uses ICMP Echo Request/Reply. Some networks filter ICMP, so ping failure does not prove an application is unreachable.

- `ping host`: basic reachability and round-trip timing.
- `traceroute host` / `tracert host`: observes hop behavior using TTL/hop-limit.
- `ipconfig` / `ip addr`: interface configuration.
- `ip route` / `route print`: routing table.
- `ss -tulpn` / `netstat -ano`: socket inspection.

Record exact errors and compare name-based versus IP-based tests.
