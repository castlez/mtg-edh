# coding=utf-8
"""
Class for helper functions cuz I'm lazy
"""
import os

import requests
import json

ROOT = os.path.dirname(os.path.dirname(__file__))
card_cache = os.path.join(ROOT, 'card_cache')

weird_names = {'tappedout name' : 'real name',
                   'Lim-Dul\'s Vault' : r'Lim-Dûl\'s Vault'}


class CardOps:

    @staticmethod
    def get_card(name):
        """
        Grabs a card by name, specifically the first one in the list of sets
        :param name: name of the card, derp derp
        :return: the card, derp
        """
        if name in weird_names:
            name = weird_names[name]
        cached = CardOps.check_card_cache(name)
        if not cached:
            print "Card not in cache, downloading"
            response = requests.get("https://api.magicthegathering.io/v1/cards?name={}".format(name))
            card = json.loads(response.content)["cards"][0]
            CardOps.add_to_cache(card)
            return card
        print "card in cache, no download needed"
        return cached

    @staticmethod
    def check_card_cache(name):
        if not os.path.exists(card_cache):
            os.mkdir(card_cache)
        for filename in os.listdir(card_cache):
            if filename == name:
                return json.loads(open(os.path.join(card_cache, filename)).read())
        return False

    @staticmethod
    def add_to_cache(card):
        if not os.path.exists(card_cache):
            os.mkdir(card_cache)
        with open(os.path.join(card_cache, card["name"]), 'w') as outfile:
            outfile.write(json.dumps(card))
