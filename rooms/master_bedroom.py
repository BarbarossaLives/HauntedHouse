import pygame
from rooms.room import Room

class MasterBedroom(Room):
    def __init__(self, inventory, room_manager, font):
        super().__init__("Master Bedroom", "assets/images/master.jpg")
        self.inventory = inventory
        self.room_manager = room_manager
        self.font = font
        self.dialog_text = (
            "The master bedroom smells of old perfume and velvet. "
            "The bed is still made, untouched by time or turmoil."
        )

        # Item: Jewelry Box
        self.add_interactable(
            pygame.Rect(570, 350, 50, 50),  # Jewelry Box
            "A delicate jewelry box sits on the vanity. Inside, a ring with strange engravings.",
            self.collect_ring,
            "ring"
        )

        # Exit: Back to Upstairs Hallway
        self.add_interactable(
            pygame.Rect(700, 180, 160, 360),  # To Upstairs Hallway
            "You step back into the upstairs hallway, the air cooler than before.",
            self.go_to_hallway,
            "hallway"
        )

    def collect_ring(self):
        if not self.inventory.has_item("Engraved Ring"):
            self.inventory.append("Engraved Ring")
            self.dialog_text = "You pocket the ring. It feels unnaturally warm."
        else:
            self.dialog_text = "The jewelry box is empty now, its lid quietly shut."

    def go_to_hallway(self):
        self.dialog_text = "You quietly return to the upstairs hallway."
