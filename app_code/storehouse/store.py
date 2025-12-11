from .errors import ProductNotFound
import logging

# UTF-8 лог
logging.basicConfig(
    filename='inventory.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

class Product:
    """Тауар класы"""
    def __init__(self, name, code, weight):
        self.name = name
        self.code = code
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.code}) - {self.weight} кг"

class Movement:
    """Тауар қозғалысы"""
    def __init__(self, product_code, quantity, direction):
        self.product_code = product_code
        self.quantity = quantity
        self.direction = direction  # 'in' немесе 'out'

class InventoryRepository:
    """Қойма репозиториясы"""
    def __init__(self):
        self.products = []
        self.movements = []

    def add_product(self, product):
        self.products.append(product)
        logging.info(f"Product added: {product}")

    def get_product(self, code):
        for p in self.products:
            if p.code == code:
                return p
        raise ProductNotFound(f"Тауар табылмады: {code}")

    def add_movement(self, movement):
        self.movements.append(movement)
        logging.info(f"Movement added: {movement.__dict__}")

    def get_stock(self):
        stock = {p.code: 0 for p in self.products}
        for m in self.movements:
            if m.direction == 'in':
                stock[m.product_code] += m.quantity
            elif m.direction == 'out':
                stock[m.product_code] -= m.quantity
        result = []
        for p in self.products:
            result.append({
                'name': p.name,
                'code': p.code,
                'weight': p.weight,
                'quantity': stock[p.code]
            })
        return result

class InventoryService:
    """Қойма қызметі"""
    def __init__(self):
        self.repo = InventoryRepository()

    def add_product(self, name, code, weight):
        p = Product(name, code, weight)
        self.repo.add_product(p)

    def register_movement(self, code, qty, direction):
        self.repo.get_product(code)  # жоқ болса ProductNotFound
        m = Movement(code, qty, direction)
        self.repo.add_movement(m)

    def get_stock(self):
        return self.repo.get_stock()

    def get_movements(self):
        return self.repo.movements
