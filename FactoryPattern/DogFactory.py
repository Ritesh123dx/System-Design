from AnimalFactory import AnimalFactory
from Dog import Dog

class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()