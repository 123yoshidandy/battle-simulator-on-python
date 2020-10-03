# coding: utf-8


from Battle import Battle
from Party import Party
from Commons import *


def main():
    party1 = Party.import_file("party1")
    party2 = Party.import_file("enemy1")

    for character in party1.members:
        character.set_friend(party1)
        character.set_enemy(party2)

    for character in party2.members:
        character.set_friend(party2)
        character.set_enemy(party1)

    winner = Battle((party1, party2)).run()

    print_line()
    print_line()
    print(winner.name + " is WIN !")
    print_line()
    print_line()


if __name__ == '__main__':
    main()
