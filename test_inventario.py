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

# Versión que falla
from inventario import InventoryManager
import pytest

def test_agregar_producto_fail():
    inv = InventoryManager()
    inv.add_product("Manzanas", 10)
    # Se espera que el inventario esté vacío para fallar
    assert inv.get_inventory() == {}

def test_agregar_producto_duplicado_fail():
    inv = InventoryManager()
    inv.add_product("Peras", 5)
    # No usamos raises, para que falle al lanzar ValueError
    inv.add_product("Peras", 3)

def test_agregar_producto_cantidad_invalida_fail():
    inv = InventoryManager()
    # Usamos cantidad válida para que no se lance ValueError y falle el test
    with pytest.raises(ValueError):
        inv.add_product("Uvas", 1)

def test_eliminar_producto_existente_fail():
    inv = InventoryManager()
    inv.add_product("Sandía", 4)
    # No eliminamos el producto, pero sí esperamos que no esté en el inventario
    assert "Sandía" not in inv.get_inventory()

def test_eliminar_producto_inexistente_fail():
    inv = InventoryManager()
    # Eliminamos un producto existente en vez de uno inexistente para que falle
    inv.add_product("Durazno", 2)
    with pytest.raises(KeyError):
        inv.remove_product("Durazno")

def test_consultar_inventario_fail():
    inv = InventoryManager()
    inv.add_product("Kiwi", 6)
    inv.add_product("Banano", 12)
    # Se cambia la cantidad esperada para que la comparación falle
    assert inv.get_inventory() == {"Kiwi": 6, "Banano": 10}
