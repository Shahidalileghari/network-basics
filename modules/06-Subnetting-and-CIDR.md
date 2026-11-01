# Subnetting and CIDR

CIDR appends a prefix length. `192.168.10.0/24` means 24 network bits and 8 remaining bits; total addresses are `2^(32-24) = 256`. Traditional usable host addresses are 254, excluding network and broadcast addresses in ordinary multi-access IPv4 subnets.

For `10.20.0.0/16`, total addresses are `2^16 = 65,536`.

Method: calculate host bits, compute `2^(host bits)`, determine block boundaries, and verify host capacity. `/31` is valid for IPv4 point-to-point links; `/32` represents one host route.

Practice: calculate address counts for /26, /28, /30. Does `192.168.1.70` belong to `192.168.1.64/26`?
