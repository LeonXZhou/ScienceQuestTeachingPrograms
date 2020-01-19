#By Leon Zhou
import pygame as pygame #import required modules

# Here we implement the projectiles by extending the sprite class.
# We continue from the creatingImageNonObjectPlayer.py code so some comments are omitted.


class projectile(pygame.sprite.Sprite):
    # Attributes. Every object has attributes that describe it. For example, a dog
    # could have the attributes of colour/fur length/allergenic. In the case of The
    # projectile it has a xpos, ypos, colour, xsize, ysize.These attributes are unique
    # to each projectile instance
    xpos = 0
    ypos = 0
    xsize = 4
    ysize = 10
    projectileColour = [125,0,0]
    # Here we override the default initialization function. This function is called
    # every time we want to create a projectile object. This means we are
    # assigning attributes here. Since we extended the sprite
    # class, there are several default attibutes we need to asign.
    # Note the use of self.var to access the objects internal attributes.
    def __init__(self,startingX,startingY):
        # The first line basically fills in all the attributes of a Sprite to
        # their default value.
        pygame.sprite.Sprite.__init__(self)
        # the next two lines sets the image of the sprite. In this case it is just a rectangle
        self.image = pygame.Surface((self.xsize,self.ysize)) # we use the surface class to make the rectangle
                                                             # it accepts an array (width,length) self.image
                                                             # is now set to a surface
        self.image.fill(self.projectileColour)               # since we set self.image to a surface we can call the fill command
                                                             # the fill command accepts a colour array.
        # the next two lines is setting up an invisible rectangle that outlines the space on the screen the sprite occupies.
        # this will be used for collision detection.
        self.rect = pygame.Rect(self.xpos,self.ypos,self.xsize,self.ysize) # creates a rectangle object
        self.rect.center = (startingX, startingY)                          # sets the position of the rectangle

        #setting the positions to their starting values
        self.xpos = startingX
        self.ypos = startingY

    # we overwrite the default update function. We are going to call this functions
    # with every iteration of the main game loop. Basically this determines the behavior
    # of the class. For the projectile class it just means moving up (changing the y position)
    def update(self):
        self.ypos = self.ypos - 0.11 # update ypos
        self.rect.center = (self.xpos,self.ypos) #update center of rectangle to be at the new ypos



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

pygame.display.flip()



projectileList = pygame.sprite.Group()      # sprite.Group is a data structure than can hold multiple sprites.
                                            # here it will at as a collection of all projectile sprites so
                                            # we can easily keep track of them and iterate through them.
                                            # projectileList is now a Group object

ProjectileCoolDown = 0
while running:

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

    if keysPressed[pygame.K_SPACE] and not ProjectileCoolDown:                  # Remember 0 = false and any other number is true. Since we only want the projectile to fire
                                                                                # when the ProjectileCoolDown is 0 we use the not key word to invert the logic.
        ProjectileCoolDown = 2000                                               # since we fired the projectile we set the cooldown back to 2000
        newProjectile = projectile(playerXPosition+10,playerYPosition-10)       # we initiate a new projectile at the center of the player.
        projectileList.add(newProjectile)                                       # we then append (add at the end) the newProjectile to our projectile list.


    rectanglePlayer = pygame.Rect(playerXPosition,playerYPosition,20,20)
    screen.fill(backgroundColour)

    projectileList.update()                                                     # the Group object (remember projectileList is a group object) has a update function that will updates
                                                                                # all the sprites stored in it.

    for sprite in projectileList:                                               # this forloop cycles through all the projectiles. in each iteration sprite is a pointer to an element
                                                                                # in projectile list.
        if sprite.ypos < -20:                                                   # if the projectile is off the screen we remove the sprite from our list of projectiles
            projectileList.remove(sprite)

    projectileList.draw(screen)
    screen.blit(playerImage,[playerXPosition,playerYPosition])
    pygame.display.flip()
