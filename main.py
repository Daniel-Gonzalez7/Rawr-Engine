from game import Game
from board import Board
import pygame as p


WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {} #image dictionary

def load_images():
    white_pieces = ['P', 'R', 'B', 'N', 'Q', 'K']
    black_pieces = ['p', 'r', 'b', 'n', 'q', 'k']

    for piece in white_pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/w" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    
    for piece in black_pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/b" + piece.upper() + ".png"), (SQ_SIZE, SQ_SIZE))

def main():
    board = Board("r4rk1/ppp2ppp/8/3pP1qP/3P4/2P2Q2/PP1n4/R4R1K w - - 0 1")
    load_images()
    p.init()
    game_display = p.display.set_mode((HEIGHT,WIDTH))
    p.display.set_caption('Chess')
    game_display.fill(p.Color('White'))
    clock = p.time.Clock()
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        draw_game(game_display, board)
        p.display.update()
        clock.tick(60)   
    p.quit()
    quit()

def draw_game(screen, board):
    draw_board(screen)
    draw_pieces(screen, board)


def draw_board(screen):
    colors = [p.Color(239,239,239), p.Color(136,119,183)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r+c)%2]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board.board[r][c]
            if piece != '-':
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))



if __name__ == "__main__":
    main()

