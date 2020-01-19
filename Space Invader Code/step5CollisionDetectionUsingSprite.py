import pygame as pygame #import required modules

# Here we implement the colission detection for aliens. 

class aliens(pygame.sprite.Sprite):
    xpos = 0
    ypos = 0
    xsize = 30
    ysize = 30
    horizontaldirection = 1
    def __init__(self,startingX,startingY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('alienboi.png')
        self.image = pygame.transform.scale(self.image, [self.xsize,self.ysize])
        self.rect = pygame.Rect(self.xpos,self.ypos,self.xsize,self.ysize)
        self.rect.center = (startingX, startingY)
        self.xpos = startingX
        self.ypos = startingY

    def update(self,horizontalMovement,verticalMovement):
        self.xpos = self.xpos + self.horizontaldirection * horizontalMovement
        self.ypos = self.ypos + verticalMovement
        self.rect.center = (self.xpos,self.ypos)

class projectile(pygame.sprite.Sprite):
    xpos = 0
    ypos = 0
    xsize = 4
    ysize = 10
    projectileColour = [125,0,0]

    def __init__(self,startingX,startingY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.xsize,self.ysize))
        self.image.fill(self.projectileColour)
        self.rect = pygame.Rect(self.xpos,self.ypos,self.xsize,self.ysize)
        self.rect.center = (startingX, startingY)
        self.xpos = startingX
        self.ypos = startingY
    def update(self):
        self.ypos = self.ypos - 0.11
        self.rect.center = (self.xpos,self.ypos)



dimensions = [800,400]
screen = pygame.display.set_mode(dimensions)
backgroundColour = [0,0,0]
screen.fill(backgroundColour)
running = True
playerXPosition = 390
playerYPosition = 380
rectanglePlayer = pygame.Rect(playerXPosition,playerYPosition,20,20)
playerImage = pygame.image.load('SpaceDefender.png')
playerImage = pygame.transform.scale(playerImage, [20, 20])
screen.blit(playerImage,[playerXPosition,playerYPosition])




projectileList = pygame.sprite.Group()
alienList = pygame.sprite.Group()

for i in range(5):
    newAlien = aliens(40*i+15,40)
    screen.blit(newAlien.image,[30,30])
    alienList.add(newAlien)

alienList.draw(screen)
ProjectileCoolDown = 0
pygame.display.flip()
alienDownCounter = 10000;
while running:
    if alienDownCounter > 0:
        alienDownCounter = alienDownCounter -1

    if ProjectileCoolDown > 0:
        ProjectileCoolDown = ProjectileCoolDown - 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keysPressed = pygame.key.get_pressed()
    if keysPressed[pygame.K_LEFT] and playerXPosition>0:
        playerXPosition = playerXPosition-.05

    if keysPressed[pygame.K_RIGHT] and playerXPosition<780:
        playerXPosition = playerXPosition+.05

    if keysPressed[pygame.K_SPACE] and not ProjectileCoolDown:
        ProjectileCoolDown = 2000
        newProjectile = projectile(playerXPosition+10,playerYPosition-10)
        projectileList.add(newProjectile)

    rectanglePlayer = pygame.Rect(playerXPosition,playerYPosition,20,20)
    screen.fill(backgroundColour)
    projectileList.update()
    for sprite in alienList:
        if sprite.xpos > 800:
            for alien in alienList:
                alien.horizontaldirection = -1;
            break;
        elif sprite.xpos < 0:
            for alien in alienList:
                alien.horizontaldirection = 1;
            break;
    if alienDownCounter:
        alienList.update(.1,0)
    else:
        alienList.update(.1,40)
        alienDownCounter = 10000

    collide = pygame.sprite.groupcollide(projectileList, alienList, True, True, collided = None)
    projectileList.draw(screen)
    screen.blit(playerImage,[playerXPosition,playerYPosition])
    alienList.draw(screen)
    pygame.display.flip()
