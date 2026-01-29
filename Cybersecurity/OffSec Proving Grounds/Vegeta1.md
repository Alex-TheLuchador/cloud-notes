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

`nmap -sC -sV -p- -T3 [ip address] -oN scan001.txt`
- nmap is used to scan open ports
    - Given that we're looking for SSH credentials, we can expect the SSH port 22 to be open.
    - It's also common to see port 80 (HTTP) be open for web servers.
- `-sC` indicates we should use nmap's default scripts to gather additional information about services, like checking for common vulnerabilities .
- `-sV` is version detection. This probes open ports to determine what service is running and what version (e.g., "Apache 2.4.41" instead of just "HTTP").
- `-p-` scans ALL 65,535 TCP ports. Without this, nmap only scans the top 1,000 most common ports by default.
- `-T3` is the timing template used. T0 is the slowest and most conservative template. It transmits probes one by one, with an extensive delay between them. This template is incredibly effective for avoiding detection, however the scan may take a long time. T5 is the fastest, most aggressive. Using this template is strongly discouraged since it is extremely likely to cause major problems for the target host. It is also possible that the target's firewall will blacklist your IP address. Furthermore, this scan will almost certainly generate many alerts on the target. However, it delivers probes as rapidly as feasible, with no inter-probe latency. This template is handy for scanning many hosts or ports fast.
- `-oN scan001.txt` tells nmap to output the results of the command to a file called scan001.txt. It's a good idea to always keep track of your command useage and outputs.

```
Starting Nmap 7.98 ( https://nmap.org ) at 2026-01-28 16:09 +0000
Nmap scan report for 192.168.59.73
Host is up (0.00037s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 1f:31:30:67:3f:08:30:2e:6d:ae:e3:20:9e:bd:6b:ba (RSA)
|   256 7d:88:55:a8:6f:56:c8:05:a4:73:82:dc:d8:db:47:59 (ECDSA)
|_  256 cc:de:de:4e:84:a8:91:f5:1a:d6:d2:a6:2e:9e:1c:e0 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Site doesn't have a title (text/html).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.30 seconds
```

SSH is secure by default, so the unsecured web service (HTTP, port 80) is a good place to start looking for the credentials.

---

`gobuster dir -u http://192.168.59.73 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,wav,mp3`
- gobuster lets us see the directories on a web server, since servers don't just list directories for us.
    - gobuster is essentially brute force guessing, but with guesses that are predefined in a wordlist.
- `-w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt` indicates we want to use the wordlist `directory-list-2.3-medium.txt`.
    - The wordlist will contain the directory and file names developers most often use.
    - Gobuster will search the web server for directories/files matching the ones in the wordlist.
- `-x php,html,txt,wav,mp3` tells gobuster to search for the specific file extensions listed.

```
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.59.73
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Extensions:              php,html,txt,wav,mp3
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
index.html           (Status: 200) [Size: 119]
img                  (Status: 301) [Size: 312] [--> http://192.168.59.73/img/]
login.php            (Status: 200) [Size: 0]
image                (Status: 301) [Size: 314] [--> http://192.168.59.73/image/]
admin                (Status: 301) [Size: 314] [--> http://192.168.59.73/admin/]
manual               (Status: 301) [Size: 315] [--> http://192.168.59.73/manual/]
robots.txt           (Status: 200) [Size: 11]
server-status        (Status: 403) [Size: 278]
Progress: 1323348 / 1323348 (100.00%)
===============================================================
Finished
===============================================================
```

We can see a few paths and files listed in the output. `301` status codes indicate a redirect to a new location (like `http://192.168.59.73/img/`).

Robots.txt is a common file used to tell Google/search engines to not index certain files. This makes it a good place to look for any hidden directories.

---

`curl http://192.168.59.73/robots.txt`
- This allows us to see the contents of robots.txt.

```
*
/find_me
```

Now we can see a directory called `find_me`! We can use `curl` again to see whats in that directory.

---

`curl http://192.168.59.73/find_me/`

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
 <head>
  <title>Index of /find_me</title>
 </head>
 <body>
<h1>Index of /find_me</h1>
  <table>
   <tr><th valign="top"><img src="/icons/blank.gif" alt="[ICO]"></th><th><a href="?C=N;O=D">Name</a></th><th><a href="?C=M;O=A">Last modified</a></th><th><a href="?C=S;O=A">Size</a></th><th><a href="?C=D;O=A">Description</a></th></tr>
   <tr><th colspan="5"><hr></th></tr>
<tr><td valign="top"><img src="/icons/back.gif" alt="[PARENTDIR]"></td><td><a href="/">Parent Directory</a></td><td>&nbsp;</td><td align="right">  - </td><td>&nbsp;</td></tr>
<tr><td valign="top"><img src="/icons/text.gif" alt="[TXT]"></td><td><a href="find_me.html">find_me.html</a></td><td align="right">2020-06-28 19:16  </td><td align="right">3.8K</td><td>&nbsp;</td></tr>
   <tr><th colspan="5"><hr></th></tr>
