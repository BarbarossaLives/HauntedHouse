import pygame
from rooms.room import Room

class SecretRoom(Room):
    def __init__(self, inventory, room_manager, font):
        super().__init__("Secret Room", "assets/images/secretroom.jpg")
        self.inventory = inventory
        self.room_manager = room_manager
        self.font = font
        self.dialog_text = (
            "Behind the hidden wall lies a chamber untouched for decades. Symbols mark the floor in chalk and blood."
        )

        # Example items (customize as needed)
        self.add_interactable(
            pygame.Rect(600, 200, 220, 280),  # Ritual Circle
            "The symbols pulse faintly under your gaze. This is no ordinary room.",
            self.pickup_tome,
            "ritual"
        )

        self.add_interactable(
            pygame.Rect(380, 320, 180, 60),  # Ancient Tome
            "A heavy tome rests on a pedestal. Its pages whisper as you draw near.",
            self.pickup_tome,
            "tome"
        )

        # Optional: Exit back to Furnace Room or Wine Cellar
        self.add_interactable(
            pygame.Rect(80, 150, 200, 460),  # To Furnace Room
            "The wall behind you shifts slightly. The exit is still open.",
            self.go_back,
            "furnace"
        )

    def pickup_tome(self):
        if not self.inventory.has_item("Ancient Tome"):
            self.inventory.append("Ancient Tome")
            self.dialog_text = "You take the tome. A cold sensation crawls up your spine."
        else:
            self.dialog_text = "The pedestal is empty now. The air feels heavier."

    def go_back(self):
        self.dialog_text = "You return to the furnace room, leaving the hidden chamber behind."
