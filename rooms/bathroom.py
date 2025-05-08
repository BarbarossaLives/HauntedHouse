import pygame
from rooms.room import Room

class Bathroom(Room):
    def __init__(self, inventory):
        super().__init__("Bathroom", "assets/images/bathroom.jpg")
        self.inventory = inventory
        self.dialog_text = (
            "The bathroom light flickers. The mirror is fogged, "
            "but something seems to move in the reflection even when you don’t."
        )

        # Item: Mirror
        self.add_interactable(
            pygame.Rect(360, 220, 120, 100),  # Mirror
            "You wipe the mirror, but your reflection lingers a second too long.",
            self.trigger_mirror
        )

        # Exit: Back to Upstairs Hallway
        self.add_interactable(
            pygame.Rect(100, 400, 120, 160),  # To Hallway
            "You step out into the hallway, shaken by what you saw.",
            self.go_to_hallway
        )

    def trigger_mirror(self):
        if "Mirror Event" not in self.inventory:
            self.inventory.append("Mirror Event")
            self.dialog_text = (
                "The mirror flashes with a strange light. For a moment, "
                "a second face appears beside yours, then vanishes."
            )
        else:
            self.dialog_text = "The mirror shows only you now... or so it seems."

    def go_to_hallway(self):
        self.dialog_text = "You step out into the hallway, glancing back at the mirror one last time."
