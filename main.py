import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

crashed = False

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()  # Game clock (timing feature for the game, tick and shit)

carImg = pygame.image.load('res/racecar.png')

# Function to display the image
def car(x, y):
    gameDisplay.blit(carImg, (x, y))

carX = (display_width * 0.45)
carY = (display_height * 0.8)
carX_location = 0

# Basic game loop here, while we have not crashed, everything here will run (while loop)
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if the event type is recognize as quitting...
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                carX_location = -5
            elif event.key == pygame.K_RIGHT:
                carX_location = 5
                
        if event.type == pygame.KEYUP:  # If you stop pressing a key, the modifier for carX becomes 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    carX_location = 0

    carX += carX_location
    gameDisplay.fill(white)  # First paint background in white
    car(carX, carY)  # Then load the car
    pygame.display.update()
    clock.tick(60)
# End of loop

pygame.quit()
quit()
