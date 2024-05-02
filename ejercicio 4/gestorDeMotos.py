import csv
from claseConductor import *
from gestorDePedidos import *
from clasePedidos import *


class GestorMoto():
    __listado = list

    def __init__(self, listado=[]) -> None:
        self.__listado = listado

    def Carga_Motos(self):
        archivo = open(
            r"C:\Users\erica\OneDrive\Documents\Pythonfacultad\unidad 2\ejercicio 4\datosMotos.csv")
        reader = csv.reader(archivo, delimiter=",")
        bandera = True

        for i in reader:
            if bandera:
                bandera = False
            else:
                patente = i[0]
                marca = i[1]
                nya = i[2]
                km = float(i[3])
                obj = conductor(patente, marca, nya, km)
                self.__listado.append(obj)
        archivo.close()

    def muestra(self):
        for elemento in self.__listado:
            print(elemento)


    def mostrarConductor(self,patente):
        i=0
        while i< len(self.__listado) and self.__listado[i].getpatent().lower()!=patente:
            i=i+1
        if i<len(self.__listado):
            print(f"{self.__listado[i].getnombre()} , {self.__listado[i].getmarca()}")