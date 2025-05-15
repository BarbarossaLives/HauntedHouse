import pygame
from rooms.room import Room

class UpstairsStairsRoom(Room):
    def __init__(self, inventory, room_manager, font):
        super().__init__("Main Staircase", "assets/images/upstairs_stairs.jpg")
        self.inventory = inventory
        self.room_manager = room_manager
        self.font = font
        self.dialog_text = (
            "The grand staircase rises ahead. The wood creaks under your step, "
            "and the air grows colder the higher you climb."
        )

        # Item: Framed Portrait (atmosphere)
        self.add_interactable(
            pygame.Rect(400, 220, 100, 140),  # Portrait
            "A large portrait of a woman stares down at you. Her eyes seem freshly painted.",
            self.observe_portrait
        )

        # Exit: Down to Foyer
        self.add_interactable(
            pygame.Rect(100, 400, 120, 160),  # To Foyer
            "You descend back to the foyer, the weight of eyes on your back.",
            self.go_to_foyer
        )

        # Exit: Up to Upstairs Hallway
        self.add_interactable(
            pygame.Rect(600, 200, 120, 160),  # To Upstairs
            "You reach the top of the stairs and step into the upstairs hallway.",
            self.go_to_upstairs
        )

    def observe_portrait(self):
        if not self.inventory.has_item("Stair Portrait"):
            self.inventory.append("Stair Portrait Observed")
            self.dialog_text = "Her gaze is unsettling. You swear the eyes moved."
        else:
            self.dialog_text = "The portrait remains unchanged. Or does it?"

    def go_to_foyer(self):
        self.dialog_text = "You descend to the foyer below."
        # room_manager.set_current_room("foyer")

    def go_to_upstairs(self):
        self.dialog_text = "You enter the hallway above, the silence thicker here."
        # room_manager.set_current_room("upstairs")
