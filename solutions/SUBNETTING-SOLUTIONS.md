# Selected Subnetting Solutions

Address count is `2^(32-prefix)`: /24 = 256, /26 = 64, /27 = 32, /28 = 16, /30 = 4.

For `192.168.5.77/26`, block size is 64 in the last octet. Network: `192.168.5.64/26`, range `.64` through `.127`. `192.168.5.100` is in that range.

Traditional multi-access IPv4 usable host counts exclude network and broadcast addresses. Special prefixes such as /31 have different rules.
