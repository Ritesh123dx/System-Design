from balance_sheet import BalanceSheet
from user import User
from split_enum import SplitType

class Group:
    def __init__(self):
        self.users = []
        self.balance_sheet = BalanceSheet()

    def add_user(self, new_user : User) -> None:
        is_present = False
        for user in self.users:
            if user.id == new_user.id:
                is_present = True
                break
        
        if is_present == False:
            self.users.append(new_user)
            self.balance_sheet.add_user(new_user.id)

    def make_transaction(
            self, total_amount: int, split_type : SplitType, 
            payer_id : str, payee_ids : list[str],
            un_equal_splits : list[int] = None
    ):
        
        if split_type == SplitType.EQUAL:
            self.balance_sheet.add_equal_transaction(total_amount, payer_id, payee_ids)
        else:
            self.balance_sheet.add_unequal_transaction(payer_id, payee_ids, un_equal_splits)


    def show_balance(self, user : User)-> None:
        user_id = user.id
        self.balance_sheet.print_balances(user_id)
    
