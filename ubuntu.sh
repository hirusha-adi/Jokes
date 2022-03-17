echo "Installing Dependencies"
sudo apt install install git python3 python3-pip -y
echo "Installed git, python, python-pip with apt"
git clone "https://github.com/hirusha-adi/Jokes.git"
cd ./Jokes
pip3 install -r requirements.txt
echo "Installed dependencies with pip"
python3 app.py