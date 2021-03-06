# TheJokesAPI

this is a simple web server that will tell jokes, this also has an API

# Showcase (images)

![Screenshot_20220317_151434](https://user-images.githubusercontent.com/36286877/158782061-978ec562-0061-43f6-80f9-22b0262fd029.png)

![Screenshot_20220317_151458](https://user-images.githubusercontent.com/36286877/158782132-cc25a515-c845-4b8f-8728-3c383a0a892b.png)

![Screenshot_20220317_151549](https://user-images.githubusercontent.com/36286877/158782291-0580c5bb-1f77-4f3f-a71e-4303ab94d4d4.png)

![Screenshot_20220317_151605](https://user-images.githubusercontent.com/36286877/158782328-ac566e91-d62f-4407-88e4-c2b4541311ed.png)

# Endpoints

## UI

- `/` or `/joke`
  - return a User Interface with the joke and the category from `jokes.json`
- `/wocka`
  - return a User Interface with the joke and the category from `wocka.json`
- `/stupidstuff`
  - return a User Interface with the joke and the category from `stupidstuff.json`

## API

- ### Information -
  - `/api` - returns a HTML User Interface with basic information and endpoint URLs
- ### Endpoints -
  - `/api/jokes`
    - return a json with a randomly select joke from `jokes.json`
  - `/api/wocka`
    - return a json with a randomly select joke from `wocka.json`
  - `/api/stupidstuff`
    - return a json with a randomly select joke from `stupidstuff.json`

# Installation

## Arch Linux

run the commands below, line by line

```bash
sudo pacman -Syy wget --noconfirm
wget "https://raw.githubusercontent.com/hirusha-adi/Jokes/setup/arch.sh"
chmod +x ./arch.sh
./arch.sh
```

## Ubuntu/Debain

run the commands below, line by line

```bash
sudo apt install wget -y
wget "https://raw.githubusercontent.com/hirusha-adi/Jokes/setup/ubuntu.sh"
chmod +x ./ubuntu.sh
./ubuntu.sh
```

## Windows

1. Download and install Python3. Make sure to 'Add to PATH' when install python3

![imagew1](https://www.tutorials24x7.com/uploads/2019-12-26/files/3-tutorials24x7-python-windows-install.png)

2. Download the code as a .zip file from [this Github Reposotory](https://github.com/hirusha-adi/Discord-Channel-Attacthment-Save)

![imagew2](https://cdn.discordapp.com/attachments/935515175073763398/937186561299197952/unknown.png)

(this above image might not be the same)

3. Extract the downloaded `.zip` file

4. open `cmd` or `powershell` in that folder

5. run the command below to install requirements

```
python -m pip install -r requirements.txt
```

6. run the command below to start the prorgam

```
python app.py
```

## "it's just a joke" ~ nobody. lol
