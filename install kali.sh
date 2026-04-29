#!/bin/bash
echo "Instalando a ferramenta..."
apt update && apt upgrade -y
git clone https://github.com/seu-usuario/nome-da-ferramenta.git
cd nome-da-ferramenta
pip3 install -r requirements.txt
python3 tool.py
