# tool.py
import subprocess
import requests
import sys
import ipaddress
import OSINT
import Sistema
import Portas

print("OSINT ASSASSINO - shodan+nmap")
print("por: xzzyz e slash3r")

SHODAN_API_KEY = "sua_api_key_aqui"

def banner():
    print("="*50)
    print("recon automatizado - SHODAN + NMAP")
    print("="*50)

def shodan_lookup(ip):
    print(f"\n[+] Consultando SHODAN para o ip: {ip}")
    url = f"https://api.shodan.io/shodan/host/{ip}?key={SHODAN_API_KEY}"
    response = requests.get(url)
    data = response.json()

    print(f" Organização: {data.get('org', 'N/A')}")
    print(f" - Pais: {data.get('country_name', 'N/A')}")
    print(f" - Sistema Operacional: {data.get('os', 'N/A')}")
    print(f" - Portas abertas no SHODAN:")
    for item in data.get("data", []):
        print(f"   - {item['port']}")

def main():
    banner()
    ip = input("\nDigite o IP: ")
    try:
        ipaddress.ip_address(ip)
        shodan_lookup(ip)
    except ValueError:
        print("IP inválido")
        sys.exit(1)

if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()            
