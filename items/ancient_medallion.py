from items.item import Item

class AncientMedallion(Item):
    def __init__(self):
        super().__init__(
            name="Ancient Medallion",
            description="A heavy medallion etched with cryptic runes.",
            can_use=True
        )

    def use(self, context=None):
        return "The medallion fits into the ritual box slot... something shifts behind the wall."
