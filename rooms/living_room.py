import pygame
from rooms.room import Room

class LivingRoom(Room):
    def __init__(self, inventory):
        super().__init__("Living Room", "assets/images/living_room.jpg")
        self.inventory = inventory
        self.dialog_text = (
            "Dust motes dance in the filtered light. "
            "The silence is deeper here, like the room is holding its breath."
        )

        # Items
        self.add_interactable(
            pygame.Rect(180, 260, 100, 150),  # Mirror
            "The mirror is clouded, but for a moment, a pale reflection moves where yours should be."
        )

        self.add_interactable(
            pygame.Rect(400, 220, 80, 60),  # Picture Frame
            "The picture frame holds a faded photo. Scribbled on the back: 'They never saw it coming.'"
        )

        # Exits
        self.add_interactable(
            pygame.Rect(50, 300, 100, 200),  # To Foyer
            "You glance back toward the foyer. It feels further away than it should.",
            self.go_to_foyer
        )

        self.add_interactable(
            pygame.Rect(700, 280, 120, 200),  # To Library
            "The library door creaks open slightly as if inviting you in.",
            self.go_to_library
        )

    # Placeholder transition methods
    def go_to_foyer(self):
        self.dialog_text = "You step cautiously back toward the foyer."

    def go_to_library(self):
        self.dialog_text = "You cross the room and push open the door to the library."
