import pygame
from room import Room

class SecretRoom(Room):
    def __init__(self, inventory):
        super().__init__("Secret Room", "assets/images/secret_room.png")
        self.inventory = inventory
        self.dialog_text = (
            "Behind the hidden wall lies a chamber untouched for decades. Symbols mark the floor in chalk and blood."
        )

        # Example items (customize as needed)
        self.add_interactable(
            pygame.Rect(300, 260, 120, 100),  # Ritual Circle
            "The symbols pulse faintly under your gaze. This is no ordinary room."
        )

        self.add_interactable(
            pygame.Rect(480, 320, 80, 60),  # Ancient Tome
            "A heavy tome rests on a pedestal. Its pages whisper as you draw near.",
            self.pickup_tome
        )

        # Optional: Exit back to Furnace Room or Wine Cellar
        self.add_interactable(
            pygame.Rect(100, 400, 120, 160),  # To Furnace Room
            "The wall behind you shifts slightly. The exit is still open.",
            self.go_back
        )

    def pickup_tome(self):
        if "Ancient Tome" not in self.inventory:
            self.inventory.append("Ancient Tome")
            self.dialog_text = "You take the tome. A cold sensation crawls up your spine."
        else:
            self.dialog_text = "The pedestal is empty now. The air feels heavier."

    def go_back(self):
        self.dialog_text = "You return to the furnace room, leaving the hidden chamber behind."
