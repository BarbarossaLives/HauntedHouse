import pygame
from rooms.room import Room

class GuestBedroom(Room):
    def __init__(self, inventory, room_manager,font):
        super().__init__("Guest Bedroom", "assets/images/guest_new.jpg")
        self.inventory = inventory
        self.manager = room_manager
        self.font = font
        self.dialog_text = (
            "The guest bedroom is tidy—too tidy. The air smells of mothballs and forgotten visits."
        )

        # Item: Dusty Suitcase
        self.add_interactable(
            pygame.Rect(5, 320, 120, 90),  # Suitcase
            "You open a dusty suitcase. Inside are clothes... and a note: 'Don't trust the portraits.'",
            self.read_suitcase_note,
            "suitcase"
        )

        # Exit: Back to Upstairs Hallway
        self.add_interactable(
            pygame.Rect(650, 100, 200, 500),  # To Upstairs Hallway
            "You quietly leave the guest bedroom.",
            self.go_to_hallway,
            "hallway"
        )

    def read_suitcase_note(self):
        if not self.inventory.has_item("Suitcase Note"):
            self.inventory.add_item("Suitcase Note")
            self.dialog_text = "The note reads: 'Don't trust the portraits.' You shiver slightly."
        else:
            self.dialog_text = "The suitcase lies open, its warning already heeded."

    def go_to_hallway(self):
        self.dialog_text = "You return to the hallway, the bedroom door clicking shut behind you."
        self.manager.set_current_room("upstairs_stairs")
        
