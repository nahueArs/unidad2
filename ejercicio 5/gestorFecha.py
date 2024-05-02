import csv
from claseEquipo import *
from claseFecha import *
from gestorEquipo import *
class Gestor_Fechas():
    __listado = list

    def __init__(self, lista=[]) -> None:
        self.__listado = lista

    def carga_Fechas(self):
        bandera = True
        archivo = open(
            r"C:\Users\erica\OneDrive\Documents\Pythonfacultad\unidad 2\ejercicio 5\fechaFutbol.csv")
        reader = csv.reader(archivo, delimiter=",")
        for fila in reader:
            if bandera:
                bandera = False
            else:
                print("entra")
                fecha = fila[0]
                idL = int(fila[1])
                idV = int(fila[2])
                golL = int(fila[3])
                golV = int(fila[4])
                c = Fecha(fecha, idL, idV, golL, golV)
                self.__listado.append(c)
        archivo.close()

    def mostrarFechas(self):
        for fecha in self.__listado:
            print(fecha)
            
    def mostrar_Equipo(self, id,nombre,gestorEquipo):
        i=0
        print(f"Equipo {nombre}")
        for i in  self.__listado:
            golfav=0
            golcon=0
            difgol=0
            if i.getidlocal()==id:
                golfav=golfav+i.golLocal()
                golcon=golcon+i.getgolvisitante()
                difgol=difgol+(golfav-golcon)
                if golfav>golcon:
                    gestorEquipo.setpuntos(id,3)
                elif golfav==golcon:
                    gestorEquipo.setpuntos(id,1)
            elif i.getidvisitante()==id:
                golcon=golcon+i.golLocal()
                golfav=golfav+i.getgolvisitante()
                difgol=difgol+(golfav-golcon)
                if golfav>golcon:
                    gestorEquipo.setpuntos(id,3)
                elif golfav==golcon:
                    gestorEquipo.setpuntos(id,1)
            else:
                pass
            print("FECHA          GOL A FAVOR        GOL EN CONTRA       DIF GOL      PUNTOS")
            print(f" {i.getfecha()}        {golfav}          {golcon}          {difgol}           {gestorEquipo.getpuntos(id)}")    
            