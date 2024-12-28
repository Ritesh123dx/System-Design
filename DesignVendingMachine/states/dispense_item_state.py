# from typing_extensions import override
#
# from states.idle_state import IdealState
# from states.state import State


# class DispenseItemState(State):
#
#     @override
#     def move_to_accept_money_state(self, vending_machine : 'VendingMachine'):
#         raise Exception("Machine is in Dispense Item state")
#
#     @override
#     def insert_money(self, vending_machine : 'VendingMachine', money : int):
#         raise Exception("Machine is in Dispense Item state")
#
#     @override
#     def select_product(self, vending_machine : 'VendingMachine', product_code : str):
#         raise Exception("Machine is in Dispense Item state")
#
#     @override
#     def dispense_product(self, vending_machine : 'VendingMachine', product_code : str):
#         product = vending_machine.get_product(product_code)
#         quantity = vending_machine.get_product_quantity(product_code)
#         vending_machine.update_product_quantity(product_code, quantity - 1)
#
#         remaining_balance = vending_machine.balance - product.price
#
#         if remaining_balance > 0:
#             self.refund_money(vending_machine, remaining_balance)
#
#         print(f"Dispensing {product.name}")
#         vending_machine.balance = 0
#         vending_machine.set_state(IdealState())
#
#     @override
#     def cancel_transaction(self, vending_machine : 'VendingMachine'):
#         raise Exception("Machine is in Dispense Item state, cannot cancel transactions")
#
#     @override
#     def refund_money(self, vending_machine : 'VendingMachine', remaining_balance : int):
#         print(f"Refunding {remaining_balance}")
#         vending_machine.balance = 0
#         vending_machine.set_state(IdealState())
#
#
