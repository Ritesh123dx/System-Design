from enums.request_type import RequestType
from models.request import Request
from enums.direction import Direction
from enums.state import State
from models.elevator_button import ElevatorButton
from services.elevator_system_manager import ElevatorSystemManager
from models.elevator import Elevator


button_list = [ElevatorButton(i) for i in range(0, 6)]
elevator_1 = Elevator("A01", 0, Direction.IDLE, State.NOT_MOVING, button_list)
elevator_2 = Elevator("A02", 0, Direction.IDLE, State.NOT_MOVING, button_list)

elevator_manager = ElevatorSystemManager([elevator_1, elevator_2])

request1 = Request(RequestType.EXTERNAL, Direction.UP, 1, 1)
request2 = Request(RequestType.INTERNAL, Direction.UP, 1, 4)

elevator = elevator_manager.request_elevator(request1)
elevator.accept_up_request(request2)
elevator.run()


request3 = Request(RequestType.EXTERNAL, Direction.DOWN, 5, 5)
request4 = Request(RequestType.INTERNAL, Direction.DOWN, 5, 0)

elevator = elevator_manager.request_elevator(request3)
elevator.accept_down_request(request4)
elevator.run()