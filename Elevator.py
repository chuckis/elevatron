# Лифт собственно

class Elevator:
    """ 
    """
    MAX_PASSENGERS = 5
    
    def __init__(self, level, passengers=0):
        self.level = level
        self.passengers = passengers
        self.is_free = True


    def add_passengers(n):
        return self.passengers.append(n)

    def find_nearest_call(self, current_level, pull):
        """
        """
        distances = []
        for level in pull:
            distances.append(abs(level - current_level))
        #print(distances)
        minimal_distance = min(distances)
        index_in_pull = distances.index(minimal_distance)
        destination = pull[index_in_pull]
        return destination
