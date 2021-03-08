import random


LEVELS=9


class Survivor:
    """
    """
    def __init__(self):
        self.curr_floor = random.randrange(LEVELS)
        self.waiting = True
    
    def call_elevator(self, requests_queue):
        requests_queue.append(self.curr_floor)
        print(f"I waiting for Elevator at {self.curr_floor} floor")

    def choose_destination(self, races_queue):
        self.destination = random.randrange(LEVELS)
        races_queue.append(self.destination)
        print(f"I, {self}, want to go to {self.destination} floor")
        
    def __repr__(self):
        return f'Survivor on {self.curr_floor!r}'
    
