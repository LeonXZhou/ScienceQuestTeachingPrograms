#By Leon Zhou

import pygame as pygame #import required modules
import random as random
# The below code documents the implementation of text display and buttons.
# it continues from step4 collision detection.
pygame.init()
dimensions = [500,300]
screen = pygame.display.set_mode(dimensions)
backgroundColour = [0,0,0]
green = [0, 255, 0]             # we define some colours here for the text later.
blue = [0, 0, 128]
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


font = pygame.font.SysFont('Arial', 21)                                         # The first thing we have to do is to create a font object
                                                                                # this is done with pygame.font.SysFont(). it takes 2 arguements
                                                                                # font and size.

P1Points = font.render(str(player1Points), True, green, blue)                   # this next part is sorta like creating a text box. font.render() returns
                                                                                # an object that we can draw onto our main display, which we named screen.
                                                                                # it four arguements font.render(text, anti-aliasing, text colour, background colour)
                                                                                # text: a string containing the messages to be displayer. Note I had to convert the integer
                                                                                # points into a string with str()
                                                                                # anti-aliasing: idk what this does but just set it to true :p
                                                                                # text colour: textcolour an array of rgb values
                                                                                # background colour: background colour an array of rgb values
P2Points = font.render(str(player2Points), True, green, blue)
reset = font.render('Reset!', True, green, blue)

pygame.display.flip()

# below is the main game loop.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keysPressed = pygame.key.get_pressed()
    mouseposition = pygame.mouse.get_pos()                                      # returns a 2 element array containing the x and y position of the cursor

    mouseclick = pygame.mouse.get_pressed()                                     # works in the same way as keyboard. returns a 3 element array representing the left mouseclick,
                                                                                # right mouse click, and middle mouse click. [1,0,0] means the left mouse key was pressed. [1,1,1]
                                                                                # means all 3 were pressed.
    #print(mouseposition)                                                       # if you uncomment the print you can see what the coordinates of the screen are by moving your mouse around.
                                                                                # this can be used by campers expierementally to determine x and y pos
    if keysPressed[pygame.K_DOWN] and playerXPosition>0:
        playerYPosition = playerYPosition+.05


    if keysPressed[pygame.K_UP] and playerXPosition<780:
        playerYPosition = playerYPosition-.05
    if keysPressed[pygame.K_w] and playerXPosition<780:
        player2YPosition = player2YPosition-.05

    if keysPressed[pygame.K_s] and playerXPosition<780:
        player2YPosition = player2YPosition+.05

    if ballYPosition <= 0 or ballYPosition > 300:
        ballySpeed = -ballySpeed

    if ballXPosition > 445 and ballXPosition <455:
        if ballYPosition < playerYPosition+height and ballYPosition > playerYPosition:
            ballxSpeed = -ballxSpeed

    if ballXPosition < 55 and ballXPosition >45:
        if ballYPosition < player2YPosition+height and ballYPosition > player2YPosition:
            ballxSpeed = -ballxSpeed

    if mouseposition[0] > 230 and mouseposition[0] <280 and mouseposition[1] >55 and mouseposition[1] < 77: # we check to see if the mouse positions are within rectangle of the reset button
                                                                                                            # the coordinates were found expierementally using print(mouseposition).
                                                                                                            # mouseposition[0] is the first element of the 2 element array and the x pos
                                                                                                            # mouseposition[1] is the second element of the 2 element array and the y pos.
                                                                                                            # most programing languages start counting from 0 (excpet like matlab cuz its a dumb)
        reset = font.render('Reset!', True, blue, green)                                                    # if the mouse is within the button we invert the colour to give it a button like animation
                                                                                                            # we then check if the left mouse was clicked. If so we reset the ball
        if mouseclick[0]:
            ballXPosition =245
            ballYPosition = 145
            ballxSpeed = random.choice((-1,1))*random.randint(1,6)/200
            ballySpeed = random.choice((-1,1))*random.randint(1,6)/200
            player1Points = 0
            player2Points = 0

    else:
        reset = font.render('Reset!', True, green, blue)

    if ballXPosition < 0:
        player2Points = player2Points + 1
        ballXPosition =245
        ballYPosition = 145
        ballxSpeed = random.randint(-5,6)/200
        ballySpeed = random.randint(-5,6)/200
    if ballXPosition > 500:
        player1Points = player1Points + 1
        ballXPosition =245
        ballYPosition = 145
        ballxSpeed = random.randint(-5,6)/200
        ballySpeed = random.randint(-5,6)/200





    ballXPosition = ballXPosition+ballxSpeed
    ballYPosition = ballYPosition+ballySpeed


    rectanglePlayer = pygame.Rect(playerXPosition,playerYPosition,width,height)
    rectanglePlayer2 = pygame.Rect(player2XPosition, player2YPosition, width, height)

    P1Points = font.render(str(player1Points), True, green, blue)

    P2Points = font.render(str(player2Points), True, green, blue)

    screen.fill(backgroundColour)
    pygame.draw.rect(screen,rectanglePlayerColour,rectanglePlayer)
    pygame.draw.rect(screen,rectanglePlayerColour,rectanglePlayer2)
    pygame.draw.circle(screen,ballColour,(int(ballXPosition),int(ballYPosition)),ballRadius)

    screen.blit(P1Points,(50, 50))                                              # here we use the blit function to draw our points on the screen
    screen.blit(P2Points,(450, 50))

    screen.blit(reset,(225,50))

    pygame.display.flip()
