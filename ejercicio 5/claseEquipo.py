import numpy as np
import csv


class Equipo():
    __id_Equipo: int
    __nombre: str
    __golesAFavor: int
    __golesEnContra: int
    __difGoles: int
    __puntos: int

    def __init__(self, id, nombre, gFavor, gContra, difGol, puntos):
        self.__id_Equipo = id
        self.__nombre = nombre
        self.__golesAFavor = gFavor
        self.__golesEnContra = gContra
        self.__difGoles = difGol
        self.__puntos = puntos

    def __str__(self):
        return f"{self.__id_Equipo} , {self.__nombre} , {self.__golesAFavor} , {self.__golesEnContra} , {self.__difGoles} , {self.__puntos}"


    def __gt__(self, other):
        if self.__puntos > other.__puntos:
            return self.__puntos > other.__puntos
        elif self.__difGoles>other.__difGoles:
            return self.__difGoles > other.__difGoles
        elif self.__puntos == other.__puntos:
            if self.__golesAFavor > other.__golesAFavor:
                return self.__golesAFavor > other.__golesAFavor
        
    
    def getIde(self):
        return self.__id_Equipo
    
    def getnombre(self):
        return self.__nombre
    
    def getgolesAFavor(self):
        return self.__golesAFavor
    
    def getgolesEnContra(self):
        return self.__golesEnContra
    
    def getdifGoles(self):
        return self.__difGoles
    
    def getpuntos(self):
        return self.__puntos
    
    def setgoless(self,gol):
        self.__golesAFavor=self.getgolesAFavor+gol
        
    def setpunto(self,puntos):
        self.__puntos=self.__puntos+puntos