from states.state import State
# from vending_machine import VendingMachine
from typing_extensions import override



class IdealState(State):

    @override
    def move_to_accept_money_state(self, vending_machine : 'VendingMachine'):
        vending_machine.set_state(AcceptMoneyState())

    @override
    def insert_money(self, vending_machine : 'VendingMachine', money : int):
        raise Exception("Machine is in Ideal state, please click the button to initialise machine")

    @override
    def select_product(self, vending_machine : 'VendingMachine', product_code : str):
        raise Exception("Machine is in Ideal state, please click the button to initialise machine")

    @override
    def dispense_product(self, vending_machine : 'VendingMachine', product_code : str):
        raise Exception("Machine is in Ideal state, please click the button to initialise machine")


    @override
    def cancel_transaction(self, vending_machine : 'VendingMachine'):
        raise Exception("Machine is in Ideal state, please click the button to initialise machine")


    @override
    def refund_money(self, vending_machine : 'VendingMachine'):
        raise Exception("Machine is in Ideal state, please click the button to initialise machine")


class SelectItemState(State):

    def move_to_accept_money_state(self, vending_machine: 'VendingMachine'):
        raise Exception("Machine is in Select Item state")

    def insert_money(self, vending_machine: 'VendingMachine', money: int):
        raise Exception("Machine is in Select Item state")

    def select_product(self, vending_machine, product_code: str):
        product = vending_machine.get_product(product_code)

        if product == None:
            vending_machine.set_state(SelectItemState())
            print("Product Code entered is wrong")
            return

        quantity = vending_machine.get_product_quantity(product_code)
        price = product.price

        if quantity == 0:
            vending_machine.set_state(SelectItemState())
            print("Product is not available")
            return

        if vending_machine.balance < price:
            vending_machine.set_state(SelectItemState())
            print("Insufficient balance")
            return

        vending_machine.set_state(DispenseItemState())
        vending_machine.state.dispense_product(vending_machine, product_code)

    def dispense_product(self, vending_machine: 'VendingMachine', product_code: str):
        raise Exception("Machine is in Select Item state")

    def cancel_transaction(self, vending_machine):
        balance = vending_machine.balance
        vending_machine.balance = 0
        print(f"Transaction cancelled, returning {balance}")
        vending_machine.set_state(IdealState())

    def refund_money(self, vending_machine):
        raise Exception("Machine is in Select Item state")


class AcceptMoneyState(State):

    def move_to_accept_money_state(self, vending_machine: 'VendingMachine'):
        raise Exception("Machine is already in accept money state")

    def insert_money(self, vending_machine: 'VendingMachine', money: int):
        vending_machine.add_money(money)
        vending_machine.set_state(SelectItemState())

    def select_product(self, vending_machine: 'VendingMachine', product_code: str):
        raise Exception("Machine is in accept money state")

    def dispense_product(self, vending_machine: 'VendingMachine', product_code: str):
        raise Exception("Machine is in accept money state")

    def cancel_transaction(self, vending_machine: 'VendingMachine'):
        raise Exception("Machine is in accept money state")

    def refund_money(self, vending_machine: 'VendingMachine'):
        raise Exception("Machine is in accept money state")


class DispenseItemState(State):

    @override
    def move_to_accept_money_state(self, vending_machine: 'VendingMachine'):
        raise Exception("Machine is in Dispense Item state")

    @override
    def insert_money(self, vending_machine: 'VendingMachine', money: int):
        raise Exception("Machine is in Dispense Item state")

    @override
    def select_product(self, vending_machine: 'VendingMachine', product_code: str):
        raise Exception("Machine is in Dispense Item state")

    @override
    def dispense_product(self, vending_machine: 'VendingMachine', product_code: str):
        product = vending_machine.get_product(product_code)
        quantity = vending_machine.get_product_quantity(product_code)
        vending_machine.update_product_quantity(product_code, quantity - 1)

        remaining_balance = vending_machine.balance - product.price

        if remaining_balance > 0:
            self.refund_money(vending_machine, remaining_balance)

        print(f"Dispensing {product.name}")
        vending_machine.balance = 0
        vending_machine.set_state(IdealState())

    @override
    def cancel_transaction(self, vending_machine: 'VendingMachine'):
        raise Exception("Machine is in Dispense Item state, cannot cancel transactions")

    @override
    def refund_money(self, vending_machine: 'VendingMachine', remaining_balance: int):
        print(f"Refunding {remaining_balance}")
        vending_machine.balance = 0
        vending_machine.set_state(IdealState())





