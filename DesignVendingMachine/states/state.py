from abc import ABC, abstractmethod

class State(ABC):
    
    @abstractmethod
    def move_to_accept_money_state(self, vending_machine : 'VendingMachine'):
        pass

    @abstractmethod
    def insert_money(self, vending_machine : 'VendingMachine', money : int):
        pass

    @abstractmethod
    def select_product(self, vending_machine : 'VendingMachine', product_code : str):
        pass

    @abstractmethod
    def dispense_product(self, vending_machine : 'VendingMachine', product_code : str):
        pass

    @abstractmethod
    def cancel_transaction(self, vending_machine : 'VendingMachine'):
        pass

    @abstractmethod
    def refund_money(self, vending_machine : 'VendingMachine'):
        pass

