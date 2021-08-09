STARTING_POSITION = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

class Board:
    def __init__(self, fen=STARTING_POSITION):
        rows, cols = (8,8)
        self.board = [['']*8 for i in range(8)] #initialize 8*8 grid
        self.set_board(fen)

    #set the board based on the fen inputted
    def set_board(self, fen):
        fen_items = fen.replace(' ', '/').split('/')
        for row, fen_row in enumerate(fen_items):
            if row == 8:
                break
            col = 0
            for char in fen_row:
                if char.isalpha(): #put piece on square
                    self.board[row][col] = char
                    col += 1
                elif char.isnumeric(): #populate empty squares
                    for i in range(int(char)):
                        self.board[row][col] = '-'
                        col += 1

    #print the position
    def print_position(self):
        for row in self.board:
            print('\n')
            for val in row:
                print(val, end='')











