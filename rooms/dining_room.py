import pygame
from rooms.room import Room

class DiningRoom(Room):
    def __init__(self, inventory, room_manager, font):
        super().__init__("Dining Room", "assets/images/dining_room.jpg")
        self.inventory = inventory
        self.manager = room_manager
        self.font = font
        self.dialog_text = (
            "The long dining table is set for a meal that never came. "
            "Dust-covered plates rest like silent witnesses."
        )

        # Items
        self.add_interactable(
            pygame.Rect(40, 110, 140, 220),  # Portrait
            "A large portrait of a stern-faced man. The eyes almost seem to follow you.",
            self.nothing(),
            "portrait"
        )

        self.add_interactable(
            pygame.Rect(60, 380, 200, 140),  # Sideboard Drawer
            "The drawer creaks open. Inside, a slip of paper with faded numbers—could this be a code?",
            self.collect_code,
            "Sideboard"
        )

        # Exits
        self.add_interactable(
            pygame.Rect(500, 250, 100, 150),  # To Foyer
            "The foyer door remains ajar, the chill from the entrance still lingering.",
            self.go_to_foyer,
            "foyer"
            
        )

        self.add_interactable(
            pygame.Rect(700, 200, 120, 300),  # To Kitchen
            "The door to the kitchen swings on old hinges, revealing shadows beyond.",
            self.go_to_kitchen,
            "kitchen"
        )

    def collect_code(self):
        if not self.inventory.has_item("Faded Code"):
            self.inventory.add_item("Faded Code")
            self.dialog_text = "You carefully pocket the faded code."
        else:
            self.dialog_text = "You already collected the code from the drawer."
    def nothing(self):
        pass
    
    # Placeholder transitions
    def go_to_foyer(self):
        self.dialog_text = "You return toward the foyer."
        #from room_manager import manager
        self.manager.set_current_room("foyer")

    def go_to_kitchen(self):
        self.dialog_text = "You enter the darkened kitchen."
       #from room_manager import manager
        self.manager.set_current_room("kitchen")
