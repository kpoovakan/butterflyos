import wasp
import time
import json
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("butterflytools")
os.chdir("jambahasa")

'''with open("jambahasa.json", "r", encoding="utf-8") as file:
    global translate
    translate = json.load(file)
    input = input("Enter any English word: ")
    translation = translate.get(input, "No results")
    print(translation)'''

class JambahasaApp():
    NAME = "Bahasa"
    def __init__(self):
        with open("jambahasa.json", "r", encoding="utf-8") as file:
                global translate
                translate = json.load(file)

    def foreground(self):
        self._draw()

    def _draw(self):
     draw = wasp.watch.drawable
     draw.fill()
     draw.string("Welcome to Jambahasa!")

    def _update(self):
     draw = wasp.watch.drawable
     draw.fill()
     draw.string(translation)

    def getTranslation(input):
     global translation
     translation = translate.get(input, "No results")