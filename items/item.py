class Item:
    def __init__(self, name, description="", can_use=False, image=None):
        """
        Base class for all inventory items.
        
        Args:
            name (str): Name of the item
            description (str): What it is or what it hints at
            can_use (bool): If the item can be used actively (default False)
            image (str): Path to image file (optional, for UI)
        """
        self.name = name
        self.description = description
        self.can_use = can_use
        self.image = image  # Optional icon for inventory display

    def use(self, context=None):
        """
        Called when the player attempts to use the item.
        Override this method in subclasses.
        
        Args:
            context (any): Optional game state or room data
        
        Returns:
            str: Dialog result from using the item
        """
        if self.can_use:
            return f"You use the {self.name}."
        else:
            return f"The {self.name} can't be used like that."
