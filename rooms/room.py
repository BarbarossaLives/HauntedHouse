import pygame

ROOM_WIDTH = 900
ROOM_HEIGHT = 620


class Room:
    def __init__(self, name, image_path):
        self.name = name
        original_image = pygame.image.load(image_path).convert()
        self.background = pygame.transform.scale(original_image, (ROOM_WIDTH, ROOM_HEIGHT))
        self.interactables = []  # List of {rect, dialog, callback (optional)}
        self.dialog_text = ""    # The last dialog triggered in this room

    ROOM_AREA = pygame.Rect(0, 60, 900, 620)  # x, y, width, height
    
    def add_interactable(self, rect, dialog_text, callback=None, label="", color=(255,0,0),font=None):
        """Add a clickable area with optional behavior."""
        self.interactables.append({
            'rect': rect,
            'dialog': dialog_text,
            'callback': callback,
            'label': label,
            'color': color,
            'font': font
        })

    def handle_event(self, event):
        """Check if the player clicked on any interactable area."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for item in self.interactables:
                if item['rect'].collidepoint(mouse_pos):
                    self.dialog_text = item['dialog']
                    if item['callback']:
                        item['callback']()
                    break

    def update(self):
        """Update room logic (not much for now)."""
        pass

    def draw(self, screen):
        # Draw room background
        screen.blit(self.background, (0, 60))  # Top bar is 60px high

        # Draw title bar
        pygame.draw.rect(screen, (20, 20, 20), pygame.Rect(0, 0, 1200, 60))
        font = pygame.font.Font(None, 36)
        title = font.render(f"{self.name}", True, (255, 255, 0))
        screen.blit(title, (20, 15))

        # Draw dialog area
        pygame.draw.rect(screen, (30, 30, 30), pygame.Rect(0, 680, 1200, 120))
        dialog_font = pygame.font.Font(None, 28)
        dialog = dialog_font.render(self.dialog_text, True, (255, 255, 255))
        screen.blit(dialog, (20, 700))

        # Draw interactable debug outlines (optional)
        for item in self.interactables:
            pygame.draw.rect(screen, (255, 0, 0), item['rect'], 2)


            # For debugging: draw interactables
            for item in self.interactables:
                pygame.draw.rect(screen, (255, 0, 0), item['rect'], 2)
                
                label_surface = self.font.render(item['label'], True, (255,255,255))
                label_rect = label_surface.get_rect()
                label_rect.center = item['rect'].center
                screen.blit(label_surface, label_rect)

    def get_dialog(self):
        """Return the current dialog for display."""
        return self.dialog_text
