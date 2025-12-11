import unittest
from storehouse.store import InventoryService, ProductNotFound

class TestInventory(unittest.TestCase):

    def setUp(self):
        """Әр тестке жаңа InventoryService жасау"""
        self.service = InventoryService()
        self.service.add_product("Тауар1", "001", 10)
        self.service.add_product("Тауар2", "002", 20)

    def test_add_product(self):
        """Тауар қосу жұмыс істейді ме"""
        stock = self.service.get_stock()
        codes = [p['code'] for p in stock]
        self.assertIn("001", codes)
        self.assertIn("002", codes)

    def test_register_movement_in(self):
        """Қоймаға тауар келу"""
        self.service.register_movement("001", 5, "in")
        stock = self.service.get_stock()
        for item in stock:
            if item['code'] == "001":
                self.assertEqual(item['quantity'], 5)

    def test_register_movement_out(self):
        """Қоймадан тауар шығару"""
        self.service.register_movement("002", 10, "in")
        self.service.register_movement("002", 4, "out")
        stock = self.service.get_stock()
        for item in stock:
            if item['code'] == "002":
                self.assertEqual(item['quantity'], 6)

    def test_product_not_found(self):
        """Тауар жоқ болса қате шығу"""
        with self.assertRaises(ProductNotFound):
            self.service.register_movement("999", 1, "in")

if __name__ == "__main__":
    unittest.main()
