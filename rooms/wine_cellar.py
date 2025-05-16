import pygame
from rooms.room import Room

class WineCellar(Room):
    def __init__(self, inventory, room_manager, font):
        super().__init__("Wine Cellar", "assets/images/wine_new.jpg")
        self.inventory = inventory
        self.manager = room_manager
        self.font = font
        self.dialog_text = (
            "The air is damp and heavy. A chill runs through the stone walls of the cellar."
        )

        # Items
        self.add_interactable(
            pygame.Rect(250, 330, 150, 180),  # Wine Rack
            "Rows of dusty wine bottles line the shelves. One bottle seems recently disturbed.",
            self.nothing(),
            "wine"
        )

        self.add_interactable(
            pygame.Rect(430, 100, 220, 450),  # Locked Cabinet
            "The cabinet creaks but won’t open. Something rattles inside.",
            self.nothing(),
            "cabinate"
        )

        # Exit
        self.add_interactable(
            pygame.Rect(0, 100, 180, 550),  # To Basement Stairs
            "A steep set of stairs creaks with every step. You fend up back in the kitchen.",
            self.go_to_basement_stairs,
            "kitchen"
        )
        
                
        self.add_interactable(
            pygame.Rect(700,100,200,450),
            "The furnace room becons you.",
            self.go_to_furnace_room,
            "furnace"
        )

    def nothing(self):
        pass
    
    # Placeholder transition
    def go_to_basement_stairs(self):
        self.dialog_text = "You slowly climb back toward the main basement hall."
        self.manager.set_current_room("kitchen")
        
    def go_to_furnace_room(self):
        self.dialog_text = "You head to the furnace room"
        #from room_manager import manager
        self.manager.set_current_room("furnace_room")