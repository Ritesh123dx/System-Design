from elevator import Elevator, Request, Direction, RequestType

class ElevatorSystemManager:
    def __init__(self):
        self.request_queue = []
        self.elevator_managers = []

    def add_elevator(self, elevator : Elevator):
        self.elevator_managers.append(elevator)

    def request_elevator(self, floor : int, request_type : RequestType, direction : Direction):
        request = Request(floor, request_type, direction)
        self.request_queue.append(request)

    def run():
        pass

    
