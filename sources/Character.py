# coding: utf-8


from Commons import *


class Character:

    @log
    def __init__(self, name, class_name, hp, mp, _str, vit, _int, agi, actions=[]):
        self.name = name
        self.class_name = class_name

        self.hp_max = hp
        self.mp_max = mp
        self.str = _str
        self.vit = vit
        self.int = _int
        self.agi = agi

        self.hp = self.hp_max
        self.mp = self.mp_max
        self.atk = self.str
        self.defe = self.vit
        self.actions = ["attack", "guard"]
        self.actions.extend(actions)
        self.conditions_loop = {}
        self.conditions_turn = {}
        self.friend = None
        self.enemy = None

    @classmethod
    @log
    def create_class_character(cls, name, class_name):

        if class_name == "hero":
            return Character(name, class_name, 150, 10, 15, 15, 10, 10)
        elif class_name == "healer":
            return Character(name, class_name, 100, 10, 10, 10, 15, 10, ['heal'])
        elif class_name == "slime":
            return Character(name, class_name,  50, 10, 10, 10, 10, 10)
        elif class_name == "zombie":
            return Character(name, class_name, 100, 10, 10,  5,  5,  5)
        elif class_name == "dragon":
            return Character(name, class_name, 150, 10, 15, 10, 10, 10)
        else:
            return Character(name, class_name, 100, 10, 10, 10, 10, 10)

    @log
    def set_friend(self, party):
        self.friend = party

    @log
    def set_enemy(self, party):
        self.enemy = party
