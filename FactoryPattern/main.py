from CatFactory import CatFactory
from DogFactory import DogFactory


cat_factory = CatFactory()
dog_factory = DogFactory()

cat = cat_factory.create_animal()
dog = dog_factory.create_animal()

cat.speak()
dog.speak()


