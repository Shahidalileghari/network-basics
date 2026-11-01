# Routing, NAT, and Gateways

Routers forward IP packets using routing tables. The most specific matching prefix generally wins (longest-prefix match). A default route is used when no more specific route matches.

A host sends traffic for a remote subnet to its default gateway. It resolves the gateway's local link-layer address and sends the frame to that gateway.

NAT translates address information. PAT/NAPT commonly lets multiple private IPv4 hosts share one public address using transport ports. NAT is not itself a security policy; firewalls enforce access rules.

Inspect routes with `ip route` (Linux), `route print` (Windows), or `netstat -rn` (macOS).

Checkpoint: distinguish routing, NAT, and firewalling.
