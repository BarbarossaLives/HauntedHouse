import pygame
from rooms.room import Room

class Bathroom(Room):
    def __init__(self, inventory, room_manager, font):
        super().__init__("Bathroom", "assets/images/bathroom.jpg")
        self.inventory = inventory
        self.room_manager = room_manager
        self.font = font
        self.dialog_text = (
            "The bathroom light flickers. The mirror is fogged, "
            "but something seems to move in the reflection even when you don’t."
        )

        # Item: Mirror
        self.add_interactable(
            pygame.Rect(420, 150, 120, 200),  # Mirror
            "You wipe the mirror, but your reflection lingers a second too long.",
            self.trigger_mirror,
            "mirror"
            
        )

        # Exit: Back to Upstairs Hallway
        self.add_interactable(
            pygame.Rect(700, 100, 160, 550),  # To Hallway
            "You step out into the hallway, shaken by what you saw.",
            self.go_to_hallway,
            "Hallway"
        )

    def trigger_mirror(self):
        if not self.inventory.has_item("Mirror_Event"):
            self.inventory.append("Mirror Event")
            self.dialog_text = (
                "The mirror flashes with a strange light. For a moment, "
                "a second face appears beside yours, then vanishes."
                
            )
        else:
            self.dialog_text = "The mirror shows only you now... or so it seems."

    def go_to_hallway(self):
        self.dialog_text = "You step out into the hallway, glancing back at the mirror one last time."
