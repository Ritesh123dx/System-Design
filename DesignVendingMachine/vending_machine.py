from states.idle_state import IdealState
from states.state import State
from products.coke import Coke
from products.pepsi import Pepsi

class VendingMachine:
    def __init__(self):
        self.state = IdealState()
        self.product_map = {}
        self.quantity_map = {}
        self.balance = 0
        
    def set_state(self, state : State):
        self.state = state
    
    def get_product(self, product_code):
        return self.product_map.get(product_code, None)
    
    def add_money(self, money : int):
        self.balance += money   
    
    def get_product_quantity(self, product_code : str):
        return self.quantity_map.get(product_code, None)
    
    def update_product_quantity(self, product_code : str, quantity : int):
        self.quantity_map[product_code] = quantity
    
    def fill_inventory(self):
        coke = Coke("100", 25)
        pepsi = Pepsi("201", 35)
        self.product_map[coke.code] = coke
        self.product_map[pepsi.code] = pepsi
        self.quantity_map[coke.code] = 12
        self.quantity_map[pepsi.code] = 15
    
