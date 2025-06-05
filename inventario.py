class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_product(self, name, quantity):
        if name in self.inventory:
            raise ValueError("Producto ya existe.")
        if quantity <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        self.inventory[name] = quantity

    def remove_product(self, name):
        if name not in self.inventory:
            raise KeyError("El producto no existe en el inventario.")
        del self.inventory[name]

    def get_inventory(self):
        return dict(self.inventory)