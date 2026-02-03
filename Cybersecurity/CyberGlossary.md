# Glossary for Cybersecurity

## Connect Scan
In Nmap, the Connect scan has the underlying OS issue a "connect" system call, which tries to complete the full TCP handshake (SYN - SYN/ACK - ACK) with the target port, making it a slow and easily detectable method.

## Enumeration
In cybersecurity, the different types of enumeration allow the attacker to gain insight into the topology and security of a target environment.

The types of enumeration are:
- Network Enumeration
  - Scans a target network using discovery protocols like ICMP, SNMP to gather information about active IP addresses, devices, and users.
- Service Enumeration
  - The attacker scans for active services, applications, and open ports on the target systems, as well as relevant configurations and versions.
- User Enumeration
  - The attacker identifies usernames and accounts on the target systems, ascertaining where valid users exist on applications.
- Web Enumeration
  - The process of gathering detailed information about a target web server, including the operating system, applications, and potential vulnerabilities.

Preventing enumeration may include:
- Deploying strong access controls and comprehensive password policies.
- Employing firewalls in conjunction with network segmentation.
- Implementing network monitoring technologies like intrusion detection systems (IDS) and intrusion systems (IPS).
- Addressing identified vulnerabilities with regular updates and patches.

## Error: 403
The web server understood your request but refused to grant access, indicating insufficient permission.

## Port 80
Default TCP port for unencrypted HTTP data.

## SYN-ACK
The crucial steps in the TCP three-way handshake, where SYN (Synchronize) initiates a connection request and ACK (Acknowledge) confirms receipt, which forms the pattern `SYN -> SYN-ACK -> ACK`.

The initiator, generally the browser, sends a TCP SYNchronize packet to the other host, generally the server.
The server receives the SYN and sends back a SYNchronize-ACKnowledgement.
The initiator receives the server's SYN-ACK and sends an ACKnowledge. The server receives ACK and the TCP socket connection is established.

## SYN Scan
In Nmap, a TCP SYNC scan is the default and most popular type of scan because it is quick and unlikely to be stopped by firewalls.
- The scanner sends a SYN packet.
- If the scanner receives a SYN/ACK packet, the port is open.
- Instead of completeing the handshake by sending an ACK packet, the scanner immediately sends an reset (RST) packet, which terminates the connection.

This works because a connection is never truly established because the final handshake ACK packet is never sent.
