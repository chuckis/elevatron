import time
import random
from Elevator import Elevator
from Survivor import Survivor


class Simulator:
    """
    """
    def __init__(self, elevator, survivors):
        self.elevator = elevator
        self.survivors = survivors
        self.pull_of_requests = set()
        self.survivors_destinations = set()
    
    def run(self):
        
        for survivor in range(self.survivors):
            survivor = Survivor()
            time.sleep(random.randrange(1, 3))
            survivor.call_elevator()
            self.pull_of_requests.add(survivor.origin_floor) #maybe not origin, but current(?)
            time.sleep(1)
            survivor.choose_destination()
            self.survivors_destinations.add(survivor.destination)


if __name__=='__main__':

    el = Elevator()
    sim = Simulator(el, 5)
    sim.run()

    

    
