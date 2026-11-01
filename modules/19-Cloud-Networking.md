# Cloud Networking

Cloud networking applies familiar concepts to virtual infrastructure: VPC/VNet, public/private subnets, route tables, internet/NAT gateways, security groups, network ACLs, load balancers, private endpoints, DNS zones, and CDNs.

Typical architecture: a public load balancer receives HTTPS traffic and forwards to private application instances, which access a private database subnet. Avoid public database exposure unless there is a specific secured requirement.

Provider terminology differs; learn concepts, not just console screenshots.
