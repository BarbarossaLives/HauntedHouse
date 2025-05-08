import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Haunted House Layout Preview")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
DARK_GRAY = (30, 30, 30)
YELLOW = (255, 255, 0)
RED = (200, 50, 50)
GREEN = (50, 200, 50)
BLUE = (50, 50, 200)

# Fonts
font = pygame.font.Font(None, 32)

# Layout Dimensions
TITLE_HEIGHT = 60
DIALOG_HEIGHT = 120
INVENTORY_WIDTH = 300

# Rectangles
title_bar = pygame.Rect(0, 0, WIDTH, TITLE_HEIGHT)
room_area = pygame.Rect(0, TITLE_HEIGHT, WIDTH - INVENTORY_WIDTH, HEIGHT - TITLE_HEIGHT - DIALOG_HEIGHT)
inventory_area = pygame.Rect(WIDTH - INVENTORY_WIDTH, TITLE_HEIGHT, INVENTORY_WIDTH, HEIGHT - TITLE_HEIGHT - DIALOG_HEIGHT)
dialog_area = pygame.Rect(0, HEIGHT - DIALOG_HEIGHT, WIDTH, DIALOG_HEIGHT)

def draw_label(rect, label, color):
    pygame.draw.rect(screen, color, rect, 2)
    text = font.render(label, True, WHITE)
    screen.blit(text, (rect.x + 10, rect.y + 10))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    draw_label(title_bar, "Room Title Area", YELLOW)
    draw_label(room_area, "Room Image Area", GREEN)
    draw_label(inventory_area, "Inventory Area", BLUE)
    draw_label(dialog_area, "Dialog Text Area", RED)

    pygame.display.flip()

# Cleanup
pygame.quit()
sys.exit()
