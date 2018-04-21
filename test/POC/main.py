#!/usr/bin/env python

"""
002_display_fps_pretty.py

Display framerate and playtime.
Works with Python 2.7 and 3.3+.

URL:     http://thepythongamebook.com/en:part2:pygame:step002
Author:  yipyip
License: Do What The Fuck You Want To Public License (WTFPL)
         See http://sam.zoy.org/wtfpl/

         altered for Castle's evil purposes; a POC of the "tower UI" for edh
"""

####


import pygame_sdl2
pygame_sdl2.import_as_pygame()

import pygame

import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


class PygView(object):

    hand = []

    deck = ["first card", "second card", "third card"]

    def __init__(self, width=640, height=400, fps=30):
        """Initialize pygame, window, background, font,...
        """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 20, bold=True)


    def run(self):
        """The mainloop
        """
        running = True
        pos = "poop"
        show_hand = False
        while running:
            pos = pygame.mouse.get_pos()  # [width, height]

            hand_button = (38, 160)
            drawcard_button = (38, 360)

            draw_clicked = False
            hand_clicked = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.check_collision_with_button(pos, drawcard_button):
                        if self.deck:
                            self.hand.append(self.deck.pop())
                        draw_clicked = True
                    elif self.check_collision_with_button(pos, hand_button) and not show_hand:
                        hand_clicked = True

            if show_hand and not draw_clicked:
                x = 50
                y = 100
                for card in self.hand:
                    self.draw_text(card, (x, y))
                    y += 30
            elif not show_hand and hand_clicked:
                show_hand = True
            elif show_hand and draw_clicked:
                show_hand = False

            if not show_hand:
                self.draw_button("hand_button", hand_button)
            self.draw_button("drawcard_button", (38, 360))

            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds / 1000.0
            self.draw_pos_text("Position of mouse = {}".format(str(pos)))


            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))

        pygame.quit()

    def draw_pos_text(self, text):
        """Center text in window
        """
        fw, fh = self.font.size(text) # fw: font width,  fh: font height
        surface = self.font.render(text, True, (0, 255, 0))
        # // makes integer division in python3
        self.screen.blit(surface, ((self.width - fw) // 2, (self.height - fh) // 2))

    def draw_text(self, text, pos):
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, (0, 255, 0))
        self.screen.blit(surface, pos)

    def draw_button(self, which_button, pos):
        button = pygame.image.load(os.path.join(ROOT, 'assets', '{}.jpg'.format(which_button)))
        button = pygame.transform.scale(button, (100, 75))
        self.screen.blit(button, pos)
        return pos



    @staticmethod
    def check_collision_with_button(click_pos, button_pos):
        if button_pos[0] < click_pos[0] < button_pos[0] + 100:
            if button_pos[1] < click_pos[1] < button_pos[1] + 75:
                return True
        return False


####

if __name__ == '__main__':

    # call with width of window and fps
    PygView(400, 800).run()