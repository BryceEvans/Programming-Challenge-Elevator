class Controller:

    def __init__(self, area, elevators, floors, floorCall):
        # this may refer to the area of the building this controller and set of elevators is located
        self.area = area
        # this may refer to the elevators in the area
        self.elevators = elevators
        # this may refer to the number of floors in the building or floors the area serves (like in a skyscraper where a set of elevators may only serve a portion of the floors)
        self.floors = floors
        # this will take a floor call from a request
        self.floorCall

    def take_floorCall(self):
        # this function takes a call from panel (either inside or outside)
        pass #ToDo

    def find_elevator(self):
        # this function finds the nearest elevator
        pass #ToDo

    def stop_elevator(self):
        # this function stops an elevator at a request
        pass #ToDo

    

class Elevator(Controller):

    def __init__(self, area, elevators, floors, floorCall, elevatorNumber, reportFloor, openDoor, doorObstruction, floorRequest, tripAmount, maintenanceNeeded):
        super().__init__(area, elevators, floors, floorCall)
        # this refers to which elevator is it (int)
        self.elevatorNumber = elevatorNumber
        # this refers to the floor the elevator is on (int)
        self.reportFloor = reportFloor
        # this reports door open or closed (boolean)
        self.openDoor = openDoor
        # this will sense if anything obstructs the door--to open it if needed (boolean)
        self.doorObstruction = doorObstruction
        # this will take a floor request from the controller
        self.floorRequest = floorRequest
        # this will be a counter to track the number of trips (int, counter)
        self.tripAmount = tripAmount
        # this will track whether or not maintenance is needed at 100 tripAmount (Boolean). If true, elevator will not be operatable.
        self.maintenanceNeeded = maintenanceNeeded

    def move_to_request(self):
        # this function will move the elevator to requested floor
        pass #ToDo

    def open_door(self):
        # this function will open the door
        pass #ToDo

    def close_door(self):
        # this function will close the door after a timeout from opening if there is no obstruction
        pass #ToDo

    def count_trips(self):
        # this will count trips up to 100
        pass #ToDo
    
    def put_in_maintenance(self):
        # this will put elevator into maintenance mode, making it inoperable after 100 trips.
        pass #ToDo


class OutsidePanel(Controller):
    
    def __init__(self, area, elevators, floors, floorCall, floorNumber, upCall, downCall):
        super().__init__(area, elevators, floors, floorCall)
        # this is the floor the outside panel is on (int)
        self.floorNumber = floorNumber
        # this is if the panel calls for an elevator to go up (boolean)
        self.upCall = upCall
        # this is if the panel calls for an elevator to go down (boolean)
        self.downCall = downCall

    def up_request(self):
        # this function sends a request to the controller to move up from floor it's on
        pass #ToDo

    def down_request(self):
        # this function sends a request to the controller to move down from floor it's on
        pass #ToDo

class InsidePanel(Elevator):
    def __init__(self, area, elevators, floors, floorCall, elevatorNumber, reportFloor, openDoor, doorObstruction, floorRequest, tripAmount, maintenanceNeeded, floorCalled):
        super().__init__(area, elevators, floors, floorCall, elevatorNumber, reportFloor, openDoor, doorObstruction, floorRequest, tripAmount, maintenanceNeeded)
        # this will make a request to which floor the person inside wants to go to. It will send it to the controller
        self.floorCalled = floorCalled

    def request_to_floor(self):
        # this function sends a request from the elevator it is in to the controller to move to the requested floor
        pass #ToDo

    # I suppose on this panel, you could have other controls like closeDoor, openDoor, callForHelp (or soundAlarm) or something. But for the sake of time, I'll forego those options.