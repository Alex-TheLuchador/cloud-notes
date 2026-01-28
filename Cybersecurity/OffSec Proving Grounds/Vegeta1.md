# Vegeta1

## About
In this lab, you will uncover SSH credentials encoded in Morse code hidden inside an audio file. Privilege escalation is achieved by exploiting writable file permissions on /etc/passwd, allowing the creation of a root-equivalent user.

Utilize enumeration and web enumeration techniques to identify vulnerabilities. Engage in understanding Morse code and implement privilege escalation strategies to enhance your access. This lab is designed to capitalize on your skills in vulnerability exploitation.

After completion of this lab, learners will be able to:
- Perform service enumeration to identify open ports and accessible directories.
- Analyze the discovered audio file to extract hidden SSH credentials.
- Gain SSH access using the recovered credentials.
- Identify writable permissions on the /etc/passwd file.
- Escalate privileges by adding a root-equivalent user.

## Guide

### I - Reconnaissance

`nmap -sC -sV -p- -T4 [ip address] -oN scan001.txt`
- nmap is used to scan open ports
    - Given that we're looking for SSH credentials, we can expect the SSH port 22 to be open.
    - It's also common to see port 80 (HTTP) be open for web servers.
- `-sC` indicates we should use nmap's default scripts to gather additional information about services, like checking for common vulnerabilities .
- `-sV` is version detection. This probes open ports to determine what service is running and what version (e.g., "Apache 2.4.41" instead of just "HTTP").
- `-p-` scans ALL 65,535 TCP ports. Without this, nmap only scans the top 1,000 most common ports by default.
- `-T4` is the timing template used. T0 is the slowest and most conservative template. It transmits probes one by one, with an extensive delay between them. This template is incredibly effective for avoiding detection, however the scan may take a long time. T5 is the fastest, most aggressive. Using this template is strongly discouraged since it is extremely likely to cause major problems for the target host. It is also possible that the target's firewall will blacklist your IP address. Furthermore, this scan will almost certainly generate many alerts on the target. However, it delivers probes as rapidly as feasible, with no inter-probe latency. This template is handy for scanning many hosts or ports fast.
- `-oN scan001.txt` tells nmap to output the results of the command to a file called scan001.txt. It's a good idea to always keep track of your command useage and outputs.