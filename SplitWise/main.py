from user import User
from group import Group
from split_enum import SplitType

'''
Entities:
1. User
2. Group
3. BalanceSheet
4. BalanceSheetService

Each Group will maintain a BalanceSheet of its users.
'''

user1 = User("Ritesh Gupta", "ritesh123dx@gmail.com")
user2 = User("Rohan Paul", "rohan@gmail.com")
user3 = User("Rahul Kumar", "rahul@gmail.com")
user4 = User("Roman Singh", "roman@gmail.com")

group = Group()
group.add_user(user1)
group.add_user(user2)
group.add_user(user3)
group.add_user(user4)



group.make_transaction(1000, SplitType.EQUAL, user1.id, [user2.id, user3.id])
group.show_balance(user1)
group.show_balance(user2)

group.make_transaction(1000, SplitType.UNEQUAL, user2.id, [user1.id, user3.id, user4.id], [333, 530, 267])
group.show_balance(user1)
group.show_balance(user2)