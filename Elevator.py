# Лифт собственно
import random

class Elevator:
    """ 
    """
    MAX_PASSENGERS = 5
    
    def __init__(self):
        self.current_level = random.randrange(9)
        self.passengers = []
        self.is_free = True


    def add_passenger(survivor):
        return self.passengers.append(survivor)


    def make_race(self, a_floor, b_floor):  #TODO
        self.is_free = False
        pass

    def find_nearest_call(self, pull):
        """
        """
        distances = []
        for level in pull:
            distances.append(abs(level - self.current_level))
        minimal_distance = min(distances)
        index_in_pull = distances.index(minimal_distance)
        destination = pull[index_in_pull]
        return destination
