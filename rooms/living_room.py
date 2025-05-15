import pygame
from rooms.room import Room

class LivingRoom(Room):
    def __init__(self, inventory, room_manager, font):
        super().__init__("Living Room", "assets/images/living.jpg")
        self.inventory = inventory
        self.room_manager = room_manager
        self.font = font
        self.dialog_text = (
            "Dust motes dance in the filtered light. "
            "The silence is deeper here, like the room is holding its breath."
        )

        # Items
        self.add_interactable(
            pygame.Rect(40, 150, 100, 130),  # Mirror
            "The mirror is clouded, but for a moment, a pale reflection moves where yours should be.",
            self.go_to_foyer,
            "mirror"
        )

        self.add_interactable(
            pygame.Rect(480, 170, 100, 160),  # Picture Frame
            "The picture frame holds a faded photo. Scribbled on the back: 'They never saw it coming.'",
            self.go_to_foyer,
            "Picture Frame"
        )

        # Exits
        self.add_interactable(
            pygame.Rect(250, 200, 120, 300),  # To Foyer
            "You glance back toward the foyer. It feels further away than it should.",
            self.go_to_foyer,
            "foyer"
        )

        self.add_interactable(
            pygame.Rect(700, 200, 160, 300),  # To Library
            "The library door creaks open slightly as if inviting you in.",
            self.go_to_library,
            "library"
        )

    # Placeholder transition methods
    def go_to_foyer(self):
        self.dialog_text = "You step cautiously back toward the foyer."

    def go_to_library(self):
        self.dialog_text = "You cross the room and push open the door to the library."
