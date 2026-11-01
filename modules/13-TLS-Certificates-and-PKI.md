# TLS, Certificates, and PKI

TLS protects data in transit. An HTTPS connection negotiates cryptographic parameters, authenticates the server using its certificate chain, establishes shared key material, and protects application records with symmetric cryptography.

A certificate binds a public key to an identity under a certificate authority trust model. Clients validate chain, validity period, hostname, and constraints.

Common failures: expired certificate, hostname mismatch, missing intermediate, untrusted CA, or incorrect system clock. Do not disable certificate validation in production to bypass errors.

Checkpoint: what does TLS protect, and what can it not protect (for example, a compromised endpoint)?
