import csv
from claseConductor import *


class pedidos():
    __patentemoto: str
    __idPedido: int
    __comida: str
    __tiempoentrega: str
    __treal: int
    __precio: float

    def __init__(self, patente, id, comida, Tentrega , real, precio):
        self.__patentemoto = patente
        self.__idPedido = id
        self.__comida = comida
        self.__tiempoentrega = Tentrega
        self.__treal = real
        self.__precio = precio

    def __str__(self) -> str:
        return (f"{self.__patentemoto} ,{self.__idPedido} , {self.__comida} , {self.__tiempoentrega} , {self.__tiempoentrega} , {self.__precio}")

    def __lt__(self, other):
        return (self.__patentemoto < other.__patentemoto)

    def cambiarTiempo(self):
        tiempo = input("ingrese tiempo")
        self.__treal = tiempo
        print("tiempo cambiado \n")

    def getpatente(self):
        return self.__patentemoto

    def getid(self):
        return (self.__idPedido)
    def gettiempo(self):
        return self.__tiempoentrega
    def gettreal(self):
        return (self.__treal)
    def getprecio(self):
        return self.__precio


