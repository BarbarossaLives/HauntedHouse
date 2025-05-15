import pygame
from rooms.room import Room


class Foyer(Room):
    def __init__(self, inventory,room_manager, font):
        super().__init__("Foyer", "assets/images/foyer.jpg")
        self.inventory = inventory
        self.manager = room_manager
        self.font = font
        self.dialog_text = "You step into the foyer of Hargrave Manor. It's silent. The air is thick with memory."

        # Items
        self.add_interactable(
            pygame.Rect(125, 200, 60, 300),  # Coat Rack
            "You brush dust off the coat rack. Something clinks—it's a key hidden inside a sleeve.",
            self.pickup_key(),
            "coat rack"
        )

        self.add_interactable(
            pygame.Rect(190, 320, 60, 200),  # Umbrella Stand
            "An old umbrella stand. Empty... but it's been moved recently.",
            "Umbrella"
        )

        # Exits
        self.add_interactable(
            pygame.Rect(325, 200, 100, 300),  # To Living Room
            "A wooden door leads into the living room. You hear a faint ticking beyond it.",
            self.go_to_living_room, 
            ";viing room"
        )

        self.add_interactable(
            pygame.Rect(800, 200, 100, 300),  # To Dining Room
            "The dining room lies behind this door. The scent of old food seeps through.",
            self.go_to_dining_room,
            "dinning Room"
        )

        self.add_interactable(
            pygame.Rect(500, 150, 300, 400),  # Stairs
            "The staircase winds upward into darkness. Cold air drifts down the steps.",
            self.go_to_stairs,
            "upstairs"
            
        )

    def pickup_key(self):
        if not self.inventory.has_item("Silver Key"):
            self.inventory.add_item("Silver Key")
            self.dialog_text = "You picked up the Silver Key."
        else:
            self.dialog_text = "You've already taken the Silver Key."

    # Placeholder transition methods — you can wire them up to room loading later
    def go_to_living_room(self):
        self.dialog_text = "You head toward the living room."
        #from room_manager import manager
        self.manager.set_current_room("living_room")

    def go_to_dining_room(self):
        self.dialog_text = "You head toward the dining room."
        #from room_manager import manager
        self.manager.set_current_room("dining_room")

    def go_to_stairs(self):
        self.dialog_text = "You begin ascending the creaking stairs."
        #from room_manager import manager
        #manager.set_current_room("upstairs_stairs_room")