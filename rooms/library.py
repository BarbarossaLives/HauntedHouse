import pygame
from rooms.room import Room

class Library(Room):
    def __init__(self, inventory, room_manager):
        super().__init__("Library", "assets/images/library.jpg")
        self.inventory = inventory
        self.room_manager = room_manager
        self.dialog_text = (
            "The library smells of dust, leather, and secrets. "
            "Shelves tower high, packed with forgotten knowledge."
        )

        # Item: Bookshelf (atmospheric, maybe triggers secret?)
        self.add_interactable(
            pygame.Rect(280, 200, 140, 200),  # Bookshelf
            "You scan the bookshelf... one of the books seems oddly placed.",
            self.shift_bookshelf
        )

        # Item: Marked Book (collectible clue)
        self.add_interactable(
            pygame.Rect(440, 240, 100, 80),  # Marked Book
            "A book bound in red leather. You flip it open and see a handwritten message.",
            self.collect_book
        )

        # Exit: To Living Room
        self.add_interactable(
            pygame.Rect(100, 400, 120, 160),
            "You return to the living room, head buzzing with new questions.",
            self.go_to_living_room
        )

    def shift_bookshelf(self):
        if not self.inventory.has_item("Bookshelf Shifted"):
            self.inventory.append("Bookshelf Shifted")
            self.dialog_text = (
                "You tug the odd book. The bookshelf groans as if something behind it has shifted..."
            )
        else:
            self.dialog_text = "The book’s already been moved. Something’s different here now."

    def collect_book(self):
        if "Marked Book" not in self.inventory:
            self.inventory.append("Marked Book")
            self.dialog_text = "The message inside reads: 'Only the medallion reveals the truth.'"
        else:
            self.dialog_text = "You’ve already read this clue."

    def go_to_living_room(self):
        self.dialog_text = "You return to the living room, the weight of knowledge in your hands."