</table>
<address>Apache/2.4.38 (Debian) Server at 192.168.59.73 Port 80</address>
</body></html>
```

If you look closely, you can see there's a file referenced within the HTML code called `find_me.html`. Once again, we can use `curl`.

---

`curl http://192.168.59.73/find_me/find_me.html`

```
<html>
<head> Vegeta-1.0 </head>
<body></body>
</html>

<!-- aVZCT1J3MEtHZ29BQUFBTlNVaEVVZ0FBQU1nQUFBRElDQVlBQUFDdFdLNmVBQUFIaGtsRVFWUjRuTzJad1k0c09RZ0U1LzkvK3UyMU5TdTdCd3JTaVN0QzhoR2M0SXBMOTg4L0FGanljem9BZ0RNSUFyQUJRUUEySUFqQUJnUUIySUFnQUJzUUJHQURnZ0JzUUJDQURRZ0NzQUZCQURhRUJmbjUrUmwvbk9aTFAxeER6K3g5VTA1cWJoWjFkcjRzSFQyejkwMDVxYmxaMU5uNXNuVDB6TjQzNWFUbVpsRm41OHZTMFRONzM1U1RtcHRGblowdlMwZlA3SDFUVG1wdUZuVjJ2aXdkUGJQM1RUbXB1Vm5VMmZteWRQVE0zamZscE9hdVhKUVRUamxkSHZ0YmxvNDZOUWp5UjV4eUlvZ09CUGtqVGprUlJBZUMvQkdubkFpaUEwSCtpRk5PQk5HQklIL0VLU2VDNkVDUVArS1VFMEYwakJWRS9aSGM4SEhkUHZ1RWQwZVF3N003MWFtelRIaDNCRGs4dTFPZE9zdUVkMGVRdzdNNzFhbXpUSGgzQkRrOHUxT2RPc3VFZDBlUXc3TTcxYW16VEhoM0JEazh1MU9kT3N1RWQwZVFJcWJNNENUcmhKMGhTQkZUWmtDUUdBaFN4SlFaRUNRR2doUXhaUVlFaVlFZ1JVeVpBVUZpSUVnUlUyWkFrQmdJVXNTVUdSQWtCb0lVMFRHZjAxN2UrdTRJVXNScEtSRGtXYzVsdjNEQlN4ZjFqZE5TSU1pem5NdCs0WUtYTHVvYnA2VkFrR2M1bC8zQ0JTOWQxRGRPUzRFZ3ozSXUrNFVMWHJxb2I1eVdBa0dlNVZ6MkN4ZThkRkhmT0MwRmdqekx1ZXdYTGhCL2VGazZjcm84Mm9rc2IzMTNCQkgwdkNITFc5OGRRUVE5YjhqeTFuZEhFRUhQRzdLODlkMFJSTkR6aGl4dmZYY0VFZlM4SWN0YjN4MUJCRDF2eVBMV2R5OFZaTXJwV1BDYjY2YWNEQWdTbUkrNjJTY0RnZ1RtbzI3MnlZQWdnZm1vbTMweUlFaGdQdXBtbnd3SUVwaVB1dGtuQTRJRTVxTnU5c25nOVNPMkFjcmxQN212SXd2OEg3YjVDd1NCVDlqbUx4QUVQbUdidjBBUStJUnQvZ0pCNEJPMitRc0VnVS9ZNWk4UUJENlIvUS9pMURPTFU4OHBkV3FxY3lKSTBlenFubFBxMUNBSWdveXFVNE1nQ0RLcVRnMkNJTWlvT2pVSWdpQ2o2dFFnQ0lLTXFsTnpYQkExYnhZeWk5TU1UbStVeWwvZXNSZ0VpZU0wZzlNYnBmS1hkeXdHUWVJNHplRDBScW44NVIyTFFaQTRUak00dlZFcWYzbkhZaEFranRNTVRtK1V5bC9lc1JnRWllTTBnOU1icGZLWGR5d0dRZUk0emVEMFJxbjhwYzJTUTcxWkFxZlpwd2pTVWJmc2w2cEtoRU1RajV3SUVzeWZxa3FFUXhDUG5BZ1N6SitxU29SREVJK2NDQkxNbjZwS2hFTVFqNXdJRXN5ZnFrcUVReENQbkFnU3pKK3FTb1JERUkrY0NCTE1uNm9xRHVleWpLNmVhcHdFNmNpWjdabkttS29xRHVleWpLNmVhaEFFUVI3VnFYdXFRUkFFZVZTbjdxa0dRUkRrVVoyNnB4b0VRWkJIZGVxZWFoQUVRUjdWcVh1cVFaQ0JncWcvNWpmZjEvRngzUzdXOHE2cHdia1BRUkNFK3hDa01HZnFycW5CdVE5QkVJVDdFS1F3WitxdXFjRzVEMEVRaFBzUXBEQm42cTdLY0ZtY0hzYnBvM1RLMlpGbEFnaHlPQXVDZUlNZ2g3TWdpRGNJY2pnTGduaURJSWV6SUlnM0NISTRDNEo0Z3lDSHN5Q0lONldDM1A0d1RvL3RKTEo2TDhvc0NGSjBueG9FUVpDMkxCMzNxVUVRQkduTDBuR2ZHZ1JCa0xZc0hmZXBRUkFFYWN2U2NaOGFCRUdRdGl3ZDk2bEJrSUdDZE5TcGUyYnZVMzk0Nm5mb3lPazAzN0pmdU1Ba2VGZlA3SDFPSDE3MlBuVk9wL21XL2NJRkpzRzdlbWJ2Yy9yd3N2ZXBjenJOdCt3WExqQUozdFV6ZTUvVGg1ZTlUNTNUYWI1bHYzQ0JTZkN1bnRuN25ENjg3SDNxbkU3ekxmdUZDMHlDZC9YTTN1ZjA0V1h2VStkMG1tL1pMMXhnRXJ5clovWStwdzh2ZTU4NnA5Tjh5MzdoQXZHSGZzUHlPN0pNMmFkNlp3aGkrbWdkODkyd1R3UzU3RUU3WmtjUUJMbm1RVHRtUnhBRXVlWkJPMlpIRUFTNTVrRTdaa2NRQkxubVFUdG1SNUFYQ1hJNzZnKzJBN1dRSFZrNnhFcmxUMVZkRElKNFpFRVFVeERFSXd1Q21JSWdIbGtReEJRRThjaUNJS1lnaUVjV0JERUZRVHl5akJXa1kyRDFjV0xLQitUeXdYNERRUkFFUVlUM0ljaGhFS1FXQkVFUUJCSGVoeUNIUVpCYUVBUkJFRVI0SDRJY0JrRnFzUmJFaVk2Y04zek1UaCtzK28xUy9VNEg2QUpCRUFSQk5pQUlnaURJQmdSQkVBVFpnQ0FJZ2lBYkVBUkJFR1FEZ2lESUtFRnUrTGc2NW5QSzRuVFV1MTdlRlM0d2VqUjF6bzc1bkxJNEhmV3VsM2VGQzR3ZVRaMnpZejZuTEU1SHZldmxYZUVDbzBkVDUreVl6eW1MMDFIdmVubFh1TURvMGRRNU8rWnp5dUowMUx0ZTNoVXVNSG8wZGM2TytaeXlPQjMxcnBkM2hRdU1IazJkczJNK3B5eE9SNzNyNVYzaEFxTkhVK2QwMnN1VUxOTnpJb2h4M1ExWnB1ZEVFT082RzdKTXo0a2d4blUzWkptZUUwR002MjdJTWowbmdoalgzWkJsZWs0RU1hNjdJY3YwbkFoU3hKUVoxRDJuZkMvTEhKWExjQm9ZUVR4NlR2bGVsamtxbCtFME1JSjQ5Snp5dlN4elZDN0RhV0FFOGVnNTVYdFo1cWhjaHRQQUNPTFJjOHIzc3N4UnVReW5nUkhFbytlVTcyV1pvM0laVGdNamlFZlBLZC9MTWtmbE1weVk4bEVxSC9zSlRoODZnaFNBSUxVZ1NQT2kxQ0JJTFFqU3ZDZzFDRklMZ2pRdlNnMkMxSUlnell0U2d5QzFJRWp6b3RRZ1NDMElVckNvS1NjN245TmVzcHplZmNVTTJmbFMvU29EVERrZEMzYWF3U2tuZ2d3OEhRdDJtc0VwSjRJTVBCMExkcHJCS1NlQ0REd2RDM2Fhd1NrbmdndzhIUXQybXNFcEo0SU1QQjBMZHByQktlZnJCQUY0RXdnQ3NBRkJBRFlnQ01BR0JBSFlnQ0FBR3hBRVlBT0NBR3hBRUlBTkNBS3dBVUVBTmlBSXdBWUVBZGp3SHlVRnd2VnIwS3ZGQUFBQUFFbEZUa1N1UW1DQw== -->
```

