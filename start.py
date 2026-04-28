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
        response.raise_for_status()
        data = response.json()
        
        print(Fore.CYAN + f"Organização: {data.get('org', 'N/A')}")
        print(Fore.CYAN + f"Pais: {data.get('country_name', 'N/A')}")
        print(Fore.CYAN + f"Sistema Operacional: {data.get('os', 'N/A')}")
        
        print(Fore.GREEN + "\nPortas abertas no SHODAN:")
        for item in data.get("data", []):
            print(Fore.GREEN + f"- {item.get('port')} - {item.get('transport')}")
            
    except Exception as e:
        print(Fore.RED + f"Erro ao consultar SHODAN: {e}")

def start_kali_mode():
    """Specialized mode for Kali Linux"""
    print(Fore.BLUE + "[*] Modo Kali Linux ativado")
    kali_commands = [
        "ifconfig",
        "route -n",
        "netstat -tulnp",
        "ss -tulnp"
    ]
    
    for cmd in kali_commands:
        print(Fore.YELLOW + f"\n[+] Executando: {cmd}")
        result = subprocess.run(cmd.split(), capture_output=True, text=True)
        print(result.stdout)

def main():
    banner()
    
    # Check if running on Kali Linux
    if os.path.exists("/etc/kali-version"):
        print(Fore.BLUE + "[*] Sistema detectado como Kali Linux")
        kali_mode = input(Fore.YELLOW + "Deseja ativar modo Kali Linux? (y/n): ")
        
        if kali_mode.lower() == 'y':
            start_kali_mode()
            print(Fore.GREEN + "[*] Modo Kali Linux concluído")
            return
    
    # Rest of the original functionality
    if len(sys.argv) > 1:
        target = sys.argv[1]
        print(Fore.YELLOW + f"[*] Iniciando reconhecimento para: {target}")
        
        try:
            ipaddress.ip_address(target)
            shodan_lookup(target)
        except ValueError:
            print(Fore.RED + "[!] Erro: IP inválido")
            sys.exit(1)
    else:
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
