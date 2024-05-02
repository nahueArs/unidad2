import numpy as np
import csv
from claseCuenta import *
class gestorCuentas():
    __array:np.ndarray
    __dimension:int
    __cantidad:int
    
    def __init__(self,dimension):
        self.__array = np.empty(dimension, dtype=Cuenta)
        self.__dimension = dimension
        self.__cantidad = 0
    
    def crear(self):
        archi=open(r"C:\Users\erica\OneDrive\Documents\Pythonfacultad\unidad 2\ejercicio 6\cuentasBilletera.csv")
        reader = csv.reader(archi, delimiter=",")
        for i in reader:
            c=Cuenta(i[0],i[1],i[2],i[3],i[4],i[5])
            self.agregar(c)
        archi.close()
        
    def agregar(self,cuenta):
    
        if self.__cantidad < self.__dimension:
            self.__array[self.__cantidad] = cuenta
            self.__cantidad = self.__cantidad + 1
        else: 
            print("No hay espacio")
    
    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__array[i].muestra())
    
    def informe(self,dni):
        i=0
        while i < self.__cantidad and self.__array[i].getdni().lower()!=dni.lower():
            i=i+1
        if i < self.__cantidad:
            print(self.__array[i].muestra())
        else :
            print("error")
    
    @classmethod
    def actualizar(cls):
        porcentaje= float(input("Actualizar porcentaje : "))
        Cuenta.porcentajeRendimiento(porcentaje)
        
    def actualizarSaldo(self):
        valor=0
        for i in range(self.__array):
            valor=self.__array[i].getsaldo()*self.__array[i].getporcentaje()
            self.__array[i].setsaldo(valor)
            valor=0
    
    def buscarcvu(self, cvu, gestortransaccion):
        cuenta_encontrada = None
        for cuenta in self.__array:
            if cuenta.getcvu() == cvu:
                cuenta_encontrada = cuenta
                break
        
        if cuenta_encontrada:
            print(f"Saldo actual: {cuenta_encontrada.getsaldo()}")
            tipo_transaccion = gestortransaccion.gettipo(cvu)
            if tipo_transaccion == "D":
                transaccion = gestortransaccion.gettransaccion(cvu)
                print("Realizando transacción...")
                cuenta_encontrada.setsaldo(float(float(cuenta_encontrada.getsaldo()) - float(transaccion)))
                print("Transacción realizada.")
                print(f"Nuevo saldo: {cuenta_encontrada.getsaldo()}")
            elif tipo_transaccion == "C":
                print("Usted ha realizado un crédito.")
        else:
            print("Error: No se encontró ninguna cuenta con el CVU proporcionado.")
    def crearArchivo(self):
        archi=open("archivo.csv","w")
        for i in range(self.__cantidad):
            archi.write(f"{self.__array[i].getdni()},{self.__array[i].getnombre()},{self.__array[i].getapellido()},{self.__array[i].getcvu()},{self.__array[i].getsaldo()},{Cuenta.porcentajeRendimient}\n")
        archi.close()
