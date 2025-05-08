from items.item import Item

class SafeCode(Item):
    def __init__(self):
        super().__init__(
            name="Safe Code",
            description="Faded numbers scribbled on a torn slip of paper.",
            can_use=True
        )

    def use(self, context=None):
        return "You enter the code behind the portrait. The safe unlocks with a low mechanical hum."
