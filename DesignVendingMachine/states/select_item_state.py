# from states.state import State
# # from states.select_item_state import SelectItemState
# from states.idle_state import IdealState, DispenseItemState
# # from vending_machine import VendingMachine
#
# # class SelectItemState(State):
# #
# #     def move_to_accept_money_state(self, vending_machine : 'VendingMachine'):
# #         raise Exception("Machine is in Select Item state")
# #
# #     def insert_money(self, vending_machine : 'VendingMachine', money : int):
# #         raise Exception("Machine is in Select Item state")
# #
# #     def select_product(self, vending_machine, product_code : str):
# #         product = vending_machine.get_product(product_code)
# #         quantity = vending_machine.get_product_quantity(product_code)
# #         price = product.price
# #
# #         if quantity == 0:
# #             vending_machine.set_state(SelectItemState())
# #             print("Product is not available or insufficient balance")
# #             return
# #
# #         if vending_machine.get_balance() < price:
# #             vending_machine.set_state(SelectItemState())
# #             print("Insufficient balance")
# #             return
# #
# #         vending_machine.set_state(DispenseItemState())
# #         vending_machine.state.dispense_product(vending_machine, product_code)
# #
# #
# #
# #
# #     def dispense_product(self, vending_machine : 'VendingMachine', product_code : str):
# #         raise Exception("Machine is in Select Item state")
# #
# #     def cancel_transaction(self, vending_machine):
# #         balance = vending_machine.balance
# #         vending_machine.balance = 0
# #         print(f"Transaction cancelled, returning {balance}")
# #         vending_machine.set_state(IdealState())
# #
# #     def refund_money(self, vending_machine):
# #         raise Exception("Machine is in Select Item state")
# #
