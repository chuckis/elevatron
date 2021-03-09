import random


LEVELS=9


class Survivor:
    """
    """
    def __init__(self):
        self.origin_floor = random.randrange(LEVELS)
        self.waiting = True
        self.current_floor = None
    
    def call_elevator(self):
        print(f"I waiting for Elevator at {self.origin_floor} floor")

    def choose_destination(self):
        self.destination = random.randrange(LEVELS)
        print(f"I, {self}, want to go to {self.destination} floor")
        return self.destination
        
    def __repr__(self):
        return f'Survivor on {self.origin_floor!r}'
    
