import pygame
from rooms.room import Room

class Kitchen(Room):
    def __init__(self, inventory, room_manager, font):
        super().__init__("Kitchen", "assets/images/kitchen_new.jpg")
        self.inventory = inventory
        self.room_manager = room_manager
        self.font = font
        self.dialog_text = (
            "Dust hangs in the air. The lights flicker as you enter, "
            "illuminating grime-covered counters and age-worn appliances."
        )

        # Items
        self.add_interactable(
            pygame.Rect(140, 340, 150, 200),  # Stove
            "The stove's surface is cold, but a faint warmth lingers beneath the burners.",
            self.pickup_key,
            "stove"
        )

        self.add_interactable(
            pygame.Rect(330, 150, 200, 150),  # Cabinet
            "Inside the cabinet, cracked dishes and a faded note: 'He said not to enter the basement...'.",
            self.pickup_key,
            "cabinet"
        )

        self.add_interactable(
            pygame.Rect(530, 280, 100, 240),  # Refrigerator
            "The refrigerator creaks open. Empty, except for a rusted key tied with string.",
            self.pickup_key,
            "Fridge"
        )

        # Exits
        self.add_interactable(
            pygame.Rect(5, 150, 100, 450),  # To Dining Room
            "The dining room door sits crooked on its hinges, letting in a draft.",
            self.go_to_dining_room,
            "dining"
        )

        self.add_interactable(
            pygame.Rect(630, 150, 100, 400),  # To Pantry
            "A sliding door leads into a small pantry. Something shifts in the shadows.",
            self.go_to_pantry,
            "Pantry"
        )

        self.add_interactable(
            pygame.Rect(750,100, 120, 400),  # To Basement Stairs
            "A heavy door with scratch marks leads to the basement stairs. It smells like mold and metal.",
            self.go_to_basement,
            "basement"
        )

    def pickup_key(self):
        if not self.inventory.has_item("Rusted Key"):
            self.inventory.append("Rusted Key")
            self.dialog_text = "You take the rusted key, unsure what it might unlock."
        else:
            self.dialog_text = "The refrigerator is empty now. Just rust and shadows."

    # Placeholder transition methods
    def go_to_dining_room(self):
        self.dialog_text = "You push back into the dining room."

    def go_to_pantry(self):
        self.dialog_text = "You open the pantry door and peer inside."

    def go_to_basement(self):
        self.dialog_text = "You steel yourself and open the basement door."
