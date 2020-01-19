import pygame as pygame #import required modules

# Here we add a projectile that will launch from the defender if the space key is pressed.
# We continue from the creatingImageNonObjectPlayer.py code so some comments are omitted.
# we will be using classes and arrays

# Here we create a projectile class. You can imagine this as a template that
# describes all the features of a projectile.
class projectile:
# Attributes. Every object has attributes that describe it. For example, a dog
# could have the attributes of colour/fur length/allergenic. In the case of The
# projectile it has a xpos, ypos, colour, xsize, ysize.These attributes are unique
# to each projectile instance
    xpos = 0
    ypos = 0
    xsize = 4
    ysize = 10
    projectileColour = [125,0,0]
# below we define the methods/functions of the class. These are like the actions
# this object can perform. For example a dog could have a functions such as jump,
# run, or sleep. In the case of a bullet we have 2.

# This first function is the initialization function. So when we create a new projectile
# this is the function used. The creation method will require the x, y position the
# projectile should be created at.
    def __init__(self,x,y):
        self.xpos = x       # we use the self key word to access the attributes of
        self.ypos = y       # the specific instance of projectile that called this fucntion

# This second function is the draw function. This function will be called at the end the game loop
# where all images are updated. Since the projectile will always be moving up we can just updates
# the y pos at every draw. We use the same method in creating the rectangle player to draw a rectangle bullet
    def draw(self,surface):
        self.ypos = self.ypos - 0.1
        rectangleProjectile = pygame.Rect(self.xpos,self.ypos,self.xsize,self.ysize)
        pygame.draw.rect(surface,self.projectileColour,rectangleProjectile)


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

ProjectileList = []                                                             # A list to keep track of all the projectiles
ProjectileCoolDown = 0                                                          # A counter to prevent the player from spamming bullets

while running:

    if ProjectileCoolDown > 0:                                                  # reduce cool down by 1 unless it is already 0
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
        newProjectile = projectile(playerXPosition+9,playerYPosition+10)        # we initiate a new projectile at the center of the player.
        ProjectileList.append(newProjectile)                                    # we then append (add at the end) the newProjectile to our projectile list.


    rectanglePlayer = pygame.Rect(playerXPosition,playerYPosition,20,20)
    screen.fill(backgroundColour)

    # use a for loop to cycle through ProjectileList. Each p is an instance of a projectile.
    for p in ProjectileList:
        if p.ypos < -20:                                                        # Here we check if a bullet has reached the edge of the screen.
            ProjectileList.pop(0)                                               # If one has we know it is the first bullet that has so we pop (remove) the first bullet in the list
        else:
            p.draw(screen)                                                      # If no projectile has reached the edge we simply redraw all the projectiles
    print(len(ProjectileList))
    screen.blit(playerImage,[playerXPosition,playerYPosition])
    pygame.display.flip()
