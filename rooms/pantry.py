import pygame
from rooms.room import Room

class Pantry(Room):
    def __init__(self, inventory,room_manager, font):
        super().__init__("Pantry", "assets/images/pantry_new.jpg")
        self.inventory = inventory
        self.manager = room_manager
        self.font = font
        self.dialog_text = "You step into the pantry. It's filled with canned and old bagged goods."


        self.add_interactable(
            pygame.Rect(400, 150, 150, 400),  # Stairs
            "The staircase winds upward into darkness. Cold air drifts down the steps.",
            self.go_to_kitchen,
            "kitchen"
            
        )



    def go_to_kitchen(self):
        self.dialog_text = "You return the kitchen"
        #from room_manager import manager
        self.manager.set_current_room("kitchen")
        
