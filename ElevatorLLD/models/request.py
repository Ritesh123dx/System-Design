from enums.request_type import RequestType
from enums.direction import Direction

class Request:
    def __init__(self, request_type : RequestType, direction: Direction, source_floor_no : int, destination_floor_no : int):
        self.request_type = request_type
        self.direction = direction
        self.source_floor_no = source_floor_no
        self.destination_floor_no = destination_floor_no
    
    def __lt__(self, other):
        return self.source_floor_no < other.source_floor_no