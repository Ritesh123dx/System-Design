
class BalanceSheet:
    def __init__(self):
        self.balances = {}
    
    def add_user(self, new_user_id : str)-> None:
        user_ids = list(self.balances.keys())
        self.balances[new_user_id] = {}

        for user_id in user_ids:
            self.balances[user_id][new_user_id] = 0
            self.balances[new_user_id][user_id] = 0
        
    def add_equal_transaction(
        self, total_amount : int, payer_id : str, payee_ids : list[str]
        )-> None:
        
        individual_amt = total_amount//(len(payee_ids) + 1)

        for payee_id in payee_ids:
            self.balances[payee_id][payer_id] += individual_amt
            self.balances[payer_id][payee_id] -= individual_amt
    


    def add_unequal_transaction(
            self, payer_id : str,
            payee_ids : list[str], amts : list[int]
    )-> None:
        

        n = len(payee_ids)
        for i in range(n):
            payee_id = payee_ids[i]
            self.balances[payee_id][payer_id] += amts[i]
            self.balances[payer_id][payee_id] -= amts[i]   
            

    def print_balances(self, user_id : str) -> str:
        print(f"Balance for user id : {user_id}")

        user_ids = list(self.balances.keys())
        for u_id in user_ids:
            if user_id == u_id:
                continue

            amt = self.balances[user_id][u_id]
            if amt >= 0:
                print(f"Gives user {u_id} | Amt : {amt}")
            else:
                print(f"Gets from {u_id} | Amt : {-amt}")
    
    
            




