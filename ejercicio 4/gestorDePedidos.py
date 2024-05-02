from clasePedidos import *
from claseConductor import *

import csv


class gestorPedidos():
    __lista = list

    def __init__(self, lista=[]) -> None:
        self.__lista = lista
        


    def cargar_Pedidos(self):
        archi = open(
            r"C:\Users\erica\OneDrive\Documents\Pythonfacultad\unidad 2\ejercicio 4\datos.Pedidos.csv")
        reader = csv.reader(archi, delimiter=",")
        bandera = True
        for i in reader:
            if bandera:
                bandera = False
            else:
                patente = i[0]
                id = i[1]
                comida = i[2]
                tiempo = i[3]
                treal = int(i[4])
                precio = float(i[5])
                c = pedidos(patente, id, comida, tiempo,treal, precio)
                self.__lista.append(c)
        archi.close()

    def mostrar(self):
        print("entra")
        for elemento in self.__lista:
            print(elemento)

    def cargar_nuevo(self):
        i=0
        patente = input("ingrese patente :")
        while i < len(self.__lista) and self.__lista[i].getpatente()!=patente:
            i=i+1
        if i < len(self.__lista):
            id = int(input("ingrese identifivador : \n"))
            comida = input("comida : \n")
            tiempo = input("ingrese tiempo \n")
            tiempoReal=int(input ("ingrese tiempo real: \n"))
            precio = float(input("ingrese precio : \n"))
            c = pedidos(patente, id, comida, tiempo,tiempoReal, precio)
            self.__lista.append(c)
        else:
            print("Error")

    def Modifica_Tiempo(self):
        i = 0
        patente = input("ingrese patente :")
        id = int(input("ingrese identifivador :"))
        while i < len(self.__lista) and self.__lista[i].getpatente() != patente and  self.__lista[i].getid() != id :
                i = i+1
        if i < len(self.__lista):
            self.__lista[i].cambiarTiempo()
        else:
            print("patente no encontrada \n")


    def ordenar_gestor(self):
        self.__lista = sorted(self.__lista)
        
    def InformarConductor(self,gestor):
        i = 0
        sum = 0
        patente = input("patente que desea buscar : \n")
        while i < len(self.__lista) and (self.__lista[i].getpatente() != patente):
            i = i+1
        if i < len(self.__lista):
            sum=sum+int(self.__lista[i].gettreal())
            gestor.mostrarConductor(patente)
        print(f"{sum}")


    def comisiones(self,patente):
        i=0
        sumador = 0
        print(f"id pedido      tiempo estimado        tiempo real      precio")
        for i in range (len(self.__lista)):
            if self.__lista[i].getpatente().lower()== patente:
                print(f"{int(self.__lista[i].getid())}  ,  {self.__lista[i].gettiempo()}  ,  {int(
                      self.__lista[i].gettreal())}  ,  {float(self.__lista[i].getprecio())} \n")
                sumador = sumador+float(self.__lista[i].getprecio())
        print(f"total{sumador} \n")
        print(f"total de comision {sumador*0.20}")
