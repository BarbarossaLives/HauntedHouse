import pygame
from items.inventory import Inventory
from room_manager import RoomManager



# Import all rooms from the rooms package
from rooms.foyer import Foyer
from rooms.kitchen import Kitchen
from rooms.living_room import LivingRoom
from rooms.library import Library
from rooms.dining_room import DiningRoom
from rooms.wine_cellar import WineCellar
from rooms.furnace_room import FurnaceRoom
from rooms.secret_room import SecretRoom
#from rooms.stairs_room import StairsRoom
from rooms.upstairs_stairs_room import UpstairsStairsRoom
#from rooms.upstairs_hallway import UpstairsHallway
from rooms.master_bedroom import MasterBedroom
from rooms.guest_bedroom import GuestBedroom
from rooms.childs_bedroom import ChildsBedroom
from rooms.bathroom import Bathroom

# Initialize Pygame
pygame.init()
font = pygame.font.SysFont('Arial', 20)
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Haunted House")
clock = pygame.time.Clock()

# Set up inventory and room manager
inventory = Inventory()
manager = RoomManager(inventory)

# Register all room instances
manager.register_room("foyer", Foyer(inventory, manager, font))
manager.register_room("kitchen", Kitchen(inventory, manager, font))
manager.register_room("living_room", LivingRoom(inventory, manager, font))
manager.register_room("library", Library(inventory, manager,font))
manager.register_room("dining_room", DiningRoom(inventory, manager, font))
manager.register_room("wine_cellar", WineCellar(inventory, manager, font))
manager.register_room("furnace_room", FurnaceRoom(inventory, manager, font))
manager.register_room("secret_room", SecretRoom(inventory, manager, font))
#manager.register_room("stairs", StairsRoom(inventory, manager, font))
#manager.register_room("upstairs_stairs", UpstairsStairsRoom(inventory, manager, font))
#manager.register_room("upstairs", UpstairsHallway(inventory, manager, font))
manager.register_room("master", MasterBedroom(inventory, manager, font))
manager.register_room("guest", GuestBedroom(inventory, manager, font))
manager.register_room("childs", ChildsBedroom(inventory, manager, font))
manager.register_room("bathroom", Bathroom(inventory, manager, font))

# Set the starting room
manager.set_current_room("foyer") 

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            manager.get_current_room().handle_event(event)

    # Update the current room
    manager.get_current_room().update()

    # Draw everything
    screen.fill((0, 0, 0))
    manager.get_current_room().draw(screen)
    pygame.display.flip()

    # Maintain 60 FPS
    clock.tick(60)

pygame.quit()
