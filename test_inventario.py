from inventario import InventoryManager
import pytest

def test_agregar_producto():
    inv = InventoryManager()
    inv.add_product("Manzanas", 10)
    assert inv.get_inventory() == {"Manzanas": 10}

def test_agregar_producto_duplicado():
    inv = InventoryManager()
    inv.add_product("Peras", 5)
    with pytest.raises(ValueError):
        inv.add_product("Peras", 3)

def test_agregar_producto_cantidad_invalida():
    inv = InventoryManager()
    with pytest.raises(ValueError):
        inv.add_product("Uvas", 0)

def test_eliminar_producto_existente():
    inv = InventoryManager()
    inv.add_product("Sandía", 4)
    inv.remove_product("Sandía")
    assert "Sandía" not in inv.get_inventory()

def test_eliminar_producto_inexistente():
    inv = InventoryManager()
    with pytest.raises(KeyError):
        inv.remove_product("Durazno")

def test_consultar_inventario():
    inv = InventoryManager()
    inv.add_product("Kiwi", 6)
    inv.add_product("Banano", 12)
    assert inv.get_inventory() == {"Kiwi": 6, "Banano": 12}