The above is our output from the `find_me.html` file with a lot of blank whitespace removed. We can see there's a random string of text, which is actually base64 encoded text.

**Copy and paste that string into a text file (I've called it string.txt)**

---

`base64 -d string.txt`
- This command allows us to encode or decode base64 strings, which our text file contains..
- `-d` indicates the decode functionality.

```
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
```

After decoding the base64 string from the HTML file, we get *another* base64 encoded string.

Same process, let's decode it. Instead of saving it to a file, I'll pipe it into another base64 command.

---

`base64 -d string.txt | base64 -d`
- This means we are decoding the string.txt file, then sending that output to another `base64 -d` call to decode again.

The output is a bunch of jumbled text and symbols, but **notice it says png at the top**.

We can assume this is a decoded image file, so we should try to save this output as a .png file to see what it looks like.

---

`base64 -d string.txt | base64 -d > output.png`
- Building off our last command, we simply add `> output.png` to indicate we should output the result as a .png file.

**We now see that the output.png file is a QR code.**

Scanning the QR code shows the following text:

*Password: topshellv*

After trying this password with username 'Vegeta' in SSH, the login failed. Perhaps this was just a rabbit hole intended to distract me!

---

`sudo apt install seclists -y`
- I installed seclists, which provides several wordlists for different purposes, including directory enumeration. Perhaps this will show us directories we missed.

---

`gobuster dir -u http://192.168.52.73 -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-lowercase-2.3-big.txt -x php,html,txt,wav,mp3`
- Here we make use of seclists' largest wordlist, in hopes that it will reveal something new.

```
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.52.73
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-lowercase-2.3-big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Extensions:              php,html,txt,wav,mp3
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
index.html           (Status: 200) [Size: 119]
img                  (Status: 301) [Size: 312] [--> http://192.168.52.73/img/]
login.php            (Status: 200) [Size: 0]
image                (Status: 301) [Size: 314] [--> http://192.168.52.73/image/]
admin                (Status: 301) [Size: 314] [--> http://192.168.52.73/admin/]
manual               (Status: 301) [Size: 315] [--> http://192.168.52.73/manual/]
robots.txt           (Status: 200) [Size: 11]
server-status        (Status: 403) [Size: 278]
bulma                (Status: 301) [Size: 314] [--> http://192.168.52.73/bulma/]
logitech-quickcam_w0qqcatrefzc5qqfbdz1qqfclz3qqfposz95112qqfromzr14qqfrppz50qqfsclz1qqfsooz1qqfsopz1qqfssz0qqfstypez1qqftrtz1qqftrvz1qqftsz2qqnojsprzyqqpfidz0qqsaatcz1qqsacatzq2d1qqsacqyopzgeqqsacurz0qqsadisz200qqsaslopz1qqsofocuszbsqqsorefinesearchz1.html (Status: 403) [Size: 278]
Progress: 7111512 / 7111512 (100.00%)
===============================================================
Finished
===============================================================
```

*We found a new directory: bulma*.

Let's see what this contains.

---

`curl http://192.168.52.73/bulma/`

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
 <head>
  <title>Index of /bulma</title>
 </head>
 <body>
<h1>Index of /bulma</h1>
  <table>
   <tr><th valign="top"><img src="/icons/blank.gif" alt="[ICO]"></th><th><a href="?C=N;O=D">Name</a></th><th><a href="?C=M;O=A">Last modified</a></th><th><a href="?C=S;O=A">Size</a></th><th><a href="?C=D;O=A">Description</a></th></tr>
   <tr><th colspan="5"><hr></th></tr>
<tr><td valign="top"><img src="/icons/back.gif" alt="[PARENTDIR]"></td><td><a href="/">Parent Directory</a></td><td>&nbsp;</td><td align="right">  - </td><td>&nbsp;</td></tr>
<tr><td valign="top"><img src="/icons/sound2.gif" alt="[SND]"></td><td><a href="hahahaha.wav">hahahaha.wav</a></td><td align="right">2020-06-28 18:19  </td><td align="right">231K</td><td>&nbsp;</td></tr>
   <tr><th colspan="5"><hr></th></tr>
</table>
<address>Apache/2.4.38 (Debian) Server at 192.168.52.73 Port 80</address>
</body></html>
```

Wow! We found `hahahaha.wav`! An audio file exactly what we're looking for in this lab.

According to the lab specs, the audio should be in Morse code, so we will use a website to decode it.

After downloading the file to my machine, I passed it into a website that takes audio files with Morse code and produces the text equivalent.

The result I got is:

`USER:TRUNKSPASSWORD:US3R<KN>SINDOLLARSSYMBOK`

This is tricky because it looks like what we need, but the formatting is a little weird.

`trunks` is the username, and `PASSWORD:US3R<KN>SINDOLLARSSYMBOK` is meaning the password is `u$3r`, with the 'S' as the dollar symbol ($).

Let's try it out.

---

`ssh trunks@192.168.52.73`

It took a few tries (I initially tried all upercase, then all lowercase, which was the proper way). After entering the password, we successfully connected as the user Trunks!

Now, we must find the flag.
