from claseEquipo import *
from gestorFecha import *
class Gestor_Equipo():
    __arreglo = list

    def __init__(self, lista=[]) -> None:
        self.__arreglo = lista

    def carga(self):
        bandera = True
        archi = open(
            r"C:\Users\erica\OneDrive\Documents\Pythonfacultad\unidad 2\ejercicio 5\equipos2024.csv")
        reader = csv.reader(archi, delimiter=",")
        for iterador in reader:
            if bandera:
                bandera = False
            else:
                id = int(iterador[0])
                nombre = iterador[1]
                golfav = iterador[2]
                golcontra = int(iterador[3])
                difgol = int(iterador[4])
                pts = int(iterador[5])
                c = Equipo(id, nombre, golfav, golcontra, difgol, pts)
                self.__arreglo.append(c)

    def mostrar(self):
        for listado in self.__arreglo:
            print(listado)

    def actualiza_Posiciones(self):
        self.__arreglo.sort()
    def crea_archivo(self):
        archi = open("actualizacionTablaPosiciones.csv", "a+")
        for i in range(len(self.__arreglo)):
            archi.writelines(str(self.__arreglo[i]) + "\n")
            
    def buscaid(self,nombre):
        i=0
        while i < len(self.__arreglo) and self.__arreglo[i].getnombre() !=nombre:
            i=i+1
        if i < len(self.__arreglo):
            return self.__arreglo[i].getIde()
        else: 
            print("error")
    def getpuntos(self,id):
        i=0
        while i < len(self.__arreglo) and self.__arreglo[i].getIde()!=id:
            i=i+1
        if i < len(self.__arreglo):
            return self.__arreglo[i].getpuntos()
        else: 
            print("error")
    def setpuntos(self,id,puntos):
        i=0
        while i < len(self.__arreglo) and self.__arreglo[i].getIde()!=id:
            i=i+1
        if i < len(self.__arreglo):
            return self.__arreglo[i].setpunto(puntos)
        else: 
            print("error")

