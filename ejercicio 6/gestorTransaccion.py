import csv
from claseTransaccion import *
class gestorTransaccion():
    __listado = list
    
    def __init__(self) -> None:
        self.__listado = []
        
    def cargarTransaccion(self):
        archi=open(r"C:\Users\erica\OneDrive\Documents\Pythonfacultad\unidad 2\ejercicio 6\transaccionesBilletera.csv")
        reader=csv.reader(archi, delimiter=",")
        for i in reader:
            t=transaccion(i[0],i[1],float(i[2]),i[3])
            self.__listado.append(t)
    
    def mostrar(self):
        for elemento in self.__listado:
            print(elemento)
            
    def gettipo(self,cvu):
        i=0
        while i< len(self.__listado) and self.__listado[i].getcvu()!=cvu:
            i=i+1
        if i < len(self.__listado):
            return self.__listado[i].gettr()
        else: 
            print("error")
    
    def gettransaccion(self,cvu):
        i=0
        while i< len(self.__listado) and self.__listado[i].getcvu()!=cvu:
            i=i+1
        if i < len(self.__listado):
            return self.__listado[i].getimp()
        else: 
            print("error")