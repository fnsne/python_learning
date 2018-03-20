class Vehicle:
    def __init__(self, name, engine):
        self.__name = name
        self.__engine = engine

    def getName(self):
        return self.__name

    def getEngine(self):
        return self.__engine

class Homda(Vehicle):
    def __init__(self, name, engine, electric):
        super().__init__(name, engine)
        self.__electric = electric

    def getEngine(self):
        return  "super Homda Engine"

#test
def test():
    carA = Homda("homda", "EEEEEngine", "elec")
    print(carA.getName())
    print(carA.getEngine())

if __name__ == "__main__":
    test()
