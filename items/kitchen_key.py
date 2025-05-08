from items.item import Item

class KitchenKey(Item):
    def __init__(self):
        super().__init__(
            name="Kitchen Key",
            description="A bent little key with a kitchen emblem on the bow.",
            can_use=True
        )

    def use(self, context=None):
        return "You unlock the pantry cabinet. Something skitters inside..."
