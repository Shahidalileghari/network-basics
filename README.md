# Networking Mastery

A practical networking course for software engineers, from fundamentals to advanced concepts. Learn how applications communicate, how packets travel, how protocols work, and how to diagnose and secure real systems.

## Outcomes
- Explain the journey of a request from a Flutter/web client to a backend.
- Understand OSI and TCP/IP, encapsulation, Ethernet, IP, TCP, UDP, DNS, HTTP, and TLS.
- Work with IPv4/IPv6, CIDR, subnetting, ports, routing, NAT, and gateways.
- Diagnose common DNS, connectivity, routing, TLS, and HTTP failures.
- Use `ping`, `traceroute`/`tracert`, `ip`/`ipconfig`, `ss`/`netstat`, `dig`/`nslookup`, `curl`, and Wireshark.
- Understand network security, VPNs, cloud networking, CDNs, HTTP/2, HTTP/3, and QUIC.

## Roadmap

| Stage | Modules | Focus |
|---|---|---|
| Foundations | 01–04 | Network basics, models, devices, Ethernet/Wi-Fi |
| Addressing | 05–07 | IPv4/IPv6, subnetting, DHCP, ARP |
| Transport | 08–10 | TCP, UDP, ports, routing, NAT, ICMP |
| Application | 11–14 | DNS, HTTP, TLS, SSH and common protocols |
| Operations | 15–16 | Network tools and packet analysis |
| Security/modern | 17–20 | Security, VPNs, cloud, modern protocols |
| Engineering | 21–23 | App networking, architecture, interview review |

## Repository map
- `modules/`: lessons in learning order.
- `labs/`: safe command-line and programming labs.
- `exercises/` and `solutions/`: practice and selected worked answers.
- `projects/`: portfolio-sized projects.
- `cheatsheets/`: commands and protocol references.
- `docs/`: roadmap, glossary, troubleshooting.

## How to study
Read each module, answer its checkpoint in your own words, run relevant labs, then complete exercises before consulting solutions. Spend extra time on subnetting, TCP/IP, DNS, HTTP/TLS, and troubleshooting.

## Prerequisites
Basic computer use and terminal familiarity. Programming experience helps but is not required for the theory modules. Python 3.11+ is used in one socket lab.

## Safety
Only inspect networks, hosts, and traffic you own or are explicitly authorized to test. Prefer localhost and private lab networks. Never publish credentials, private packet captures, or sensitive network details.

## Validation
The ZIP archive and required-file structure are checked when packaged. Runtime tests and live network tests have not been run. Commands may differ across operating systems.

## License
MIT. See `LICENSE`.
