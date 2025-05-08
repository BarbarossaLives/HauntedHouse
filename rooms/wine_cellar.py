import pygame
from rooms.room import Room

class WineCellar(Room):
    def __init__(self, inventory):
        super().__init__("Wine Cellar", "assets/images/wine_cellar.jpg")
        self.inventory = inventory
        self.dialog_text = (
            "The air is damp and heavy. A chill runs through the stone walls of the cellar."
        )

        # Items
        self.add_interactable(
            pygame.Rect(300, 250, 140, 120),  # Wine Rack
            "Rows of dusty wine bottles line the shelves. One bottle seems recently disturbed."
        )

        self.add_interactable(
            pygame.Rect(480, 280, 100, 100),  # Locked Cabinet
            "The cabinet creaks but won’t open. Something rattles inside."
        )

        # Exit
        self.add_interactable(
            pygame.Rect(100, 400, 120, 160),  # To Basement Stairs
            "A steep set of stairs creaks with every step. You feel the house above pressing down.",
            self.go_to_basement_stairs
        )

    # Placeholder transition
    def go_to_basement_stairs(self):
        self.dialog_text = "You slowly climb back toward the main basement hall."
