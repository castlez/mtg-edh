"""
Main game loop for edh
"""
import os
# Allow pygame_sdl2 to be imported as pygame.
import pygame_sdl2
pygame_sdl2.import_as_pygame()
import pygame

from src.player import Player

ROOT = os.path.dirname(os.path.dirname(__file__))

players = []
player_buttons = {}
screen_w = 0
screen_h = 0


class Game(object):

    def __init__(self):
        """Initialize pygame, window, background, font,...
        """
        pygame.init()
        self.screen = pygame.display.set_mode((720, 1280))
        self.screen_w, self.screen_h = self.screen.get_size()
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.screen.blit(self.background, (0, 0))
        self.font = pygame.font.SysFont('mono', 20, bold=True)

    def save_state(self):
        """
        Saves the game state.
        """

        with open("state.txt", "w") as f:
            f.write(players)

    def load_state(self):
        try:
            with open("state.txt", "r") as f:
                players = []  # TODO: state
            return players
        except Exception:
            return None

    def delete_state(self):
        if os.path.exists("state.txt"):
            os.unlink("state.txt")

    def draw_pos_text(self, text):
        """Center text in window
        """
        fw, fh = self.font.size(text) # fw: font width,  fh: font height
        surface = self.font.render(text, True, (0, 255, 0))
        # // makes integer division in python3
        self.screen.blit(surface, ((self.screen_w - fw) // 2, (self.screen_h - fh) // 2))

    def draw_button(self, which_button, pos):
        button = pygame.image.load(os.path.join(ROOT, 'assets', '{}.jpg'.format(which_button)))
        button = pygame.transform.scale(button, (100, 75))
        self.screen.blit(button, pos)
        return pos

    def draw_player_columns(self):
        col = 1
        for player in players:
            x = (screen_w/4)*col
            y = screen_h


def main():
    game = Game()

    sleeping = False

    # On startup, load state saved by APP_WILLENTERBACKGROUND, and then delete
    # that state.
    players = game.load_state()

    game.delete_state()

    while True:
        # If not sleeping, draw the screen.
        if not sleeping:
            game.screen.fill((0, 0, 0, 255))

            if not players:
                # TODO: right now just hard start with two decks
                pass

            pos = pygame.mouse.get_pos()  # [width, height]
            game.draw_pos_text("Position of mouse = {}".format(str(pos)))

            #game.draw_player_columns()

            pygame.display.flip()
            game.screen.blit(game.background, (0, 0))


if __name__ == "__main__":
    deck1 = os.path.join(ROOT, 'test', 'test_deck_1')
    p = Player(deck1)
    players = [p]
    main()