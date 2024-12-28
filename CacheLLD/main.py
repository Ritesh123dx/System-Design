from typing import TypeVar, Generic

K = TypeVar('K')
V = TypeVar('V')

class CacheEntity(Generic[K, V]):
    def __init__(self, key : K, value : V):
        self.key = key
        self.value = value


class CacheNode(Generic[K, V]):
    def __init__(self, entity : CacheEntity[K, V]):
        self.entity = entity
        self.next = None
        self.prev = None
    
class DoubleLinkedList(Generic[K, V]):
    def __init__(self):
        self.head = CacheNode(None)
        self.tail = CacheNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_to_head(self, node : CacheNode[K, V]):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def remove_node(self, node : CacheNode[K, V]):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
    
    def move_to_head(self, node : CacheNode[K, V]):
        self.remove_node(node)
        self.add_to_head(node)

    def get_least_recently_used(self) -> CacheNode[K, V]:
        return self.tail.prev

class LRUEvictionPolicy(Generic[K, V]):
    def __init__(self):
        pass

    def evict(self):
        pass

    def update(self, key : K):
        pass

    def get_least_recently_used(self) -> K:
        pass


class Cache(Generic[K, V]):
    def __init__(self):
        pass

    def put(self, key : K, value: V):
        pass

    def get(self, key : K) -> V | None:
        pass

    def remove(self, key : K):
        pass