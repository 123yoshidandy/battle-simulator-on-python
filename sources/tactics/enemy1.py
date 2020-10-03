# coding: utf-8

from random import choice

PARTY_NAME = "enemy1"
CHARACTERS = [
    {
        "name": "Slime",
        "class_name": "slime",
    },
    {
        "name": "Zombie",
        "class_name": "zombie",
    },
    {
        "name": "Dragon",
        "class_name": "dragon",
    },
]


def tactics(actor, fiends, enemies):
    target = choice(actor.enemy.get_survivors())
    return "attack", target
