import time
import random
from Elevator import Elevator
from Survivor import Survivor


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
        self.survivors = survivors
        self.pull_of_requests = []
        self.survivors_destinations = []
    
    def run(self):
        
        for survivor in range(self.survivors):
            survivor = Survivor()
            time.sleep(random.randrange(1, 3))
            survivor.call_elevator(self.pull_of_requests)
            time.sleep(1)
            survivor.choose_destination(self.survivors_destinations)
            
if __name__=='__main__':

    el = Elevator(9, 0)
    sim = Simulator(el, 5)
    sim.run()

    

    
