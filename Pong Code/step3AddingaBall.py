#By Leon Zhou
import pygame as pygame #import required modules
import random as random # note we imported random not just pygame.
# The below code shows how to add a player as just a shape without
#using objects. We build on the CreatingRectangleNonObjectPlayers.py example.
# Explanation for window code is omitted

dimensions = [500,300]
screen = pygame.display.set_mode(dimensions)
backgroundColour = [0,0,0]
screen.fill(backgroundColour)
running = True


playerXPosition = 450
playerYPosition = 125
player2XPosition = 40
player2YPosition = 125
width = 10
height = 50

ballXPosition =245                                                              #Here we initiate the properties of the ball. its position, radius, and speed.
ballYPosition = 145
ballRadius = 5
ballxSpeed = random.choice((-1,1))*random.randint(1,6)/200                      # We use a random number generator to determine the speed at the beginning.
ballySpeed = random.choice((-1,1))*random.randint(1,6)/200                      # the code here generates a random integer from -5 to 5 [5,6). 6 is not included!
                                                                                # we then divide that number by 200 or the ball moves to fast. The 200 was arbitrary
                                                                                # you can play around with it until you find a good value.

rectanglePlayer = pygame.Rect(playerXPosition,playerYPosition,width,height)
rectanglePlayer2 = pygame.Rect(player2XPosition, player2YPosition , width, height)
rectanglePlayerColour = [150,23,10]                                             # 3 element array representing the colour of the player
ballColour = [250,250,250]

pygame.draw.rect(screen,rectanglePlayerColour,rectanglePlayer)
pygame.draw.circle(screen,ballColour,(ballXPosition,ballYPosition),ballRadius)  # here we use the draw module to draw a cirle. It requires 4 arguements.
                                                                                # (surface,color,position,radius)
                                                                                # surface: the object we are drawing onto. in this case it is the display objects
                                                                                # we saved as screen
                                                                                # color: color of the rectangle
                                                                                # position: a 2 element array with x and y position
                                                                                # radius: the radius of the circle



pygame.display.flip()

# below is the main game loop.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keysPressed = pygame.key.get_pressed()                                      # Here we use the built in pygame function get_pressed() to retrieve the state of all the keys
                                                                                # and save it into an array called keysPressed. Each element in keysPressed reperesents a key on
                                                                                # the keyboard. If it is a 0 the key is not pressed. If it is a 1 the key is pressed.

    if keysPressed[pygame.K_DOWN] and playerXPosition>0:                        # This if statement updates the position of the player to the left.
        playerYPosition = playerYPosition+.05                                   # Pygame has built in constants. For example pygame.K_LEFT is 276. This means that the 276th
                                                                                # element in the array returted by get_pressed() represents the left arrow key. Therefore keysPressed[pygame.K_LEFT]
                                                                                # is 1 if the left arrow is pressed and 0 if the left arrow is not pressed. In the if statement we check if the
                                                                                # key is pressed (Remember 1 = true and 0 = false) and if the position of the player is sitll within bounds of the
                                                                                # window. If it is we update the x position of the player.

    if keysPressed[pygame.K_UP] and playerXPosition<780:                        # This if statment moves the player to the right. It works in the same way as move left. One thing to note since
        playerYPosition = playerYPosition-.05                                   # The x position of the rectangle is its left edge. So if we want it to stop when the right edge hits the wall
                                                                                # we have to do 780 instead of 800. (the rectangle is 20 wide)
    if keysPressed[pygame.K_w] and playerXPosition<780:
        player2YPosition = player2YPosition-.05

    if keysPressed[pygame.K_s] and playerXPosition<780:
        player2YPosition = player2YPosition+.05


    ballXPosition = ballXPosition+ballxSpeed                                    # Update ball position
    ballYPosition = ballYPosition+ballySpeed


    rectanglePlayer = pygame.Rect(playerXPosition,playerYPosition,width,height)
    rectanglePlayer2 = pygame.Rect(player2XPosition, player2YPosition, width, height)

    #in the below section we animate our game.
    screen.fill(backgroundColour)                                               # Since our shape moved the first thing we do is clear the screen
    pygame.draw.rect(screen,rectanglePlayerColour,rectanglePlayer)              # we draw the player onto screen in its new position
    pygame.draw.rect(screen,rectanglePlayerColour,rectanglePlayer2)
    pygame.draw.circle(screen,ballColour,(int(ballXPosition),int(ballYPosition)),ballRadius) # note that when I give the position for circle draw
                                                                                             # I put each of the variables inside of a int(variable).
                                                                                             # this is because the circle version of draw only accepts integers
                                                                                             # however our ball positions are decimals
                                                                                             # the int() turns whatever is in the brackets to an integer (idk about
                                                                                             # python but other languages usually just drops the decimal numbers. some
                                                                                             # round though. you can test this yourself)
    pygame.display.flip()                                                       # we use the flip() command to display the entire window again
