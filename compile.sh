#!/bin/bash
mkdir compile
cp ./* ./compile -r
cd ./compile
python3 -m PyInstaller --noconfirm --onedir --name "Jokes" ./app.py
cp ./database ./dist/Jokes/
cp ./config.json ./dist/Jokes/
echo "Compiled"