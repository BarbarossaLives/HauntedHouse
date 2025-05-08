creeate a compreensive table for the basement with all the dialog and collectable and eixit infor mation for all the roomsimport pygame
from room import Room

class Kitchen(Room):
    def __init__(self, inventory):
        super().__init__("Kitchen", "assets/images/kitchen.png")
        self.inventory = inventory
        self.dialog_text = (
            "Dust hangs in the air. The lights flicker as you enter, "
            "illuminating grime-covered counters and age-worn appliances."
        )

        # Items
        self.add_interactable(
            pygame.Rect(220, 320, 100, 60),  # Stove
            "The stove's surface is cold, but a faint warmth lingers beneath the burners."
        )

        self.add_interactable(
            pygame.Rect(340, 280, 100, 80),  # Cabinet
            "Inside the cabinet, cracked dishes and a faded note: 'He said not to enter the basement...'."
        )

        self.add_interactable(
            pygame.Rect(460, 300, 100, 120),  # Refrigerator
            "The refrigerator creaks open. Empty, except for a rusted key tied with string.",
            self.pickup_key
        )

        # Exits
        self.add_interactable(
            pygame.Rect(70, 200, 100, 150),  # To Dining Room
            "The dining room door sits crooked on its hinges, letting in a draft.",
            self.go_to_dining_room
        )

        self.add_interactable(
            pygame.Rect(680, 240, 100, 140),  # To Pantry
            "A sliding door leads into a small pantry. Something shifts in the shadows.",
            self.go_to_pantry
        )

        self.add_interactable(
            pygame.Rect(900, 250, 120, 180),  # To Basement Stairs
            "A heavy door with scratch marks leads to the basement stairs. It smells like mold and metal.",
            self.go_to_basement
        )

    def pickup_key(self):
        if "Rusted Key" not in self.inventory:
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
