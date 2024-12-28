from button import Button

class InnerButton(Button):
    def __init__(self, floor_no: int):
        self.floor = floor_no
        self.is_pressed = False
    
    def press(self) -> None:
        self.is_pressed = True
    
    def is_pressed(self) -> bool:
        return self.is_pressed
    