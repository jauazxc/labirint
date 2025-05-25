from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

x2, y2 = (275,30)
x1, y1 = (450,150)
x3, y3 = (575, 350)
win_width = 700
win_height = 500

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and x2 >= 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and x2 <= 600:
            self.rect.x += self.speed
        if keys_pressed[K_w] and y2 >= 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and y2 <= 400:
            self.rect.y  += self.speed


class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= 615:
            self.direction = 'left'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed   

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height, ):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((win_width, win_height))
display.set_caption('qeqoqeq')
background = transform.scale(image.load('background.jpg'), (700, 500))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

player = Player('hero.png', 275, 30, 5)
monster = Enemy('cyborg.png', 450, 150, 2)
treasure = GameSprite('treasure.png', 575, 350, 0)

wall1 = Wall(154, 205, 50, 100, 20, 450, 10)
wall2 = Wall(154, 205, 50, 500, 280, 350, 10)
wall3 = Wall(154, 205, 50, 300, 120, 10, 100)

game = True
finish = False
clock = time.Clock()

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 255, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))

        player.reset()
        monster.reset()
        treasure.reset()

        player.update()
        monster.update()

        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()

        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, monster):
            finish = True
            window.blit(lose, (200, 200))
            

        if sprite.collide_rect(player, treasure):
            finish = True
            window.blit(win, (200, 200))
         

    
    display.update()
    clock.tick(60)  