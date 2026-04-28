#!/bin/bash
echo "Instalando a ferramenta..."
pkg update && pkg upgrade -y
git clone https://github.com/seu-usuario/nome-da-ferramenta.git
cd nome-da-ferramenta
pip install -r requirements.txt
python tool.py
