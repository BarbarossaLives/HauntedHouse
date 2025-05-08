# inventory.py

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if not self.has_item(item.name):
            self.items.append(item)
            print(f"Added '{item.name}' to inventory.")
        else:
            print(f"You already have '{item.name}'.")

    def has_item(self, item_name):
        return any(item.name == item_name for item in self.items)

    def get_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def use_item(self, item_name, context=None):
        item = self.get_item(item_name)
        if item:
            return item.use(context)
        return f"You don’t have '{item_name}' in your inventory."

    def list_items(self):
        return [item.name for item in self.items]
