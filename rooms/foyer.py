import pygame
from rooms.room import Room

class Foyer(Room):
    def __init__(self, inventory):
        super().__init__("Foyer", "assets/images/foyer.jpg")
        self.inventory = inventory
        self.dialog_text = "You step into the foyer of Hargrave Manor. It's silent. The air is thick with memory."

        # Items
        self.add_interactable(
            pygame.Rect(150, 300, 60, 100),  # Coat Rack
            "You brush dust off the coat rack. Something clinks—it's a key hidden inside a sleeve.",
            self.pickup_key
        )

        self.add_interactable(
            pygame.Rect(250, 320, 40, 80),  # Umbrella Stand
            "An old umbrella stand. Empty... but it's been moved recently."
        )

        # Exits
        self.add_interactable(
            pygame.Rect(500, 250, 100, 150),  # To Living Room
            "A wooden door leads into the living room. You hear a faint ticking beyond it.",
            self.go_to_living_room
        )

        self.add_interactable(
            pygame.Rect(650, 250, 100, 150),  # To Dining Room
            "The dining room lies behind this door. The scent of old food seeps through.",
            self.go_to_dining_room
        )

        self.add_interactable(
            pygame.Rect(800, 150, 80, 200),  # Stairs
            "The staircase winds upward into darkness. Cold air drifts down the steps.",
            self.go_to_stairs
        )

    def pickup_key(self):
        if "Silver Key" not in self.inventory:
            self.inventory.append("Silver Key")
            self.dialog_text = "You picked up the Silver Key."
        else:
            self.dialog_text = "You've already taken the Silver Key."

    # Placeholder transition methods — you can wire them up to room loading later
    def go_to_living_room(self):
        self.dialog_text = "You head toward the living room."
        from room_manager import manager
        manager.set_current_room("living_room")

    def go_to_dining_room(self):
        self.dialog_text = "You head toward the dining room."
        from room_manager import manager
        manager.set_current_room("dining_room")

    def go_to_stairs(self):
        self.dialog_text = "You begin ascending the creaking stairs."
        #from room_manager import manager
        #manager.set_current_room("upstairs_stairs_room")