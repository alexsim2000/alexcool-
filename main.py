from pygame import *
from random import *
windov = display.set_mode((700, 500))
display.set_caption('')
backgroud = transform.scale(image.load('Remove-bg.ai_1712763450316.png'), (700, 500))
game = True
clock = time.Clock()
font.init()
font2 = font.SysFont('Arial', 36)
font3 = font.SysFont('Arial', 36)
font4 = font.SysFont('Arial', 100)
font5= font.SysFont('Arial', 100)
score = 0
lost = 0


class Player(sprite.Sprite):
    def __init__(self, color, speed , x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((50, 150))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
     

    def update(self):
        keys= key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -=self.speed
        if keys[K_s] and self.rect.y < 450:
            self.rect.y +=self.speed


    def update2(self):
        keys= key.get_pressed()
        if keys[K_UP]:
            self.rect.y -=self.speed
        if keys[K_DOWN]:
            self.rect.y +=self.speed


class Ball(sprite.Sprite):
    def __init__(self, color, speed_x ,speed_y, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        ball.rect.x += ball.speed_x
        ball.rect.y += ball.speed_y

        if ball.rect.y > 500-50 or ball.rect.y < 0:
            ball.speed_y *= -1


ball = Ball((225, 225, 225), 2, 2, 300, 320)   
player1= Player((225, 225, 225), 20, 20, 20)
player2= Player((225, 225, 225), 20, 600, 20)


finish = False
while game:
    if finish != True:
        




        player2.update2()
        player1.update()
        windov.blit(backgroud, (0, 0))
        windov.blit(ball.image, (ball.rect.x, ball.rect.y))
        windov.blit(player1.image, (player1.rect.x, player1.rect.y))
        windov.blit(player2.image, (player2.rect.x, player2.rect.y))
        
        ball.update()


        if sprite.collide_rect(player2, ball) or sprite.collide_rect(player1, ball):
            ball.speed_x*=-1
            
  
     
      
        for e in event.get():  
            if e.type ==QUIT:
                game = False

    display.update()
    clock.tick(50)

