#!/bin/bash
echo "Installing Dependencies"
sudo pacman -Syy install git python python-pip --noconfirm
echo "Installed git, python, python-pip with apt"
git clone "https://github.com/hirusha-adi/Jokes.git"
cd ./Jokes
pip install -r requirements.txt
echo "Installed dependencies with pip"
python app.py