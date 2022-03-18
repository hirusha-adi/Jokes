#!/bin/bash
mkdir ./compile
cp ./* ./compile -r
cd ./compile
python3 -m PyInstaller --noconfirm --onedir --name "Jokes" ./app.py
cp ./database ./dist/Jokes/ -r
cp ./templates ./dist/Jokes/ -r
cp ./config.json ./dist/Jokes/
rm compile.sh config.json database/ LICENSE __pycache__/ README.md requirements.txt templates/ build/ app.py Jokes.spec README.md compile -rf

echo "Code compiled with PyInstaller" 

folder_name="$(lsb_release -ds)"
cd ..
mkdir ./dist
cd ./dist
mkdir "./$folder_name"
cd "./$folder_name"
mv ./../../compile/dist/Jokes/* .

echo "Moved output to $(pwd)"
echo "DONE :)"