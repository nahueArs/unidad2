import csv


class conductor():
    __patente: str
    __marca: str
    __nyA: str
    __km: float

    def __init__(self, patent, marca, nya, km):
        self.__patente = patent
        self.__marca = marca
        self.__nyA = nya
        self.__km = km

    def __str__(self) -> str:
        return f"{self.__patente} , {self.__patente} , {self.__nyA} , {self.__marca}"
    
    def getpatent(self): 
        return self.__patente
    
    def getmarca(self):
        return self.__marca
    
    def getnombre(self):
        return self.__nyA
    
    def getkm (self):
        return self.__km

    def mostrarConductor(self):
        print(f"{self.__nyA} , {self.__patente} , {self.__marca} , {self.__km}")
