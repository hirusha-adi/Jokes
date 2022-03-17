from flask import Flask, redirect, render_template
import os
import json
import random
import requests


class FileName:
    _cwd = os.getcwd()

    static_folder = os.path.join(_cwd, "templates")
    templates_folder = os.path.join(_cwd, "static")

    jokes = os.path.join(_cwd, "database", "jokes.json")
    wocka = os.path.join(_cwd, "database", "wocka.json")
    stupidstuff = os.path.join(_cwd, "database", "stupidstuff.json")


class Settings:
    with open(os.path.join(os.getcwd(), "config.json"), "r", encoding="utf-8") as _file:
        data = json.load(_file)

    try:
        host = data["host"]
        if not(len(str(host).split(".")) == 4):
            host = "0.0.0.0"
    except KeyError:
        host = "0.0.0.0"

    try:
        port = data["port"]
        try:
            port = int(port)
        except ValueError:
            port = 8080
    except KeyError:
        port = 8080

    try:
        debug = data["debug"]
        if isinstance(debug, str):
            if debug.lower() in ("true", "yes", "t", "y"):
                debug = True
            else:
                debug = False
        elif isinstance(debug, bool):
            pass
        else:
            debug = False
    except KeyError:
        debug = False


class Database:
    def __init__(self):
        self.jokes = None
        self.jokes_lenght = None
        self.wocka = None
        self.wocka_length = None
        self.stupidstuff = None
        self.stupidstuff_length = None

    # Jokes (Main)
    # ------------------------------
    def _loadJokes(self):
        # create the file if not exists
        if not(os.path.exists(FileName.jokes)):
            r = requests.get(
                "https://raw.githubusercontent.com/hirusha-adi/TheJokeAPI/main/database/jokes.json").content
            with open(FileName.jokes, "wb") as fmake:
                fmake.write(r)
        # Load the jokes
        with open(FileName.jokes, "r", encoding="utf-8") as file:
            self.jokes = json.load(file)
        self.jokes_lenght = len(self.jokes)

    def getJoke(self):
        if self.jokes is None:
            self._loadJokes()
        return self.jokes[random.randint(0, self.jokes_lenght - 1)]

    # Wocka
    # ------------------------------
    def _loadWocka(self):
        # create the file if not exists
        if not(os.path.exists(FileName.wocka)):
            r = requests.get(
                "https://raw.githubusercontent.com/hirusha-adi/TheJokeAPI/main/database/wocka.json").content
            with open(FileName.wocka, "wb") as fmake:
                fmake.write(r)
        # Load the wocka jokes
        with open(FileName.wocka, "r", encoding="utf-8") as file:
            self.wocka = json.load(file)
        self.wocka_length = len(self.wocka)

    def getWocka(self):
        if self.wocka is None:
            self._loadWocka()
        return self.wocka[random.randint(0, self.wocka_length - 1)]

    # Stupidstuff
    # ------------------------------
    def _loadStupidStuff(self):
        # create the file if not exists
        if not(os.path.exists(FileName.stupidstuff)):
            r = requests.get(
                "https://raw.githubusercontent.com/hirusha-adi/TheJokeAPI/main/database/stupidstuff.json").content
            with open(FileName.stupidstuff, "wb") as fmake:
                fmake.write(r)
        # Load the stupidstuff jokes
        with open(FileName.stupidstuff, "r", encoding="utf-8") as file:
            self.stupidstuff = json.load(file)
        self.stupidstuff_length = len(self.stupidstuff)

    def getStupidStuff(self):
        if self.stupidstuff is None:
            self._loadStupidStuff()
        return self.stupidstuff[random.randint(0, self.stupidstuff_length - 1)]


app = Flask(__name__,
            static_folder=FileName.static_folder,
            template_folder=FileName.templates_folder
            )

dbobj = Database()


@app.route("/jokes")
def jokes():
    return str(dbobj.getJoke())


@app.route("/wocka")
def wocka():
    return str(dbobj.getWocka())


@app.route("/stupidstuff")
def stupidstuff():
    return str(dbobj.getStupidStuff())


def runTheJokesAPI():
    app.run(Settings.host,
            port=Settings.port,
            debug=Settings.debug)


if __name__ == "__main__":
    runTheJokesAPI()
