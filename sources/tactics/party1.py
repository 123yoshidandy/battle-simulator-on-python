# coding: utf-8

from random import choice

PARTY_NAME = "party1"
CHARACTERS = [
    {
        "name": "Hero",
        "class_name": "hero",
    },
    {
        "name": "Healer",
        "class_name": "healer",
    },
]


def tactics(actor, fiends, enemies):
    if "heal" in actor.actions and actor.mp >= 3:
        return "heal",  choice(actor.friend.get_survivors())

    target = choice(actor.enemy.get_survivors())
    return "attack", target
