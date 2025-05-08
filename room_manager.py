
class RoomManager:
    def __init__(self, inventory):
        self.inventory = inventory
        self.rooms = {}
        self.current_room = None

    def register_room(self, room_id, room_instance):
        """Adds a room to the manager by name or ID."""
        self.rooms[room_id] = room_instance

    def set_current_room(self, room_id):
        """Switches to the specified room."""
        if room_id in self.rooms:
            self.current_room = self.rooms[room_id]
            print(f"Entered room: {self.current_room.name}")
        else:
            print(f"Room '{room_id}' not found.")

    def get_current_room(self):
        return self.current_room
