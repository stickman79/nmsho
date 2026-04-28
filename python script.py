#!/usr/bin/env python3
import subprocess
import requests
import sys
import ipaddress
import os
import time
from colorama import init, Fore, Style

# Initialize colorama for colored output
init(autoreset=True)

# Define API key and banner function
SHODAN_API_KEY = "YOUR_SHODAN_API_KEY_HERE"

def banner():
    print(Fore.GREEN + "="*60)
    print(Fore.GREEN + "RECON AUTOMATIZADO - SHODAN + NMAP")
    print(Fore.GREEN + "="*60)

def shodan_lookup(ip):
    try:
        print(Fore.YELLOW + f"\n[+] Consultando SHODAN para o IP: {ip}")
        url = f"https://api.shodan.io/shodan/host/{ip}?key={SHODAN_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful
        data = response.json()
        
        # Print results with colors
        print(Fore.CYAN + f"Organização: {data.get('org', 'N/A')}")
        print(Fore.CYAN + f"Pais: {data.get('country_name', 'N/A')}")
        print(Fore.CYAN + f"Sistema Operacional: {data.get('os', 'N/A')}")
        
        print(Fore.GREEN + "\nPortas abertas no SHODAN:")
        for item in data.get("data", []):
            print(Fore.GREEN + f"- {item.get('port')} - {item.get('transport')}")
            
    except Exception as e:
        print(Fore.RED + f"Erro ao consultar SHODAN: {e}")

def main():
    banner()
    
    # Add command line argument support
    if len(sys.argv) > 1:
        target = sys.argv[1]
        print(Fore.YELLOW + f"[*] Iniciando reconhecimento para: {target}")
        
        # Validate IP address
        try:
            ipaddress.ip_address(target)
            shodan_lookup(target)
        except ValueError:
            print(Fore.RED + "[!] Erro: IP inválido")
            sys.exit(1)
    else:
        # Interactive mode
        while True:
            print("\n" + Fore.BLUE + "Escolha uma opção:")
            print(Fore.BLUE + "1. Consultar IP")
            print(Fore.BLUE + "2. Sair")
            
            choice = input(Fore.YELLOW + "> ")
            
            if choice == "1":
                target = input(Fore.YELLOW + "Digite o IP alvo: ")
                shodan_lookup(target)
            elif choice == "2":
                print(Fore.GREEN + "Saindo...")
                break
            else:
                print(Fore.RED + "[!] Opção inválida")

if __name__ == "__main__":
    main()
