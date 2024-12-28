# from states.state import State
# from states.idle_state import SelectItemState
from vending_machine import VendingMachine

# class AcceptMoneyState(State):
#
#     def move_to_accept_money_state(self, vending_machine : 'VendingMachine'):
#         raise Exception("Machine is already in accept money state")
#
#     def insert_money(self, vending_machine : 'VendingMachine', money : int):
#         vending_machine.add_money(money)
#         vending_machine.set_state(SelectItemState())
#
#     def select_product(self, vending_machine : 'VendingMachine', product_code : str):
#         raise Exception("Machine is in accept money state")
#
#     def dispense_product(self, vending_machine : 'VendingMachine', product_code : str):
#         raise Exception("Machine is in accept money state")
#
#     def cancel_transaction(self, vending_machine : 'VendingMachine'):
#         raise Exception("Machine is in accept money state")
#
#     def refund_money(self, vending_machine : 'VendingMachine'):
#         raise Exception("Machine is in accept money state")
