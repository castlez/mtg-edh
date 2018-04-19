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
import os

import pygame


ROOT = os.path.dirname(os.path.dirname(__file__))

hand = []

deck = ["first card", "second card", "third card"]

####

class PygView(object):


    def __init__(self, width=640, height=400, fps=30):
        """Initialize pygame, window, background, font,...
        """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        #self.height = width // 4
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
        while running:
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = "poop"

            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds / 1000.0
            #self.draw_text("Position of mouse = {}".format(str(pos)))
            self.draw_button("hand_button", (0, 0))

            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))

        pygame.quit()


    def draw_text(self, text):
        """Center text in window
        """
        fw, fh = self.font.size(text) # fw: font width,  fh: font height
        surface = self.font.render(text, True, (0, 255, 0))
        # // makes integer division in python3
        self.screen.blit(surface, ((self.width - fw) // 2, (self.height - fh) // 2))

    def draw_button(self, which_button, pos):
        button = pygame.image.load(os.path.join(ROOT, 'assets', '{}.jpg'.format(which_button)))
        self.screen.blit(button, pos)


####

if __name__ == '__main__':

    # call with width of window and fps
    PygView(400, 800).run()