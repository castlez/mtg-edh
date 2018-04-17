"""
Main game loop for edh
"""
import os

from src.deck import Deck
from src.player import Player

root = os.path.dirname(os.path.dirname(__file__))


def play_game(players):
    commanders = ', '.join([fuck.deck.commander.name for fuck in players])
    print("got {} players, with the following commanders: {}".format(len(players), commanders))


if __name__ == "__main__":
    deck1 = os.path.join(root, 'test', 'test_deck_1')
    p = Player(Deck(deck1))
    play_game([p, p])  # hehe