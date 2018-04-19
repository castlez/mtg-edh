"""
Main game loop for edh
"""
import os
import pygame

from src.deck import Deck
from src.player import Player

root = os.path.dirname(os.path.dirname(__file__))


def play_game(players):
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    background = pygame.Surface(screen.get_size())
    background.fill(255,255,255)
    background.convert(background)
    screen.blit(background, (0, 0))
    #commanders = ', '.join([fuck.deck.commander.name for fuck in players])
    #print("got {} players, with the following commanders: {}".format(len(players), commanders))


if __name__ == "__main__":
    deck1 = os.path.join(root, 'test', 'test_deck_1')
    p = Player(Deck(deck1))
    play_game([p, p])  # hehe