from abc import ABC, abstractmethod

class MathStrategy(ABC):
    @abstractmethod
    def calculate(self, a, b) -> int:
        pass

class AddStrategy(MathStrategy):
    def calculate(self, a, b) -> int:
        return a + b
    
class SubtractStrategy(MathStrategy):
    def calculate(self, a, b) -> int:
        return a - b

class MultiplyStrategy(MathStrategy):
    def calculate(self, a, b) -> int:
        return a * b


class MathContext:
    def __init__(self, strategy: MathStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: MathStrategy):
        self.strategy = strategy
    
    def calculate(self, a, b) -> int:
        return self.strategy.calculate(a, b)


add_context = MathContext(AddStrategy())
print(add_context.calculate(10, 5))