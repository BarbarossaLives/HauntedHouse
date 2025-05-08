import pygame
from rooms.room import Room

class DiningRoom(Room):
    def __init__(self, inventory):
        super().__init__("Dining Room", "assets/images/dining_room.jpg")
        self.inventory = inventory
        self.dialog_text = (
            "The long dining table is set for a meal that never came. "
            "Dust-covered plates rest like silent witnesses."
        )

        # Items
        self.add_interactable(
            pygame.Rect(500, 180, 120, 200),  # Portrait
            "A large portrait of a stern-faced man. The eyes almost seem to follow you."
        )

        self.add_interactable(
            pygame.Rect(320, 400, 100, 60),  # Sideboard Drawer
            "The drawer creaks open. Inside, a slip of paper with faded numbers—could this be a code?",
            self.collect_code
        )

        # Exits
        self.add_interactable(
            pygame.Rect(80, 250, 100, 150),  # To Foyer
            "The foyer door remains ajar, the chill from the entrance still lingering.",
            self.go_to_foyer
        )

        self.add_interactable(
            pygame.Rect(700, 260, 120, 160),  # To Kitchen
            "The door to the kitchen swings on old hinges, revealing shadows beyond.",
            self.go_to_kitchen
        )

    def collect_code(self):
        if "Faded Code" not in self.inventory:
            self.inventory.append("Faded Code")
            self.dialog_text = "You carefully pocket the faded code."
        else:
            self.dialog_text = "You already collected the code from the drawer."

    # Placeholder transitions
    def go_to_foyer(self):
        self.dialog_text = "You return toward the foyer."

    def go_to_kitchen(self):
        self.dialog_text = "You enter the darkened kitchen."
