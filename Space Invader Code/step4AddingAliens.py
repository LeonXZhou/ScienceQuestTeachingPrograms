#By Leon Zhou
import pygame as pygame #import required modules

# Here we are implementing aliens. We continue from addingOProjectileSprite.py

class aliens(pygame.sprite.Sprite):
    # Here are the attributes of an alien objects (position, size, and direction).
    xpos = 0
    ypos = 0
    xsize = 30
    ysize = 30
    horizontaldirection = 1 # 1 means the the aliens will move right and -1 means it will move left

    # Here we override the default initialization function. This function is called
    # every time we want to create an alien object. This means we are
    # assigning attributes here. Since we extended the sprite
    # class, there are several default attibutes we need to asign.
    def __init__(self,startingX,startingY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('alienboi.png')
        self.image = pygame.transform.scale(self.image, [self.xsize,self.ysize])
        self.rect = pygame.Rect(self.xpos,self.ypos,self.xsize,self.ysize)
        self.rect.center = (startingX, startingY)
        self.xpos = startingX
        self.ypos = startingY

    def update(self,horizontalMovement,verticalMovement):
        # The update function is called with each iteration of the while loop.
        # The amount of movment is determined by the inputs
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




projectileList = pygame.sprite.Group()   # list to keep track of all projectiles
alienList = pygame.sprite.Group()        # list to keep track of all aliens. # good to have a list keeping track of all sprites.
                                         # convienient to also maybe have an all sprites

for i in range(0,5):                       # we use a for loop to initiate 5 aliens.
    newAlien = aliens(40*i+15,40)        # note how we change the starting x position depending on what i is that way the alines are next to each other
    screen.blit(newAlien.image,[30,30])  # we draw the alien here
    alienList.add(newAlien)              # we add the alien to the list

ProjectileCoolDown = 0
pygame.display.flip()
alienDownCounter = 10000                # we initiate a counter to keep track of when the aliends should move down.
while running:

    if alienDownCounter > 0:
        alienDownCounter = alienDownCounter -1 # tick down alien down counter.

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


    for sprite in alienList:                                                    # This for loop checks if any of the aliens position areat the left/right boundaries
        if sprite.xpos > 800:
            for alien in alienList:
                alien.horizontaldirection = -1;                                 # if one of them is we change the direction of all the aliens. then stop checking the rest of the list
                                                                                # we have to do this because the alien list is not ordered
            break;
        elif sprite.xpos < 0:
            for alien in alienList:
                alien.horizontaldirection = 1;
            break;

    if alienDownCounter:
        alienList.update(.1,0)                                                  # if the aliendowncounter is non zero we just move the alien horizontally.
    else:
        alienList.update(.1,40)                                                 # if the aliendowncounter is 0 we move the alien down and reset the counter
        alienDownCounter = 10000

    projectileList.draw(screen)
    screen.blit(playerImage,[playerXPosition,playerYPosition])
    alienList.draw(screen)
    pygame.display.flip()
