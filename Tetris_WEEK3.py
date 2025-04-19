import pygame
from random import choice, randint
import sys


# Initialize pygame
pygame.init()




class TetrisApp:
    TILE_SIZE = 30
    BOARD_WIDTH = 10
    BOARD_HEIGHT = 20

    COLORS = [
        (0, 0, 0),       # 검은색 (빈 공간)
        (255, 255, 255), # 흰색
        (0, 0, 255),     # 파란색
        (255, 165, 0),   # 주황색
        (0, 255, 255),   # 청록색
        (255, 0, 255),   # 마젠타
        (255, 0, 0),     # 빨간색
        (0, 255, 0),     # 녹색
        (255, 255, 0)    # 노란색
    ]

    SHAPES = [
        [[1, 1, 1, 1]], # I
        [[1, 1, 1],     # T
         [0, 1, 0]],
        [[0, 1, 1],     # S
         [1, 1, 0]],
        [[1, 1, 0], # Z
         [0, 1, 1]],
        [[1, 1], # ㅁ
         [1, 1]],
        [[1, 1, 1],
         [1, 0, 0]],
        [[1, 1, 1],
         [0, 0, 1]]
    ]

    def __init__(self):
        # Set up display
        self.width = TetrisApp.TILE_SIZE * TetrisApp.BOARD_WIDTH
        self.height = TetrisApp.TILE_SIZE * TetrisApp.BOARD_HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Tetris')

        # Set up the clock for controlling game speed
        self.clock = pygame.time.Clock()

        # Game state
        self.board = [[0] * TetrisApp.BOARD_WIDTH for _ in range(TetrisApp.BOARD_HEIGHT)]
        self.current_piece = None
        self.current_piece_color = None
        self.current_piece_x = 0
        self.current_piece_y = 0
        self.game_over = False
        
        self.drop_time = pygame.time.get_ticks()
        self.drop_speed= 500

        self.new_piece()

    def check_collision(self, new_x, new_y, piece):
        for y, row in enumerate(piece):
            for x, cell in enumerate(row):
                if cell == 1:
                    real_x = new_x + x
                    real_y = new_y + y
                    if (
                            new_x < 0 or
                            real_x >= TetrisApp.BOARD_WIDTH or
                            real_y >= TetrisApp.BOARD_HEIGHT or
                            self.board[real_y][real_x] != 0
                    ):

                        return True
        return False

    def move(self, dx, dy):
        """Move the current piece if possible."""
        new_x = self.current_piece_x + dx
        new_y = self.current_piece_y + dy

        if not self.check_collision(new_x, new_y, self.current_piece):
            self.current_piece_x = new_x
            self.current_piece_y = new_y
            return True
        return False


    def new_piece(self):
        self.current_piece = choice(TetrisApp.SHAPES)
        color_index = randint(1, len(TetrisApp.COLORS) - 1)
        self.current_piece_color = TetrisApp.COLORS[color_index]
        self.current_piece_x = TetrisApp.BOARD_WIDTH // 2 - len(self.current_piece[0]) // 2
        self.current_piece_y = 0

    def freeze_piece(self):
        for y, row in enumerate(self.current_piece):
            for x,cell in enumerate(row):
                if cell:
                    self.board[self.current_piece_y + y][self.current_piece_x + x] = \
                        TetrisApp.COLORS.index(self.current_piece_color)
        self.clear_lines()
        self.new_piece()

    def clear_lines(self):
        new_board = []

        for row in self.board:
            if 0 in row:
                new_board.append(row)
        lines_cleared = len(self.board) - len(new_board)

        for _ in range(lines_cleared):
            new_board.insert(0, [0] * len(self.board[0]))
        self.board = new_board

    def rotate(self):
        new_piece = [list(row) for row in zip(*self.current_piece)][::-1]
        if not self.check_collision(self.current_piece_x, self.current_piece_y, new_piece):
            self.current_piece = new_piece

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.rotate()
                elif event.key == pygame.K_LEFT:
                    self.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    self.move(0, 1)
                elif event.key == pygame.K_SPACE:
                    while self.move(0, 1):
                        pass


    def update(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.drop_time > self.drop_speed:
            if not self.move(0,1):
                self.freeze_piece()
            self.drop_time = current_time


    def draw_tile(self, x, y, color):
        rect = pygame.rect.Rect(
            (x * TetrisApp.TILE_SIZE,
             y * TetrisApp.TILE_SIZE,
             TetrisApp.TILE_SIZE,
             TetrisApp.TILE_SIZE)
        )

        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, (128, 128, 128), rect, 1)


    def draw(self):
        self.screen.fill((0,0,0))

        for y, row in enumerate(self.board):
            for x,cell in enumerate(row):
                if cell:
                    color = TetrisApp.COLORS[cell]
                    self.draw_tile(x, y,color)

        # 현재 블록 그리기
        if self.current_piece:
            for y, row in enumerate(self.current_piece):
                for x, cell in enumerate(row):
                    if cell:
                        self.draw_tile(self.current_piece_x + x, self.current_piece_y + y,
                                       self.current_piece_color)

        # 디스플레이 업데이트 - 한 번만 호출하는 것이 효율적
        pygame.display.flip()


    def run(self):
        while not self.game_over:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(60) # limit to 60 Frame Per Second (FPS)

def main():
    app = TetrisApp()
    app.run()

if __name__ == '__main__':
    main()