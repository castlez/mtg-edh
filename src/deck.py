"""
Class for a deck
equipped to import decklists from tappedout.com
"""
from random import shuffle

from src.helper import CardOps


class Deck:
    def __init__(self, filename):
        cards_in_deck = []
        commander = None
        with open(filename, 'r') as deck_file:
            for raw_line in deck_file.readlines():
                line = raw_line.split(' ')
                number = int(line[0].split('x')[0])
                card_name = ' '.join([x for x in line[1:] if '#' not in x and '*' not in x])
                card = CardOps.get_card(card_name)
                print("adding card {}".format(card.name))
                if '*CMDR*' in line:
                    commander = card
                else:
                    cards_in_deck.append([card for _ in range(number)])

        self.deck = cards_in_deck
        self.commander = commander
        self.deck_list = [self.commander] + self.deck
        self.graveyard = []

    def shuffle_deck(self):
        self.deck = shuffle(self.deck)

    def draw(self, number_to_draw=1):
        return self.deck.pop() if number_to_draw == 1 else [self.deck.pop() for i in range(number_to_draw)]

    def discard(self, card):
        self.graveyard.insert(0, card)
