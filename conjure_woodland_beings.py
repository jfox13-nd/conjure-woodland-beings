#!/usr/bin/env python3

""" conjure_woodland_beings.py: A simple tool to help DMs randomly determine the creatured spawned by the Dungeons and Dragons 5th Edition spell Conjure Woodland Beings """

__author__ = "Jack Fox"
__email__ = "jfox13@nd.edu"

import random
import sys
from fractions import Fraction
import argparse

# A dictionary of monsters, organized by CR and including each monster's name, source, page number
fey_monsters = {
    "2": [
        ("Darkling Elder", "Volo's Guide to Monsters", 134),
        ("Meenlock", "Volo's Guide to Monsters", 170),
        ("Sea Hag", "Monster Manual", 179)
    ],
    "1": [
        ("Quickling", "Volo's Guide to Monsters", 187),
        ("Dryad", "Monster Manual", 121)
    ],
    "1/2": [
        ("Darkling", "Volo's Guide to Monsters", 134),
        ("Satyr", "Monster Manual", 267)
    ],
    "1/4": [
        ("Blink Dog", "Monster Manual", 318),
        ("Pixie", "Monster Manual", 253),
        ("Sprite", "Monster Manual", 283)
    ],
    "1/8": [
        ("Boggle", "Volo's Guide to Monsters", 128)
    ]
}

# The number of monsters conjured for each CR
cr_mapping = {"1/4": 8, "1/2": 4, "1": 2, "2": 1}
monster_crs = ("1/8", "1/4", "1/2", "1", "2")

def rand_monster_from_range(max_cr: str, min_cr: str) -> tuple:
    """ Retrieve a random monster in the specified inclusive CR range """ # max_cr: fractions.Fraction, min_cr: fractions.Fraction
    possible_monsters = []
    max_cr = Fraction(max_cr)
    min_cr = Fraction(min_cr)

    for cr in fey_monsters:
        if Fraction(cr) >= min_cr and Fraction(cr) <= max_cr:
            for monster in fey_monsters[cr]:
                possible_monsters.append(monster)

    return possible_monsters[random.randint(0,len(possible_monsters)-1)]

def collect_from_range(max_cr: str, min_cr: str, max_monsters: int) -> dict:
    """ Collects a number of random monsters from a specified CR range """
    monsters_conjured = {}
    total_monsters = 0

    while total_monsters < cr_mapping[max_cr] and len(monsters_conjured) < max_monsters:
        next_monster = rand_monster_from_range(Fraction(max_cr), Fraction(min_cr))
        if next_monster in monsters_conjured:
            monsters_conjured[next_monster] += 1
        else:
            monsters_conjured[next_monster] = 1
        total_monsters += 1

    for _ in range(cr_mapping[max_cr] - total_monsters):
        next_monster = random.choice(list(monsters_conjured.keys()))
        monsters_conjured[next_monster] += 1

    return monsters_conjured

def get_monster_cr(monster: tuple) -> str:
    """ Get the CR of a given monster """
    for cr in fey_monsters:
        for fey_monster in fey_monsters[cr]:
            if fey_monster == monster:
                return cr
    return None

def display_monsters(monsters_conjured: dict) -> None:
    """ Print out monster information """
    for monster in monsters_conjured:
        print("{} x {}".format(monster[0],monsters_conjured[monster]))
        cr = get_monster_cr(monster)
        print("\tCR {}, {}, {}\n".format(cr,monster[1],monster[2]))

if __name__ == "__main__":
    # parse arguments
    parser = argparse.ArgumentParser(description='Randomly determine the creatured spawned by the Dungeons and Dragons 5E spell Conjure Woodland Beings.CRs must be 2, 1, 1/2, 1/4, or 1/8.')
    parser.add_argument("MAXCR", type=str, 
                    help="The maximum CR of conjured monsters, minimum 1/4" )
    parser.add_argument('MINCR', nargs='?', type=str, default="", 
                    help="The minimum CR of conjured monsters (default MAXCR)")
    parser.add_argument('--max-monsters', type=int, default=8,
                    help='Set a maximum number of unique monster types')
    args = parser.parse_args()

    if not args.MINCR:
        args.MINCR = args.MAXCR

    if args.MAXCR not in monster_crs[1:]:
        print("{}: error: MAXCR is not a valid CR".format(__file__))
        parser.print_help()
        sys.exit(1)

    if args.MINCR not in monster_crs:
        print("{}: error: MINCR is not a valid CR".format(__file__))
        parser.print_help()
        sys.exit(1)

    if args.max_monsters < 1:
        print("{}: error: --max-monsters must be set to at least 1".format(__file__))
        parser.print_help()
        sys.exit(1)
    
    monsters_conjured = collect_from_range(args.MAXCR, args.MINCR, args.max_monsters)
    display_monsters(monsters_conjured)