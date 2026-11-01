# DNS: Domain Name System

DNS is a distributed hierarchical naming system. Records include A (IPv4), AAAA (IPv6), CNAME (alias), MX, TXT, and NS.

A simplified lookup: the client asks a recursive resolver; the resolver uses cache or queries the DNS hierarchy; authoritative servers provide records; the resolver caches answers according to TTL.

DNS commonly uses UDP port 53; TCP is also used. Encrypted DNS options include DNS-over-TLS and DNS-over-HTTPS.

Commands: `nslookup example.com`, `dig example.com A`, `dig example.com AAAA`.

Checkpoint: why can a site fail by domain name but work using a known IP (assuming the service supports it)?
