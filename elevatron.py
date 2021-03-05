import time
import random


SURVIVORS=10
LEVELS=9


class Elevator:
    """ 
    Лифт:
    знает:
    СВОБОДЕН ИЛИ ЗАНЯТ
    ЕДЕТ ИЛИ СТОИТ
    Э вызова из пулла вызовов, выбирается Ближайший...
    Э назначения
    кол-во Ч, но не больше макс.кол-ва
    passengers: int

    """
    MAX_PASSENGERS = 5
    
    def __init__(self, level, passengers=0):
        self.level = level
        self.passengers = passengers

    def add_passengers(n):
        return self.passengers.append(n)

    def find_nearest_call(self, current_level, pull):
        """
        находит ближайший этаж среди нескольких из пулла вызовов
        """
        distances = []
        for level in pull:
            distances.append(abs(level - current_level))
        #print(distances)
        minimal_distance = min(distances)
        index_in_pull = distances.index(minimal_distance)
        destination = pull[index_in_pull]
        return destination

class Survivor:
    """
     Чел, знает:
     свой Э(таж), куда едет тоже знает
    """
    def __init__(self):
        self.floor = random.randrange(LEVELS)
        self.destination = random.randrange(LEVELS)
        self.waiting = True
    def call_elevator(self, floor):
        print(f"I wanna go to {floor} floor")
        
    def __repr__(self):
        return f'Survivor on {self.floor!r}, goes to {self.destination!r}'
    

class Simulator:
    """
    Симулятор:
    знает: 
    на каком Этаже(Э) Лифт(Л)
    сколько Человек(Ч) в Л и на Э-х
    сколько пассажиров доставлено
    Симулятор явл. главным объектом, содержит состояние приложения.
    пулл вызовов(из кот. выбирается ближайший Э и пул уменьшается)
    Имеет методы инит ...
    инит: случайное колво этажей с случайным колвом Ч
    """
    def __init__(self, elevator, survivors):
        self.elevator = elevator
        self.survivors = [] #instances of Survivor
        self.pull_of_requests = []
    
    def run(self):
        
        for survivor in range(SURVIVORS):
            survivor = Survivor()
            time.sleep(random.randrange(1, 3))
            self.pull_of_requests.append(survivor.floor)
            survivor.call_elevator(survivor.destination)
            
            #TODO здесь вот лифт везет куда надо
            call = self.elevator.find_nearest_call(self.elevator.level, self.pull_of_requests)
            print(survivor.floor, survivor.destination, self.pull_of_requests, call)

if __name__=='__main__':

    el = Elevator(9, 0)
    sim = Simulator(el, SURVIVORS)
    sim.run()

    

    
