
# AI-VulnMapper
AI-VulnMapper leverages the potential of nmap's comprehensive network scanning abilities and the advanced natural language processing competencies of GPT-4 to produce insightful vulnerability reports. It's designed to aid in the recognition and understanding of security vulnerabilities.

## Features
- **Automated Network Scanning:** Utilizes Nmap for automated discovery and scanning of systems.
- **Exploit Suggestions:** Provides potential exploit suggestions according to the discovered services and versions.
- **Report Generation:** Makes comprehensive reports based on discovered suggestions and exploits.
- **Metasploit Integration:** Integrates with Metasploit for exploit searching and verification.
- **Multi-Process Scanning:** Takes advantage of multi-process capabilities for efficient network scanning.

## Getting Started

### Prerequisites
- Python 3.x
- Metasploit Framework
- Nmap
- Required Python libraries: `httpx`, `pymetasploit3`

OR

- Docker

### Usage
#### For hackers:
- Execute the image (command tailored to use against HackTheBox/TryHackMe machines)
```
docker run -it \
    -e  OPENAI_API_KEY="sk-.." \
     -v $(pwd):/app \
    --sysctl net.ipv6.conf.all.disable_ipv6=0 \
    --cap-add NET_ADMIN \
    --cap-add SYS_MODULE \
    --device /dev/net/tun:/dev/net/tun \
    --entrypoint=/bin/bash -p 1337:1337 quantumcrack/ai-vulnmapper:latest
```
- Execute `tmux`, followed by `openvpn lab_your_username.ovpn`, and finally `Ctrl+b` and `d`, after which you should return to the main terminal
- Execute ```python main.py TRYHACKME_MACHINE_IP --top_ports 500```. Happy hacking!

#### For developers:
- Clone the project and navigate to its directory ```git clone https://github.com/HuginTheCrow/AI-VulnMapper.git && cd ./AI-VulnMapper```