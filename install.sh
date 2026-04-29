#!/bin/bash
echo "Instalando a ferramenta..."
sudo apt update && apt upgrade -y
git clone https://github.com/stickman79/nmsho
cd nmsho
python nmsho.py
