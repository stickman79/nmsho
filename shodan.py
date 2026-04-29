import subprocess
import requests
import sys
import ip
import Sistema, Operacional
import Portas

print ("KILLER OSINT - shodan+nmap")
print ("by: xzzyz and slash3r")

SHODAN_API_KEY

def banner():
 print("="*50)
print ("recon automatizado - SHODAN + NMAP")
print ("="*50)

def shodan_lookup(ip):
      print(f"\n[+] Consultando SHODAN para o ip: {ip}")
      #   url =f"https://api.shodan.io/shodan/host/{ip}?key=SHODAN}
      response = requests.get(url)
    data = response.json()

     print(f" Organização: {data.get('org', 'N/A')}")
     print(f" - Pais: {data.get('country_name', 'N/A')}"}
     print(f" - Sistema Operacional: {data.get('os', 'N/A')}")
      print(f" - Portas abertas no SHODAN:")
      for item in data.get("data",[]
