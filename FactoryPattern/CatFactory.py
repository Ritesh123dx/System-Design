from AnimalFactory import AnimalFactory
from Cat import Cat

class CatFactory(AnimalFactory): 
    def create_animal(self):
        return Cat()