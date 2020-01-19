import pygame as pygame #import required modules

#Here we create a display object. We call it screen.

dimensions = [200,200]                       # Dimensions of the window to be created. It's a 2 element array. [width,height]

screen = pygame.display.set_mode(dimensions) # Here we call the display module within pygame. The set_mode function
                                             # initiates a display window. The function takes one argument (a 2 element)
                                             # array that determines the size of the window.


backgroundColour = [0,0,0]                   # Here we create a 3 element array to represent the
                                             # RGB values of the background [R,G,B]

screen.fill(backgroundColour)                # We call the fill function of the display object (screen) to set the
                                             # back ground colour to the values stored in backgroundColour

pygame.display.flip()                        # we can the flip function here which updates the
                                             # full display Surface to the screen

# The bottom code will prevent the screen from closing until we close the window. Or else the screen will close immediately.
# The while loop below will also act as the main game loop
running = True                               # a boolean variable to store the state of the program

while running:                               # This is a while loop. As long as the value of running is true the loop will continue to iterate

    for event in pygame.event.get():         # This is a for loop that cycles through all "events". events are interuptions like
                                             # keystrokes or mouseclicks. The forloop checks all events witch each iteration of the while loop

        if event.type == pygame.QUIT:        # We check each even to see what it is (keypress/mouseclick/other command) if the event is the
            running = False                  # windown being closed we set runnin to false which means the while loop stops running and
                                             # the program will terminate
