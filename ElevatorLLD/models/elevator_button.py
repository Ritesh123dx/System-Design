
from models.button import Button


class ElevatorButton(Button):
    def __init__(self, value : int):
        self.value = value
        self.is_pressed = False
    
    def press(self) -> None:
        self.is_pressed = True
    
    def button_status(self) -> bool:
        return self.is_pressed