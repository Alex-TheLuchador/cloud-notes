# Glossary for Cybersecurity

## SYN Scan
In Nmap, a TCP SYNC scan is the default and most popular type of scan because it is quick and unlikely to be stopped by firewalls.
- The scanner sends a SYN packet.
- If the scanner receives a SYN/ACK packet, the port is open.
- Instead of completeing the handshake by sending an ACK packet, the scanner immediately sends an reset (RST) packet, which terminates the connection.

This works because a connection is never truly established because the final handshake ACK packet is never sent.

## Connect Scan
In Nmap, the Connect scan has the underlying OS issue a "connect" system call, which tries to complete the full TCP handshake (SYN - SYN/ACK - ACK) with the target port, making it a slow and easily detectable method.