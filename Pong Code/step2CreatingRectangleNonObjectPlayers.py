#By Leon Zhou
import pygame as pygame #import required modules

# The below code shows how to add a player as just a shape without
#using objects. We build on the window creation example. Explanation for
# window code is omitted

dimensions = [500,300]
screen = pygame.display.set_mode(dimensions)
backgroundColour = [0,0,0]
screen.fill(backgroundColour)
running = True


playerXPosition = 450                                                           #Here we initiate the x and y location of the player
playerYPosition = 125

player2XPosition = 40
player2YPosition = 125

width = 10
height = 50
rectanglePlayer = pygame.Rect(playerXPosition,playerYPosition,width,height)     # This line creates a Rect object. The rect object requires four atributes
                                                                                # Rect(x-coordinate of left edge, y coordinate of top edge, width, height)
rectanglePlayer2 = pygame.Rect(player2XPosition, player2YPosition , width, height)

rectanglePlayerColour = [150,23,10]                                             # 3 element array representing the colour of the player

pygame.draw.rect(screen,rectanglePlayerColour,rectanglePlayer)                  # here we use the draw module to draw a rectangle. It requires 4 arguements.
                                                                                # (surface,color,rectangle, borderwidth)
                                                                                # surface: the object we are drawing onto. in this case it is the display objects
                                                                                # we saved as screen
                                                                                # color: color of the rectangle
                                                                                # rectangle: the rectangle object we want to draw
                                                                                # borderwidth: the width of the border (default is 0) you don't have to put anything for this one
pygame.draw.rect(screen,rectanglePlayerColour,rectanglePlayer2)
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


    rectanglePlayer = pygame.Rect(playerXPosition,playerYPosition,width,height)
    rectanglePlayer2 = pygame.Rect(player2XPosition, player2YPosition, width, height)
    #in the below section we animate our game.
    screen.fill(backgroundColour)                                               # Since our shape moved the first thing we do is clear the screen
    pygame.draw.rect(screen,rectanglePlayerColour,rectanglePlayer)              # we draw the player onto screen in its new position
    pygame.draw.rect(screen,rectanglePlayerColour,rectanglePlayer2)
    pygame.display.flip()                                                       # we use the flip() command to display the entire window again
