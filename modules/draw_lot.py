import json
import random
import os

class LotDivination:
    def __init__(self):
        with open("data/lot_book.json","r",encoding="utf-8") as f:
            self.lots = json.load(f)

    def draw(self):
        return random.choice(self.lots)
