from abc import ABC, abstractmethod

class Button(ABC):
    
    @abstractmethod
    def press(self) -> None:
        pass

    @abstractmethod
    def button_status(self) -> bool:
        pass