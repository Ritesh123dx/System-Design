from abc import ABC

class ATMProcesssor(ABC):

    def __init__(self, atm_processor : 'ATMProcesssor'):
        self.next_atm_processor = atm_processor

    def withdraw(self, atm, amount : int) -> None:
        print("Withdrawing amount: ", amount)
        if self.next_atm_processor != None:
            self.next_atm_processor.withdraw(atm, amount)
      


class TwoThousandProcessor(ATMProcesssor):
    def __init__(self, atm_processor : ATMProcesssor):
        super().__init__(atm_processor)

    def withdraw(self, atm, amount : int) -> None:
        required_notes = amount // ATM.DENOMINATION_2000
        notes_used = min(required_notes, atm.get_two_thousand_notes())

        if notes_used > 0:
            print(f"Dispensing {notes_used} notes of {ATM.DENOMINATION_2000}")
            print(f"Amount generated: {notes_used * ATM.DENOMINATION_2000}")
            remaining_amount = amount - notes_used * ATM.DENOMINATION_2000
            atm.deduct_two_thousand_notes(notes_used)            

            if remaining_amount > 0:
                super().withdraw(atm, remaining_amount)
        else:
            super().withdraw(atm, amount)    

class FiveHundredProcessor(ATMProcesssor):
    def __init__(self, atm_processor : ATMProcesssor):
        super().__init__(atm_processor)

    def withdraw(self, atm, amount : int) -> None:
        required_notes = amount // ATM.DENOMINATION_500
        notes_used = min(required_notes, atm.get_five_hundred_notes())

        if notes_used > 0:
            print(f"Dispensing {notes_used} notes of {ATM.DENOMINATION_500}")
            print(f"Amount generated: {notes_used * ATM.DENOMINATION_500}")
            remaining_amount = amount - notes_used * ATM.DENOMINATION_500
            atm.deduct_five_hundred_notes(notes_used)            

            if remaining_amount > 0:
                super().withdraw(atm, remaining_amount)
        else:
            super().withdraw(atm, amount) 


class HundredProcessor(ATMProcesssor):
    def __init__(self, atm_processor : ATMProcesssor):
        super().__init__(atm_processor)

    def withdraw(self, atm, amount : int) -> None:
        required_notes = amount // ATM.DENOMINATION_100
        notes_used = min(required_notes, atm.get_one_hundred_notes())

        if notes_used > 0:
            print(f"Dispensing {notes_used} notes of {ATM.DENOMINATION_100}")
            print(f"Amount generated: {notes_used * ATM.DENOMINATION_100}")
            remaining_amount = amount - notes_used * ATM.DENOMINATION_100
            atm.deduct_one_hundred_notes(notes_used)            

            if remaining_amount > 0:
                super().withdraw(atm, remaining_amount)
        else:
            super().withdraw(atm, amount) 


class ATM:

    DENOMINATION_2000 = 2000
    DENOMINATION_500 = 500
    DENOMINATION_100 = 100

    def __init__(self):
        self.two_thousand_notes = 0
        self.five_hundred_notes = 0
        self.one_hundred_notes = 0
    
    def add_two_thousand_notes(self, notes : int):
        self.two_thousand_notes += notes

    def add_five_hundred_notes(self, notes : int):
        self.five_hundred_notes += notes

    def add_one_hundred_notes(self, notes : int):
        self.one_hundred_notes += notes
    
    def get_two_thousand_notes(self) -> int:
        return self.two_thousand_notes
    
    def get_five_hundred_notes(self) -> int:
        return self.five_hundred_notes
    
    def get_one_hundred_notes(self) -> int:
        return self.one_hundred_notes
    
    def deduct_two_thousand_notes(self, notes : int):
        self.two_thousand_notes -= notes
    
    def deduct_five_hundred_notes(self, notes : int):
        self.five_hundred_notes -= notes
    
    def deduct_one_hundred_notes(self, notes : int):
        self.one_hundred_notes -= notes
    
    def get_total_amount(self) -> int:
        return self.two_thousand_notes * ATM.DENOMINATION_2000 + self.five_hundred_notes * ATM.DENOMINATION_500 + self.one_hundred_notes * ATM.DENOMINATION_100
    
atm = ATM()
atm.add_two_thousand_notes(2)
atm.add_five_hundred_notes(2)
atm.add_one_hundred_notes(5)
print(atm.get_total_amount())

atm_processor = ATMProcesssor(TwoThousandProcessor(FiveHundredProcessor(HundredProcessor(None))))
atm_processor.withdraw(atm, 3700)