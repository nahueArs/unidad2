import csv


class Fecha():
    __fechaPartido: str
    __idEquipoLocal: int
    __idEquipoVisitante: int
    __cantGolesEqLocal: int
    __cantGolesEqVisitante: int

    def __init__(self, fecha, idlocal, idvisitante, golLocal, golVisitante):
        self.__fechaPartido = fecha
        self.__idEquipoLocal = idlocal
        self.__idEquipoVisitante = idvisitante
        self.__cantGolesEqLocal = golLocal
        self.__cantGolesEqVisitante = golVisitante

    def __str__(self):
        return f"{self.__fechaPartido} , {self.__idEquipoLocal} , {self.__idEquipoVisitante} , {self.__idEquipoLocal} , {self.__cantGolesEqVisitante}"

    def getfecha(self):
        return self.__fechaPartido
    
    def getidlocal(self):
        return self.__idEquipoLocal
    
    def golLocal(self):
        return self.__cantGolesEqLocal
    def getgolvisitante(self):
        return self.__cantGolesEqVisitante
    def getidvisitante(self):
        return self.__idEquipoVisitante
    
    def golcon(self):
        return self.__cantGolesEqVisitante