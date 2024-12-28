from enums.direction import Direction
from enums.state import State
from models.button import Button
from models.request import Request
from enums.request_type import RequestType
import heapq

class Elevator:
    def __init__(self, elevator_id : str, floor_no: int, direction: Direction, state : State, buttons : list[Button]):
        self.id = elevator_id
        self.floor = floor_no
        self.direction = direction
        self.state = state
        self.buttons = buttons
        self.up_requests = []
        self.down_requests = []
    
    def accept_up_request(self, request : Request):
        if request.direction == Direction.UP:
            heapq.heappush(self.up_requests, request)
    
    def accept_down_request(self, request : Request):
        if request.direction == Direction.DOWN:
            heapq.heappush(self.down_requests, request)

    
    def run(self):
        if self.direction == Direction.IDLE or self.direction == Direction.UP:
            self.perform_up_request()
            self.perform_down_request()
        else:
            self.perform_down_request()
            self.perform_up_request()


    def perform_up_request(self):
        self.direction = Direction.UP
        self.state = State.MOVING

        while len(self.up_requests) > 0:
            request = heapq.heappop(self.up_requests)
            floor = request.destination_floor_no
            print(f"{self.id} Going from {self.floor} to {floor}")
            self.floor = floor
            print(f"{self.id} Reached floor {floor}")
        
        self.direction = Direction.IDLE
        self.state = State.NOT_MOVING

    def perform_down_request(self):
        self.direction = Direction.DOWN
        self.state = State.MOVING

        while len(self.down_requests) > 0:
            request = heapq.heappop(self.down_requests)
            floor = request.destination_floor_no
            print(f"{self.id} Going from {self.floor} to {floor}")
            self.floor = floor
            print(f"{self.id} Reached floor {floor}")
        
        self.direction = Direction.IDLE
        self.state = State.NOT_MOVING

    