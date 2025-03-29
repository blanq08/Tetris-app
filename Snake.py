import pygame
import random

pygame.init()

# Constant
SCREEN_SIZE = [1000, 1000]
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SNAKE_COLOR = (24, 242, 176)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
CLOCK = pygame.time.Clock()
SQUARE_SIZE = 50
APPLE_SIZE = (SQUARE_SIZE, SQUARE_SIZE)
FONT = pygame.font.SysFont('Arial', 25)
BLACK = (0, 0, 0)

KEY_DIRECTION = {
    pygame.K_UP: "UP",
    pygame.K_DOWN: "DOWN",
    pygame.K_LEFT: "LEFT",
    pygame.K_RIGHT: 'RIGHT'
}

# 블록 그리기 함수
def draw_block(color, position):
    """화면에 사각형 블록을 그리는 함수"""
    block = pygame.Rect((position[1] * SQUARE_SIZE, position[0] * SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.rect(SCREEN, color, block)

class Snake:
    # 뱀의 위치와 방향 관리 방법
    # 이동 메커니즘
    # 성장 메커니즘
    def __init__(self):
        self.positions = [(0, 2), (0, 1), (0, 0)]  # 뱀의 위치!
        self.direction = ''

    def draw(self):
        # pygame.draw.rect(surface=SCREEN, color=SNAKE_COLOR, rect=(0, 0, *SNAKE_SIZE))
        # pygame.draw.rect()
        for position in self.positions:
            draw_block(SNAKE_COLOR, position)

    def move(self):
        head_x, head_y = self.positions[0]

        if not self.direction: return
        elif self.direction == "UP":
            new_head = (head_x - 1, head_y)
        elif self.direction == "DOWN":
            new_head = (head_x + 1, head_y)
        elif self.direction == "LEFT":
            new_head = (head_x, head_y - 1)
        elif self.direction == "RIGHT":
            new_head = (head_x, head_y + 1)

        self.positions.insert(0, new_head)
        self.positions.pop()

    def grow(self):
        tail_position = self.positions[-1]
        self.positions.append(tail_position)

    def check_collision_with_wall(self):
        head_x, head_y = self.positions[0]
        max_x = SCREEN_SIZE[0] // SQUARE_SIZE
        max_y = SCREEN_SIZE[1] // SQUARE_SIZE
        return head_x < 0 or head_y < 0 or head_x >= max_x or head_y >= max_y

    def check_collision_with_self(self):
        return self.positions[0] in self.positions[1:]

class Apple:
    def __init__(self):
        x_pos = SCREEN_SIZE[0] // SQUARE_SIZE
        y_pos = SCREEN_SIZE[1] // SQUARE_SIZE
        self.position = (random.randint(0, x_pos - 1), random.randint(0, y_pos - 1))
        self.direction = ''

    def draw(self):
        draw_block(RED, self.position)

    def move(self):
        if not self.direction:
            return

        x, y = self.position

        if self.direction == "UP":
            self.position = (x, y - 1)
        elif self.direction == "DOWN":
            self.position = (x, y + 1)
        elif self.direction == "LEFT":
            self.position = (x - 1, y)
        elif self.direction == "RIGHT":
            self.position = (x + 1, y)

    def respawn(self, snake_positions):
        max_x = SCREEN_SIZE[0] // SQUARE_SIZE - 1
        max_y = SCREEN_SIZE[1] // SQUARE_SIZE - 1

        # 뱀의 위치와 겹치지 않는 새 위치 찾기
        new_position = (random.randint(0, max_y), random.randint(0, max_x))
        while new_position in snake_positions:
            new_position = (random.randint(0, max_y), random.randint(0, max_x))

        self.position = new_position

def show_score(score):
    score_text = FONT.render(f'Score: {score}', True, BLACK)
    SCREEN.blit(score_text, [10, 10])

done = False
apple = Apple()
snake = Snake()
score = 0
while not done:
    SCREEN.fill(color=WHITE)
    apple.draw()
    snake.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창 닫기 버튼을 클릭하면
            done = True
        if event.type == pygame.KEYDOWN and event.key in KEY_DIRECTION:
            # 반대 방향으로 이동 방지 (예: 오른쪽 이동 중 왼쪽 키 입력 시 무시)
            snake.direction = KEY_DIRECTION[event.key]
            print(apple.direction)
    if snake.positions[0] == apple.position:
        score += 1
        snake.grow()
        apple.respawn(snake.positions)
        print(score)
        print(snake.positions)

    if snake.check_collision_with_wall() or snake.check_collision_with_self():
        done = True

    snake.move()
    show_score(score)

    pygame.display.update()
    CLOCK.tick(5)


pygame.quit()