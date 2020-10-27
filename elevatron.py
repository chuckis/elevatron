
SURVIVORS=100
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

    def find_destination(self, current_level, pull):
        """
        находит ближайший этаж среди нескольких из пулла вызовов
        """
        distances = []
        for level in pull:
            distances.append(abs(level - current_level))
        print(distances)
        minimal_distance = min(distances)
        index_in_pull = distances.index(minimal_distance)
        destination = pull[index_in_pull]
        return destination
    pass

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
    def __init__():
        pass

    pass

if __name__=='__main__':

    pull=[2, 3, 5, 15]
    elev1 = Elevator(3, 1)
    print(elev1.find_destination(elev1.level, pull))

    
