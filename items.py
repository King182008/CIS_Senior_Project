class Item:
    def __init__(self, name, price=0):
        self.name = name
        self.price = price

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "type": "Item"
        }


class Weapon(Item):
    def __init__(self, name, price=0, damage=0):
        super().__init__(name, price)
        self.damage = damage

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "damage": self.damage,
            "type": "Weapon"
        }


# ---------- helpers ----------
def is_weapon(item):
    return isinstance(item, Weapon)