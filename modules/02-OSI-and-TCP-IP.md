# OSI and TCP/IP Models

| OSI layer | Responsibility | Examples |
|---|---|---|
| 7 Application | Network services | HTTP, DNS, SMTP |
| 6 Presentation | Representation/encryption concepts | Encoding; TLS spans layers in common models |
| 5 Session | Dialog/session coordination | Session concepts |
| 4 Transport | Process-to-process delivery | TCP, UDP |
| 3 Network | Logical addressing/routing | IP, ICMP |
| 2 Data Link | Local frame delivery | Ethernet, Wi-Fi |
| 1 Physical | Signals and media | Copper, fiber, radio |

The practical TCP/IP model is often Link, Internet, Transport, Application. Mapping is approximate. Encapsulation wraps application data in transport, IP, and link headers; the receiver processes them in reverse.

Checkpoint: map DNS, TCP, IP, and Ethernet to their typical layers.
