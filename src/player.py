"""
Class for a player
"""


class Player:

    def __init__(self, deck):
        self.life_total = 40
        self.deck = deck
        self.poison_counters = 0
