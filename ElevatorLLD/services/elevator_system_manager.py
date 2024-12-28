from models.elevator import Elevator
from collections import deque
from models.request import Request
from enums.direction import Direction

class ElevatorSystemManager:
    def __init__(self, elevator_list : list[Elevator]):
        self.elevator_list = elevator_list
    
    def request_elevator(self, request : Request) -> Elevator:
        elevator = self.get_elevator_controller(request.source_floor_no, request.direction)
        
        if request.direction == Direction.DOWN:
            elevator.accept_down_request(request)
        else:
            elevator.accept_up_request(request)

        return elevator
    
    def get_elevator_controller(self, source_floor_no : int, direction : Direction) -> Elevator:
        nearest_distance = float('inf')
        nearest_elevator = None
        
        #find the nearest elevator
        for elevator in self.elevator_list:
            if elevator.direction == direction or elevator.direction == Direction.IDLE:
                distance = abs(elevator.floor - source_floor_no)
                if nearest_distance > distance:
                    nearest_distance = distance
                    nearest_elevator = elevator
        
        if nearest_elevator != None:
            return nearest_elevator
        
        #if all the elevators are going in the opposite direction, then choose the one with leaset amount of requests
        min_requests = float('inf')
        for elevator in self.elevator_list:
            total_requests = len(elevator.up_requests) + len(elevator.down_requests)
            if min_requests > total_requests:
                min_requests = total_requests
                nearest_elevator = elevator
        
        return nearest_elevator

                



    

    