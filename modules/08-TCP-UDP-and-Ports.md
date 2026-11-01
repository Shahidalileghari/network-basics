# TCP, UDP, and Ports

**TCP** is connection-oriented and provides a reliable, ordered byte stream using sequence numbers, acknowledgements, retransmission, flow control, and congestion control. The simplified three-way handshake is SYN, SYN-ACK, ACK. TCP does not preserve application message boundaries.

**UDP** is connectionless and message-oriented with low overhead. It does not guarantee delivery, ordering, or retransmission; applications can implement their own reliability.

Ports are 16-bit transport identifiers. Conventional examples: HTTP 80, HTTPS 443, SSH 22, DNS 53. A service is not guaranteed to listen on its conventional port.

Checkpoint: why might voice/video use UDP while a typical web API uses TCP?
