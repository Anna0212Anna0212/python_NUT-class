import pygame
import sys
import random
import os

# 初始化 Pygame
pygame.init()

# 自動設置工作目錄為程式所在目錄
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# 設定視窗尺寸
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 設定視窗標題
pygame.display.set_caption('Flappy Bird')

# 加載並調整圖像大小
background = pygame.transform.scale(pygame.image.load('img/background-day.png'), (screen_width, screen_height))
bird_image = pygame.transform.scale(pygame.image.load('img/bluebird-downflap.png'), (34, 24))
pipe_image = pygame.transform.scale(pygame.image.load('img/pipe-green.png'), (52, 320))

# 設定遊戲時鐘
clock = pygame.time.Clock()
fps = 30

# 顏色
WHITE = (255, 255, 255)

# 字體
font = pygame.font.SysFont(None, 48)

# 小鳥類別
class Bird:
    def __init__(self):
        self.image = bird_image
        self.rect = self.image.get_rect(center=(50, screen_height // 2))
        self.gravity = 0.25
        self.movement = 0
        self.jump_strength = -6

    def update(self):
        self.movement += self.gravity
        self.rect.y += self.movement

    def jump(self):
        self.movement = self.jump_strength

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# 管道類別
class Pipe:
    def __init__(self):
        self.image = pipe_image
        self.rect_top = self.image.get_rect(midbottom=(screen_width + 100, random.randint(150, 400)))
        self.rect_bottom = self.image.get_rect(midtop=(screen_width + 100, self.rect_top.bottom + 150))
        self.passed = False

    def update(self):
        self.rect_top.x -= 5
        self.rect_bottom.x -= 5

    def draw(self, screen):
        screen.blit(self.image, self.rect_top)
        screen.blit(pygame.transform.flip(self.image, False, True), self.rect_bottom)

# 主遊戲函數
def main_game():
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            # 使用 MOUSEBUTTONDOWN 檢測滑鼠點擊（或觸控）
            if event.type == pygame.MOUSEBUTTONDOWN:
                bird.jump() if not game_over else main_game()

        if not game_over:
            bird.update()
            for pipe in pipes:
                pipe.update()
                if pipe.rect_top.right < 0:
                    pipes.remove(pipe)
                if pipe.rect_top.right < bird.rect.left and not pipe.passed:
                    pipe.passed = True
                    score += 1

            if pipes[-1].rect_top.centerx < screen_width // 2:
                pipes.append(Pipe())

            # 碰撞檢測
            for pipe in pipes:
                if bird.rect.colliderect(pipe.rect_top) or bird.rect.colliderect(pipe.rect_bottom):
                    game_over = True

            if bird.rect.top <= 0 or bird.rect.bottom >= screen_height:
                game_over = True

        # 繪製畫面
        screen.blit(background, (0, 0))
        for pipe in pipes:
            pipe.draw(screen)
        bird.draw(screen)

        # 顯示分數
        score_surface = font.render(str(score), True, WHITE)
        score_rect = score_surface.get_rect(center=(screen_width // 2, 50))
        screen.blit(score_surface, score_rect)

        pygame.display.update()
        clock.tick(fps)

# 遊戲入口
if __name__ == '__main__':
    while True:
        main_game()


