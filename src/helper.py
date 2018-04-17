"""
Class for helper functions cuz I'm lazy
"""
from mtgsdk import Card

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
        card = Card.where(name=name).all()[0]
        return card
