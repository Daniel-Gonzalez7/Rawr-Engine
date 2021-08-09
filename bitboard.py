from itertools import product


SQUARES = {}


def set_squares():
    ranks = range(8, 0, -1)
    files = ("a", "b", "c", "d", "e", "f", "g", "h")
    # rank,file is the key (ie a2)
    # the value in SQUARES is value. IE 64. So SQUARES["h1"]=64
    for value, (rank, file) in enumerate(product(ranks, files)):
        SQUARES[f"{file}{rank}"] = value


# returns 1 if the given square on the board matches with the bitboard value
def get_bit(bitboard, square):
    return 1 if bitboard & (1 << square) else 0


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


set_squares()

bitboard = 0
bitboard = set_bit(bitboard, SQUARES["h8"])
print_bitboard(bitboard)
