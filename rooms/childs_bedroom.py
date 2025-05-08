import pygame
from rooms.room import Room

class ChildsBedroom(Room):
    def __init__(self, inventory):
        super().__init__("Child's Bedroom", "assets/images/childs_bedroom.jpg")
        self.inventory = inventory
        self.dialog_text = (
            "The room is dimly lit. Faint music plays from a toy somewhere. "
            "Toys lie scattered, but something about their placement feels intentional."
        )

        # Item: Toy Box
        self.add_interactable(
            pygame.Rect(320, 300, 100, 80),  # Toy Box
            "You open the toy box. Inside, a music box... and a folded drawing of the manor.",
            self.collect_drawing
        )

        # Exit: To Upstairs Hallway
        self.add_interactable(
            pygame.Rect(100, 400, 120, 160),  # To Hallway
            "You step back into the hallway, the music fading behind you.",
            self.go_to_hallway
        )

    def collect_drawing(self):
        if "Child's Drawing" not in self.inventory:
            self.inventory.append("Child's Drawing")
            self.dialog_text = (
                "The drawing shows the manor's layout—"
                "but there's a room drawn where none should be..."
            )
        else:
            self.dialog_text = "The toy box is quiet now. The drawing is already with you."

    def go_to_hallway(self):
        self.dialog_text = "You return to the hallway, the door creaking softly shut."
