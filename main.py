from pygame import *
from random import *
windov = display.set_mode((700, 500))
display.set_caption('Игра про тарелки и ракету')
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


class Player(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
     

    def update(self):
    keys= pygame.key.get_pressed()
    if keys[K_s]


   



finish = False
while game:
    if finish != True:
        
        text3 = font4. render('ТЫ ВЫИГРАЛ ;)', 1, (234, 255, 0))
        text4 = font5. render('ТЫ ПРОИГРАЛ :(', 1, (234, 255, 0))
     
      
        for e in event.get():  
            if e.type ==QUIT:
                game = False
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    raceta.fier()


    display.update()
    clock.tick(50)

