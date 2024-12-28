from abc import ABC, abstractmethod
from threading import Lock, RLock

class Publisher(ABC):
    @abstractmethod
    def add_subscriber(self, subscriber) -> None:
        pass

    @abstractmethod
    def remove_subscriber(self, subscriber) -> None:
        pass

    @abstractmethod
    def notify(self, message) -> None:
        pass


class Store(Publisher):

    def __init__(self):
        self.subscribers = []
        self.lock = Lock()

    def add_subscriber(self, subscriber) -> None:
        with self.lock:
            if subscriber not in self.subscribers:
                self.subscribers.append(subscriber)
    
    def remove_subscriber(self, subscriber) -> None:
        with self.lock:
            if subscriber in self.subscribers:
                self.subscribers.remove(subscriber)
        
    def notify(self, message) -> None:
        for subscriber in self.subscribers:
            subscriber.notify(message)


class Subscriber(ABC):

    @abstractmethod
    def notify(self, message) -> None:
        pass

    @abstractmethod
    def subscribe(self, publisher) -> None:
        pass



class Customer(Subscriber):
    def __init__(self, name):
        self.id = id(self)
        self.name = name
        self.subscriptions = []
    
    def notify(self, message):
        print(f"Customer {self.name} received message: {message}")

    def subscribe(self, store):
        if store not in self.subscriptions:
            store.add_subscriber(self)
            self.subscriptions.append(store)




customer1 = Customer("John")
customer2 = Customer("Jane")
customer3 = Customer("Alice")
customer4 = Customer("Bob")

store1 = Store()
store2 = Store()

customer1.subscribe(store1)
customer2.subscribe(store1)
customer3.subscribe(store2)
customer4.subscribe(store2)

store1.notify("New product arrived at store1")
store2.notify("New product arrived at store2")
