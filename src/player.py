# coding=utf-8
"""
Class for a player
"""
from random import shuffle

from src.helper import CardOps


class Player:

    def __init__(self, deck_file):
        self.life_total = 40
        self.deck = []
        self.graveyard = []
        self.hand = []
        self.commander = ""
        self.poison_counters = 0

        self.import_deck(deck_file)

    def import_deck(self, filename):
        # TODO: add a cache so you don't have to download every time

        # open the file and get each card from the mtgsdk
        with open(filename, 'r') as deck_file:
            for raw_line in deck_file.readlines():
                line = raw_line.split(' ')
                number = int(line[0].split('x')[0])
                card_name = ' '.join([x for x in line[1:] if '#' not in x and '*' not in x])
                print("adding card {}".format(card_name.encode('utf-8')))
                card = CardOps.get_card(card_name)
                if '*CMDR*' in line:
                    self.commander = card
                else:
                    self.deck.append([card for _ in range(number)])

    def shuffle_deck(self):
        self.deck = shuffle(self.deck)

    def draw(self, number_to_draw=1):
        return self.deck.pop() if number_to_draw == 1 else [self.deck.pop() for i in range(number_to_draw)]

    def discard(self, card):
        self.graveyard.insert(0, card)
