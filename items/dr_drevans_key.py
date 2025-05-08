from items.item import Item

class DrDrevansOldKey(Item):
    def __init__(self):
        super().__init__(
            name="Dr. Drevan's Old Key",
            description="An old key with initials scratched into the head.",
            can_use=True
        )

    def use(self, context=None):
        return "You unlock the cabinet in the Wine Cellar with a satisfying *click*."
