# coding: utf-8


from importlib import import_module

from Character import Character
from Commons import *


class Party:

    @log
    def __init__(self, name="", members=None, tactics=None):
        self.name = name
        self.members = members
        self.tactics = tactics
        self.conditions_loop = {}
        self.conditions_turn = {}

    @log
    def get_survivors(self):
        survivors = []
        for members in self.members:
            if "dead" not in members.conditions_loop:
                survivors.append(members)
        return survivors

    @classmethod
    @log
    def import_file(cls, party_name):

        module = import_module("tactics." + party_name)
        characters = []
        for character in module.CHARACTERS:
            characters.append(Character.create_class_character(character["name"], character["class_name"]))

        return Party(
            name=module.PARTY_NAME,
            members=characters,
            tactics=module.tactics
        )
