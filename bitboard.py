from itertools import product
from enum import Enum


class Side(Enum):
    White, Black = 0, 1

# constants for not_files. Helpful for attack table generation
NOT_A_FILE = 0xFEFEFEFEFEFEFEFE  # ~0x0101010101010101
NOT_H_FILE = 0x7F7F7F7F7F7F7F7F  # ~0x8080808080808080

NOT_GH_FILE = 4557430888798830399
NOT_AB_FILE = 18229723555195321596

"""
example of NOT_AB_FILE represented as a bitboard:

8   0  0  1  1  1  1  1  1
7   0  0  1  1  1  1  1  1
6   0  0  1  1  1  1  1  1
5   0  0  1  1  1  1  1  1
4   0  0  1  1  1  1  1  1
3   0  0  1  1  1  1  1  1
2   0  0  1  1  1  1  1  1
1   0  0  1  1  1  1  1  1

    a  b  c  d  e  f  g  h
"""


# square dictionary for every square on the board
SQUARES = {}

#########################################
###BITBOARD REPRESENTATION####
#########################################


def set_squares():
    ranks = range(8, 0, -1)
    files = ("a", "b", "c", "d", "e", "f", "g", "h")
    # rank, file is the key (ie a2)
    # the value in SQUARES is value. IE 64. So SQUARES["h1"]=64
    for value, (rank, file) in enumerate(product(ranks, files)):
        SQUARES[f"{file}{rank}"] = value


# returns 1 if the given square on the board matches with the bitboard value
def get_bit(bitboard, square):
    return 1 if bitboard & (1 << square) else 0


def pop_bit(bitboard, square):
    return bitboard ^ (1 << square) if get_bit(bitboard, square) else bitboard


# adds a square to the bitboard
def set_bit(bitboard, square):
    return bitboard | (1 << square)


def print_bitboard(bitboard):
    print("\n")
    for rank in range(0, 8):
        for file in range(0, 8):
            print(f"{8 - rank}  " if not file else "", end="")  # ranks
            square = rank * 8 + file
            # print bit state
            print(f" {get_bit(bitboard, square)} ", end="\n" if file == 7 else "")
    print("\n    a  b  c  d  e  f  g  h\n")  # files

    # return decimal value of bitboard
    print("    bitboard:", bitboard)


#########################################
###BITBOARD REPRESENTATION####
#########################################


#########################################
###ATTACK TABLES####
#########################################

# pawn attack table [side][square]
pawn_attacks = [[0] * 2 for _ in range(64)]

# generate pawn attacks. considers current square and current side (white or black)
def mask_pawn_attacks(square, side):
    # set bit on bitboard
    bitboard = set_bit(0, square)

    # bitboard of attacks
    attacks = 0

    if side == Side.White:
        # note that we need to & with NOT_A_FILE
        # in order to prevent wrapping to the next rank when shifting
        attacks |= (bitboard >> 7) & NOT_A_FILE  # northeast
        attacks |= (bitboard >> 9) & NOT_H_FILE  # northwest
    else:
        attacks |= bitboard << 7  & NOT_H_FILE # southwest
        attacks |= bitboard << 9  & NOT_A_FILE # southeast

    return attacks


#########################################
###ATTACK TABLEs TABLES####
#########################################


set_squares()


print_bitboard(mask_pawn_attacks(SQUARES["h4"], Side.Black))


# print_bitboard(mask_pawn_attacks(SQUARES["h4"], Side.White))
