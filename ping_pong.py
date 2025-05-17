'''импорт библиотек'''
from pygame import *


'''создание классов'''
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_x_scale, player_y_scale):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_x_scale, player_y_scale))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        
        if keys_pressed[K_s] and self.rect.y < 630:
            self.rect.y += 10

    def update_2(self):
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 10
        
        if keys_pressed[K_DOWN] and self.rect.y < 630:
            self.rect.y += 10

class Ball(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, speed_x, speed_y, player_x_scale, player_y_scale):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_x_scale, player_y_scale))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y * -1

        if self.rect.y > 450:
            self.speed_y = self.speed_y * -1

        if self.rect.y < 0:
            self.speed_y = self.speed_y * -1
        


'''создание окна'''
window = display.set_mode((700, 500))
display.set_caption("Ping pong")


'''создание спрайтов игроков, мяча и фона'''
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
p1 = Player("p.png", 10, 250, 10, 10, 200)
p2 = Player("p.png", 680, 250, 10, 10, 200)
ball = Ball("ball.png", 325, 225, 3, 3, 50, 50)


'''объявление переменных и флажков'''
FPS = 60
run = True
finish = False
clock = time.Clock()

font.init()
font1 = font.SysFont('Arial', 36)

'''создание игрового цикла'''
while run:
    if finish != True:
        window.blit(background, (0, 0))
        keys_pressed = key.get_pressed()

        p1.reset()
        p1.update_1()

        p2.reset()
        p2.update_2()

        ball.reset()
        ball.update()

        text_p1_win = font1.render("Игрок 1 выиграл!", 1, (180, 0, 0))
        text_p2_win = font1.render("Игрок 2 выиграл!", 1, (180, 0, 0))
    
    if sprite.collide_rect(ball, p1) or sprite.collide_rect(ball, p2):
        ball.speed_x = ball.speed_x * -1

    if ball.rect.x < 0:
        window.blit(text_p2_win, (250, 250))
        finish = True

    if ball.rect.x > 700:
        window.blit(text_p1_win, (250, 250))
        finish = True

    for e in event.get():
        if e.type == QUIT:
            run = False

    
    display.update()
    clock.tick(FPS)