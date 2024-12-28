
class Singleton:
    _instance = None

    @staticmethod
    def get_instance():
        if Singleton._instance == None:
            Singleton()
            
        return Singleton._instance

    def __init__(self):
        if Singleton._instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton._instance = self


s1 = Singleton.get_instance()
s2 = Singleton.get_instance()

class DB:
    _instance = None
    hashmap = {}

    @staticmethod
    def get_instance():
        if DB._instance == None:
            DB()
        return DB._instance

    def __init__(self):
        if DB._instance != None:
            raise Exception("This class is a singleton!")
        else:
            DB._instance = self

    def insert(self, key, value):
        DB.hashmap[key] = value
    
    def get(self, key):
        return DB.hashmap[key]

db1 = DB.get_instance()
db2 = DB.get_instance()
db1.insert("key1", "value1")
db2.insert("key2", "value2")
print(db2.get("key1"))
print(db1.get("key2"))
