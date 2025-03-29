import pygame
import sys
from random import choice, randint

pygame.init()


class TetrisApp:
    TILE_SIZE = 30  # Actual Pixel Size
    BOARD_WIDTH = 10
    BOARD_HEIGHT = 20

    COlORS = [
        (0,0,0),
        (255,255,255),
        (153, 255, 51),
        (255, 153, 51),
        (255, 102, 204),
        (204, 153, 255),
        (21, 255, 255),
        (53, 102, 204),
        (0, 153, 153),
    ]

    SHAPES = [
        [1, 1, 1, 1],  #I
        [[1, 1, 1],
         [0, 1, 0]],  #T
        [[0, 1, 1],
         [1, 1, 0]],  #S
        [[1, 1, 0],
         [0, 1, 1]],  #Z
        [[1, 1],  #ㅁ
         [1, 1]],
        [[1, 1, 1],
         [1, 0, 0]],
        [[1, 1, 1],
         [0, 0, 1]]
    ]

    def __init__(self):
        self.width = TetrisApp.BOARD_WIDTH * TetrisApp.TILE_SIZE
        self.height = TetrisApp.BOARD_HEIGHT * TetrisApp.TILE_SIZE
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("TETRIS")

        self.clock = pygame.time.Clock()

        self.board = [[0] * TetrisApp.BOARD_WIDTH for _ in range(TetrisApp.BOARD_HEIGHT)]
        self.current_piece = None
        self.current_piece_colour = None
        self.current_piece_x = 0
        self.current_piece_y = 0
        self.game_over = False


        self.new_piece()


    def new_piece(self):
        self.current_piece = choice(TetrisApp.SHAPES)
        colour_index = randint(1, len(TetrisApp.COlORS) - 1)
        self.current_piece_colour = TetrisApp.COlORS(colour_index)
        self.current_piece_x = TetrisApp.BOARD_WIDTH // 2 - len(self.current_piece[0]) // 2


    def draw_tile(self,x,y,color):
        rect = pygame.rect.Rect((x * self.TILE_SIZE,
                                 y * self.TILE_SIZE,
                                 TetrisApp.TILE_SIZE,
                                 TetrisApp.TILE_SIZE))

        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, (128, 128, 128), rect, 1)

        pygame.display.update()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_tile(0, 0, (0, 0, 255))

        if self.current_piece:
            for _ in self.current_piece:
                for _ in self.current_piece:
                    self.draw_tile(self.current_piece_x,0,self.current_piece_colour,1)
            pygame.display.filp()
    def run(self):
        while not self.game_over:
            self.handle_input()
            self.update()
            self.draw()


def main():
    app = TetrisApp()
    app.run()
    TetrisApp.draw_tile()
    TetrisApp.draw()


if __name__ == '__main__':
    main()
