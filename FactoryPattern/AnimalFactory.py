from abc import ABC, abstractmethod

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass
