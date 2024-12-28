from elevator import Elevator, Request, Direction
import heapq


class ElevatorManager:
    def __init__(self, elevator : Elevator):
        self.elevator = elevator
        self.up_requests = []
        self.down_requests = []

    def accept_up_request(self, request : Request):
        if request.direction == Direction.UP:
            heapq.heappush(self.up_requests, request)
    
    def accept_down_request(self, request : Request):
        if request.direction == Direction.DOWN:
            heapq.heappush(self.down_requests, request)
    
    def run(self):
        pass
