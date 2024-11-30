# SETUP & INITIALIZE
import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# GAME ELEMENTS

# Player properties
player_width = 100
player_height = 20
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 10

# Falling object properties
object_width = 30
object_height = 30
object_x = random.randint(0, SCREEN_WIDTH - object_width)
object_y = -object_height
object_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# GAME LOOP
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Get user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed
        
    # Move Falling Object
    object_y += object_speed
    if object_y > SCREEN_HEIGHT:
        object_y = object_height
        object_x = random.randint(0, SCREEN_WIDTH - object_width)
        
    # Collision detection
    if (player_x < object_x < player_x + player_width or player_x < object_x + object_width < player_x + player_width) and (player_y < object_y + object_height < player_y + player_height):
        score += 1
        object_y = -object_height
        object_x = random.randint(0, SCREEN_WIDTH - object_width)
        
    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height)) #Player
    pygame.draw.rect(screen, RED, (object_x, object_y, object_width, object_height)) #Falling Object
    
    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10,10))
    
    # Update display
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(FPS)

pygame.quit()