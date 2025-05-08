import pygame
from rooms.room import Room

class GuestBedroom(Room):
    def __init__(self, inventory):
        super().__init__("Guest Bedroom", "assets/images/guest_bedroom.jpg")
        self.inventory = inventory
        self.dialog_text = (
            "The guest bedroom is tidy—too tidy. The air smells of mothballs and forgotten visits."
        )

        # Item: Dusty Suitcase
        self.add_interactable(
            pygame.Rect(340, 320, 120, 90),  # Suitcase
            "You open a dusty suitcase. Inside are clothes... and a note: 'Don't trust the portraits.'",
            self.read_suitcase_note
        )

        # Exit: Back to Upstairs Hallway
        self.add_interactable(
            pygame.Rect(100, 400, 120, 160),  # To Upstairs Hallway
            "You quietly leave the guest bedroom.",
            self.go_to_hallway
        )

    def read_suitcase_note(self):
        if "Suitcase Note" not in self.inventory:
            self.inventory.append("Suitcase Note")
            self.dialog_text = "The note reads: 'Don't trust the portraits.' You shiver slightly."
        else:
            self.dialog_text = "The suitcase lies open, its warning already heeded."

    def go_to_hallway(self):
        self.dialog_text = "You return to the hallway, the bedroom door clicking shut behind you."
