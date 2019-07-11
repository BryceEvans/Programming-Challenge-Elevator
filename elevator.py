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

    def __init__(self, area, elevators, floors, floorCall, reportFloor, openDoor, floorRequest, tripAmount, maintenanceNeeded):
        super().__init__(area, elevators, floors, floorCall)
        # this refers to the floor the elevator is on (int)
        self.reportFloor = reportFloor
        # this reports door open or closed (boolean)
        self.openDoor = openDoor
        #
        self.floorRequest = floorRequest
        # this will be a counter to track the number of trips (int, counter)
        self.tripAmount = tripAmount
        # this will track whether or not maintenance is needed at 100 tripAmount (Boolean). If true, elevator will not be operatable.
        self.maintenanceNeeded = maintenanceNeeded

    
