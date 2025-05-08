from items.item import Item

class Candle(Item):
    def __init__(self):
        super().__init__(
            name="Candle",
            description="A stub of wax with a blackened wick. Still lights.",
            can_use=True
        )

    def use(self, context=None):
        return "You light the candle and hold it to the library wall. Hidden writing appears in glowing ink."
