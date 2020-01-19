#By Leon Zhou
import pygame as pygame #import required modules
import random as random
# The below code shows how to add a player as just a shape without
# using objects. We build on step3AddingaBall.

dimensions = [500,300]
screen = pygame.display.set_mode(dimensions)
backgroundColour = [0,0,0]
screen.fill(backgroundColour)
running = True


playerXPosition = 450
playerYPosition = 125
player2XPosition = 40
player2YPosition = 125
player1Points = 0
player2Points = 0
width = 10
height = 50

ballXPosition =245
ballYPosition = 145
ballRadius = 5
ballxSpeed = random.choice((-1,1))*random.randint(1,6)/200
ballySpeed = random.choice((-1,1))*random.randint(1,6)/200


rectanglePlayer = pygame.Rect(playerXPosition,playerYPosition,width,height)

rectanglePlayer2 = pygame.Rect(player2XPosition, player2YPosition , width, height)

rectanglePlayerColour = [150,23,10]
ballColour = [250,250,250]

pygame.draw.rect(screen,rectanglePlayerColour,rectanglePlayer)
pygame.draw.circle(screen,ballColour,(ballXPosition,ballYPosition),ballRadius)



pygame.display.flip()

# below is the main game loop.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keysPressed = pygame.key.get_pressed()
    if keysPressed[pygame.K_DOWN] and playerXPosition>0:
        playerYPosition = playerYPosition+.05

    if keysPressed[pygame.K_UP] and playerXPosition<780:
        playerYPosition = playerYPosition-.05
    if keysPressed[pygame.K_w] and playerXPosition<780:
        player2YPosition = player2YPosition-.05

    if keysPressed[pygame.K_s] and playerXPosition<780:
        player2YPosition = player2YPosition+.05




    if ballYPosition <= 0 or ballYPosition > 300:                                           # First collsion detection. This checks if either the ball is at the top or bottom of the screen.
                                                                                            # If it is we make reverse it's y direction(this can be done by putting a negative sign infront)
                                                                                            # y=1 -> -y = -1 and y = -1 -> -y = 1
        ballySpeed = -ballySpeed

    if ballXPosition > playerXPosition and ballXPosition < playerXPosition+width:           # these next two collision detections check if the ball has hit the paddle. The first one is for
                                                                                            # player 1 and the second one is for player 2.
                                                                                            # The first if statment checks if the ball is in the x position range of the paddle.
                                                                                            # the second if statement checks if the ball is in the y position rang of the paddle
        if ballYPosition < playerYPosition+height and ballYPosition > playerYPosition:
            ballxSpeed = -ballxSpeed

    if ballXPosition > player2XPosition and ballXPosition < player2XPosition +width:
        if ballYPosition < player2YPosition+height and ballYPosition > player2YPosition:
            ballxSpeed = -ballxSpeed


    if ballXPosition < 0:
        player2Points = player2Points + 1
        ballXPosition =245
        ballYPosition = 145
        ballxSpeed = random.randint(-5,6)/200
        ballySpeed = random.randint(-5,6)/200
    if ballXPosition > 500:
        player1Points = player1Points + 1
        player2Points = player2Points + 1
        ballXPosition =245
        ballYPosition = 145
        ballxSpeed = random.randint(-5,6)/200
        ballySpeed = random.randint(-5,6)/200

    ballXPosition = ballXPosition+ballxSpeed                                    # Update ball position
    ballYPosition = ballYPosition+ballySpeed


    rectanglePlayer = pygame.Rect(playerXPosition,playerYPosition,width,height)
    rectanglePlayer2 = pygame.Rect(player2XPosition, player2YPosition, width, height)

    #in the below section we animate our game.
    screen.fill(backgroundColour)                                               # Since our shape moved the first thing we do is clear the screen
    pygame.draw.rect(screen,rectanglePlayerColour,rectanglePlayer)              # we draw the player onto screen in its new position
    pygame.draw.rect(screen,rectanglePlayerColour,rectanglePlayer2)
    pygame.draw.circle(screen,ballColour,(int(ballXPosition),int(ballYPosition)),ballRadius)
    pygame.display.flip()                                                       # we use the flip() command to display the entire window again
