from enum import Enum
import heapq

class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"
    IDLE = "IDLE"

class State(Enum):
    MOVING = 1
    NOT_MOVING = 0

class RequestType(Enum):
    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"


class Request:
    def __init__(self, floor : int, request_type : RequestType, direction : Direction):
        self.floor = floor
        self.request_type = request_type
        self.direction = direction
    
    def __lt__(self, other):
        return self.floor < other.floor


class Elevator:
    def __init__(self, elevator_id : str):
        self.id = elevator_id
        self.floor = 0
        self.direction = Direction.UP
        self.up_requests = []
        self.down_request = []
    
    
    def accept_up_request(self, request : Request):
        heapq.heappush(self.up_requests, (request.floor, request))
        
    def accept_down_request(self, request : Request):
        heapq.heappush(self.down_request, (-request.floor, request))     
    

    def run(self):
        while len(self.up_requests) > 0:
            floor, request = heapq.heappop(self.up_requests)

            if (elevator.floor != floor):
                print(f"Elevator {self.id} is moving to floor {floor}")
                self.floor = floor
                print(f"Elevator {self.id} has reached floor {floor}")

            if request.request_type == RequestType.INTERNAL:
                print(f"Opening door for internal people to walk out")
            elif request.request_type == RequestType.EXTERNAL:
                print(f"Opening door for external people to walk in")
            
            elevator.floor = floor
        

        elevator.direction = Direction.DOWN
        while len(self.down_request) > 0:
            floor, request = heapq.heappop(self.down_request)
            if (elevator.floor != floor):
                print(f"Elevator {self.id} is moving to floor {-floor}")
                self.floor = floor
                print(f"Elevator {self.id} has reached floor {-floor}")

            if request.request_type == RequestType.INTERNAL:
                print(f"Opening door for internal people to walk out")
            elif request.request_type == RequestType.EXTERNAL:
                print(f"Opening door for external people to walk in")
            
            elevator.floor = floor
        
        elevator.direction = Direction.IDLE

    

elevator = Elevator("A01")

request1 = Request(2, RequestType.EXTERNAL, Direction.UP)
request2 = Request(4, RequestType.EXTERNAL, Direction.DOWN)
request3 = Request(6, RequestType.INTERNAL, Direction.UP)
request4 = Request(0, RequestType.INTERNAL, Direction.DOWN)
request5 = Request(0, RequestType.EXTERNAL, Direction.DOWN)
request6 = Request(-1, RequestType.INTERNAL, Direction.DOWN)


elevator.accept_up_request(request1)
elevator.accept_up_request(request2)
elevator.accept_up_request(request3)

elevator.accept_down_request(request4)
elevator.accept_down_request(request5)
elevator.accept_down_request(request6)

elevator.run()
