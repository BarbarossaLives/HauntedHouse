import pygame
from rooms.room import Room

class UpstairsStairsRoom(Room):
    def __init__(self, inventory, room_manager, font):
        super().__init__("Hallway", "assets/images/hallway.jpg")
        self.inventory = inventory
        self.manager = room_manager
        self.font = font
        self.dialog_text = (
            "The grand staircase rises ahead. The wood creaks under your step, "
            "and the air grows colder the higher you climb."
        )

        # Item: Framed Portrait (atmosphere)
        self.add_interactable(
            pygame.Rect(370, 220, 100, 140),  # Portrait
            "A large portrait of a woman stares down at you. Her eyes seem freshly painted.",
            self.observe_portrait,
            "portrait"
        )

        # Exit: Down to Foyer
        self.add_interactable(
            pygame.Rect(5, 120, 120, 560),  # To Foyer
            "You descend back to the foyer, the weight of eyes on your back.",
            self.go_to_foyer,
            "foyer"
        )

        # Exit: Up to Upstairs Hallway
        self.add_interactable(
            pygame.Rect(750, 160, 120, 460),  # To Upstairs
            "You reach the top of the stairs and step into the upstairs hallway.",
            self.go_to_master,
            "master"
        )
        
        self.add_interactable(
            pygame.Rect(160, 160, 150, 360),  # To Upstairs
            "You reach the top of the stairs and step into the upstairs hallway.",
            self.go_to_guest,
            "guest"       
        )
        
        self.add_interactable(
            pygame.Rect(530, 160, 150, 360),  # To Upstairs
            "You reach the top of the stairs and step into the upstairs hallway.",
            self.go_to_childs,
            "childs"   
        )
        
    def observe_portrait(self):
        if not self.inventory.has_item("Stair Portrait"):
            self.inventory.add_item("Stair Portrait Observed")
            self.dialog_text = "Her gaze is unsettling. You swear the eyes moved."
        else:
            self.dialog_text = "The portrait remains unchanged. Or does it?"

    def go_to_foyer(self):
        self.dialog_text = "You descend to the foyer below."
        self.manager.set_current_room("foyer")

    def go_to_master(self):
        self.dialog_text = "You enter the hallway above, the silence thicker here."
        self.manager.set_current_room("master")

    def go_to_childs(self):
        self.dialog_text = "You enter the hallway above, the silence thicker here."
        self.manager.set_current_room("childs")
        
        
    def go_to_guest(self):
        self.dialog_text = "You enter the hallway above, the silence thicker here."
        self.manager.set_current_room("guest")