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

class Elevator(Controller):

    def __init__(self, area, elevators, floors, floorCall, elevatorNumber, reportFloor, openDoor, floorRequest, tripAmount, maintenanceNeeded):
        super().__init__(area, elevators, floors, floorCall)
        # this refers to which elevator is it (int)
        self.elevatorNumber = elevatorNumber
        # this refers to the floor the elevator is on (int)
        self.reportFloor = reportFloor
        # this reports door open or closed (boolean)
        self.openDoor = openDoor
        # this will take a floor request from the controller
        self.floorRequest = floorRequest
        # this will be a counter to track the number of trips (int, counter)
        self.tripAmount = tripAmount
        # this will track whether or not maintenance is needed at 100 tripAmount (Boolean). If true, elevator will not be operatable.
        self.maintenanceNeeded = maintenanceNeeded

    
class OutsidePanel(Controller):
    
    def __init__(self, area, elevators, floors, floorCall, floorNumber, upCall, downCall):
        super().__init__(area, elevators, floors, floorCall)
        # this is the floor the outside panel is on (int)
        self.floorNumber = floorNumber
        # this is if the panel calls for an elevator to go up (boolean)
        self.upCall = upCall
        # this is if the panel calls for an elevator to go down (boolean)
        self.downCall = downCall

class InsidePanel(Elevator):
    def __init__(self, area, elevators, floors, floorCall, elevatorNumber, reportFloor, openDoor, floorRequest, tripAmount, maintenanceNeeded, floorCalled):
        super().__init__(area, elevators, floors, floorCall, elevatorNumber, reportFloor, openDoor, floorRequest, tripAmount, maintenanceNeeded)
        # this will make a request to which floor the person inside wants to go to. It will send it to the controller
        self.floorCalled = floorCalled
