# ARP, DHCP, and Neighbor Discovery

**ARP** discovers the link-layer address for an IPv4 neighbor on the local network. It does not route packets across the Internet.

**DHCP** provides configuration such as IP address, prefix/mask, default gateway, and DNS resolver. A common DHCPv4 sequence is Discover, Offer, Request, Acknowledge (DORA).

**IPv6 Neighbor Discovery** uses ICMPv6 for neighbor resolution and router discovery.

Inspect caches with `ip neigh` (Linux) or `arp -a`. Inspect configuration with `ip addr`, `ip route`, or `ipconfig /all`.

Checkpoint: why does a host need the MAC address of its default gateway for a remote destination?
