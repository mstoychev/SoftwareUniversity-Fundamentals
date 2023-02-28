class Inventory:
    def __init__(self, capacity: int):
        self.__capacity = int(capacity)
        self.items = []
        self.filled = 0

    def add_item(self, item: str):
        if self.__capacity > self.filled:
            self.filled += 1
            self.items.append(str(item))
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        capacity_left = Inventory.get_capacity(self) - self.filled
        return f"Items: {', '.join(self.items)}.\nCapacity left: {capacity_left}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
