import pygame
from rooms.room import Room

class UpstairsHallway(Room):
    def __init__(self, inventory, room_manager, font):
        super().__init__("Upstairs Hallway", "assets/images/upstairs_hallway.jpg")
        self.inventory = inventory
        self.room_manager = room_manager
        self.font = font
        self.dialog_text = (
            "You step into the upstairs hallway. The silence here is more personal, more watching."
        )

        # Items
        self.add_interactable(
            pygame.Rect(280, 200, 120, 180),  # Portraits
            "Several portraits line the walls. One has eyes that seem just a little too real...",
            self.check_floorboard,
            "portraits"
        )

        self.add_interactable(
            pygame.Rect(480, 360, 100, 50),  # Cracked Floorboard
            "A loose floorboard creaks underfoot. Something shifts beneath it.",
            self.check_floorboard,
            "floorboard"
        )

        # Exits
        self.add_interactable(
            pygame.Rect(650, 200, 100, 160),  # To Master Bedroom
            "The master bedroom door is slightly ajar, the smell of old perfume drifting out.",
            self.go_to_master,
            "masteer"
        )

        self.add_interactable(
            pygame.Rect(780, 220, 100, 150),  # To Guest Bedroom
            "The guest bedroom door is closed. The brass handle is slightly warm.",
            self.go_to_guest,
            "guest"
        )

        self.add_interactable(
            pygame.Rect(900, 250, 100, 150),  # To Child’s Bedroom
            "Faint music drifts from the child’s bedroom. The tune is almost familiar.",
            self.go_to_child,
            "child"
        )

    def check_floorboard(self):
        if not self.inventory.has_item("Hidden Item Upstairs"):
            self.inventory.append("Hidden Item - Upstairs")
            self.dialog_text = "You pry up the floorboard and find a small locket covered in dust."
        else:
            self.dialog_text = "You’ve already taken the locket from beneath the floorboard."

    # Exit transitions
    def go_to_master(self):
        self.dialog_text = "You carefully step into the master bedroom."

    def go_to_guest(self):
        self.dialog_text = "You open the guest bedroom door with a quiet creak."

    def go_to_child(self):
        self.dialog_text = "You follow the haunting melody into the child’s bedroom."
