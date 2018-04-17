"""
Main game loop for edh
"""
import os

from src.deck import Deck
from src.player import Player

root = os.path.dirname(os.path.dirname(__file__))


def play_game(decks):
    players = [Player(deck) for deck in decks]
    print("got {} players, with the following commanders: {}".format(len(players),
                                                                     ', '.join([fuck.deck.commander.name for fuck in players])))


if __name__ == "__main__":
    deck1 = os.path.join(root, 'test', 'test_deck_1')
    play_game([Deck(deck1), Deck(deck1)])