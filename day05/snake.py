import pygame

# Initialize pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~SNEKE~~")

# Set FSP and clock)
FPS = 20
clock = pygame.time.Clock()
# Set game values
# Set colors

GREEN = (0, 255, 0)
DARKRED = (150, 0, 0)
# Set fonts
font = pygame.font.SysFont('gabriola', 48)


# Set text
title_text = font.render("~~Snake~~", True, GREEN, DARKRED)  # make a text object
title_rect = title_text.get_rect()  # gets the box containing the text object
title_rect.center = (WINDOW_WIDTH // 2,
                     WINDOW_HEIGHT // 2)  # places the box containing the text object's center to the middle of the screen.

# Set sounds and music
pick_up_sound = pygame.mixer.Sound("pick_up_sound.wav")

# Set images (in this case, use simple rects...so just create their coordinates)
# For a rectangle you need (top-left x, top-left y, width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)
body_coords = []
# The main game loop
running = True
is_paused = False
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the snake

    # Add the head coordinate to the first index of the body coordinate list
    # This will essentially move all the snakes body by one position in the list

    # Update the x,y position of the snakes head and make a new coordinate

    # Check for game over
    if head_rect.left < 0 or head_rect.right > WINDOW_WIDTH or head_rect.top < 0 or head_rect.bottom > WINDOW_HEIGHT or head_coord in body_coords:
        while is_paused:
            for event in pygame.event.get():
                # The player wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
    # Check for collisions
    if head_rect.colliderect(apple_rect):
        random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
    # Update HUD

    # Fill the surface

    # Blit HUD

    # Blit assets

    # Update display and tick clock

# End the game
pygame.quit()
