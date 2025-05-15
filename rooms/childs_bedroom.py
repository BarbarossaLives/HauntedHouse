import pygame
from rooms.room import Room

class ChildsBedroom(Room):
    def __init__(self, inventory, room_manager, font):
        super().__init__("Child's Bedroom", "assets/images/childs_bedroom.jpg")
        self.inventory = inventory
        self.room_manager = room_manager
        self.font = font
        self.dialog_text = (
            "The room is dimly lit. Faint music plays from a toy somewhere. "
            "Toys lie scattered, but something about their placement feels intentional."
        )

        # Item: Toy Box
        self.add_interactable(
            pygame.Rect(320, 200, 100, 250),  # Toy Box
            "You open the toy box. Inside, a music box... and a folded drawing of the manor.",
            self.collect_drawing,
            "toybox"
        )

        # Exit: To Upstairs Hallway
        self.add_interactable(
            pygame.Rect(720, 200, 180,360),  # To Hallway
            "You step back into the hallway, the music fading behind you.",
            self.go_to_hallway,
            "Upstairs"
        )

    def collect_drawing(self):
        if not self.inventory.has_item("Child's Drawing"):
            self.inventory.append("Child's Drawing")
            self.dialog_text = (
                "The drawing shows the manor's layout—"
                "but there's a room drawn where none should be..."
            )
        else:
            self.dialog_text = "The toy box is quiet now. The drawing is already with you."

    def go_to_hallway(self):
        self.dialog_text = "You return to the hallway, the door creaking softly shut."
