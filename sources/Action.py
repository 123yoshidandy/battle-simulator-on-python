# coding: utf-8


from random import random

from Commons import *


class Action:

    @classmethod
    @log
    def get_hit(cls, actor, target):
        return 0.95

    @classmethod
    @log
    def get_critical(cls, actor, target):
        return 0.05

    @classmethod
    @log
    def attack(cls, actor, target):

        if cls.get_hit(actor, target) > random():

            if cls.get_critical(actor, target) > random():
                damage = max(2 * actor.atk, 1)
                print("Critical Attack! Damage of " + str(damage) + " to " + target.name)

            else:
                damage = max(2 * actor.atk - target.defe, 1)
                print("Attack! Damage of " + str(damage) + " to " + target.name)
            target.hp = max(target.hp - damage, 0)

        else:
            print("Attack! Miss...")

    @classmethod
    @log
    def magic(cls, actor, target):
        dec_mp = 3
        if actor.mp >= dec_mp:
            damage = max(3 * actor.int, 10)
            print("Magic! Damage of " + str(damage) + " to " + target.name)
            target.hp = max(target.hp - damage, 0)
            actor.mp = max(actor.mp - dec_mp, 0)
        else:
            print("Magic! Miss...")

    @classmethod
    @log
    def heal(cls, actor, target):
        dec_mp = 3
        if actor.mp >= dec_mp:
            add_hp = 10 + actor.int * 2
            print("Heal! Recovery of " + str(add_hp) + " to " + target.name)
            target.hp = min(target.hp + add_hp, target.hp_max)
            actor.mp = max(actor.mp - dec_mp, 0)
        else:
            print("Heal! Miss...")
