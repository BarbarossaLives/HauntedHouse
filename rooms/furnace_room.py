import pygame
from rooms.room import Room

class FurnaceRoom(Room):
    def __init__(self, inventory, room_manager, font):
        super().__init__("Furnace Room", "assets/images/furnace_room.jpg")
        self.inventory = inventory
        self.room_manager = room_manager
        self.font = font
        self.dialog_text = (
            "The air is damp and heavy. A chill runs through the stone walls of the cellar."
        )

        # Interactable Item: Furnace Switch
        self.add_interactable(
            pygame.Rect(20, 300, 100, 80),  # Furnace Switch
            "A switch beside the furnace hums faintly. It looks recently used.",
            self.flip_switch,
            "furnace"
        )

    def flip_switch(self):
        if not self.inventory.has_item("Furnace Switch"):
            self.inventory.append("Furnace Switch Flipped")
            self.dialog_text = "You flip the switch. A deep rumble echoes through the walls."
        else:
            self.dialog_text = "The switch has already been flipped."
