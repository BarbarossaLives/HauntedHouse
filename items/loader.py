# items/loader.py
from items.dr_drevans_key import DrDrevansOldKey
from items.ancient_medallion import AncientMedallion
from items.safe_code import SafeCode
from items.kitchen_key import KitchenKey
from items.candle import Candle

def load_all_items():
    return {
        "Dr. Drevan's Old Key": DrDrevansOldKey(),
        "Ancient Medallion": AncientMedallion(),
        "Safe Code": SafeCode(),
        "Kitchen Key": KitchenKey(),
        "Candle": Candle(),
    }
