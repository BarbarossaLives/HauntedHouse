import pygame

class Room:
    def __init__(self, name, image_path):
        self.name = name
        self.background = pygame.image.load(image_path).convert()
        self.interactables = []  # List of {rect, dialog, callback (optional)}
        self.dialog_text = ""    # The last dialog triggered in this room

    def add_interactable(self, rect, dialog_text, callback=None):
        """Add a clickable area with optional behavior."""
        self.interactables.append({
            'rect': rect,
            'dialog': dialog_text,
            'callback': callback
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
        """Draw the background and (optionally) interactable areas."""
        screen.blit(self.background, (0, 60))  # assumes 60px top for room title

        # For debugging: draw interactables
        for item in self.interactables:
            pygame.draw.rect(screen, (255, 0, 0), item['rect'], 2)

    def get_dialog(self):
        """Return the current dialog for display."""
        return self.dialog_text
