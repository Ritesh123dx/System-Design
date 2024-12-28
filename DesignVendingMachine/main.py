from vending_machine import VendingMachine
from states.idle_state import AcceptMoneyState
# from states.dispense_item_state import DispenseItemState
from states.idle_state import IdealState

vending_machine = VendingMachine()
vending_machine.fill_inventory()


#Buy Pepsi
vending_machine.set_state(AcceptMoneyState())
state = vending_machine.state
state.insert_money(vending_machine, 35)

state = vending_machine.state
state.select_product(vending_machine, "201")



# Buy Coke
vending_machine.set_state(AcceptMoneyState())
state = vending_machine.state
state.insert_money(vending_machine, 35)

state = vending_machine.state
state.select_product(vending_machine, "100")


