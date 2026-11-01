# Troubleshooting Playbook

1. Scope the issue: one device, one service, or the whole network?
2. Check interface/link state and configuration (`ip addr`, `ipconfig`).
3. Verify address, prefix, and default gateway.
4. Test local gateway reachability where ICMP is permitted.
5. Check DNS with `nslookup` or `dig`.
6. Test the intended TCP port with an approved tool.
7. Inspect HTTP status, headers, and body with `curl`.
8. Use `traceroute`/`tracert` and packet capture if needed.
9. Change one variable at a time and record the hypothesis and result.

A failed ping does not prove a server is down: ICMP may be filtered while HTTPS works.
