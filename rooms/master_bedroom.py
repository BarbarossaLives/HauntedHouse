import pygame
from rooms.room import Room

class MasterBedroom(Room):
    def __init__(self, inventory):
        super().__init__("Master Bedroom", "assets/images/master_bedroom.jpg")
        self.inventory = inventory
        self.dialog_text = (
            "The master bedroom smells of old perfume and velvet. "
            "The bed is still made, untouched by time or turmoil."
        )

        # Item: Jewelry Box
        self.add_interactable(
            pygame.Rect(360, 280, 100, 80),  # Jewelry Box
            "A delicate jewelry box sits on the vanity. Inside, a ring with strange engravings.",
            self.collect_ring
        )

        # Exit: Back to Upstairs Hallway
        self.add_interactable(
            pygame.Rect(100, 400, 120, 160),  # To Upstairs Hallway
            "You step back into the upstairs hallway, the air cooler than before.",
            self.go_to_hallway
        )

    def collect_ring(self):
        if "Engraved Ring" not in self.inventory:
            self.inventory.append("Engraved Ring")
            self.dialog_text = "You pocket the ring. It feels unnaturally warm."
        else:
            self.dialog_text = "The jewelry box is empty now, its lid quietly shut."

    def go_to_hallway(self):
        self.dialog_text = "You quietly return to the upstairs hallway."
