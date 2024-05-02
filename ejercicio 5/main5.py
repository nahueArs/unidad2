from claseEquipo import *
from claseFecha import *
from gestorFecha import *
from gestorEquipo import *

if __name__ == "__main__":
    opcion = int(input("op 1:cargar equipos \n op2: cargar fechas \n op3:informe Equipo \n op4 : actualizar fecha \n op5: ordenar tabla de posiciones\n op 6 generar archivo con la tabla de posiciones \n op 0; salir \n"))
    while opcion != 0:
        if opcion == 1:
            Eq= Gestor_Equipo()
            Eq.carga()
            Eq.mostrar()
        elif opcion == 2:
            Fe = Gestor_Fechas()
            Fe.carga_Fechas()
            Fe.mostrarFechas()
        elif opcion == 3:
            nombre=input ("nombre de equipo : ")
            id=Eq.buscaid(nombre)
            Fe.mostrar_Equipo(id,nombre,Eq)
        elif opcion==4 :
            Eq.mostrar()
        elif opcion == 5:
            Eq.actualiza_Posiciones()
            Eq.mostrar()
        elif opcion == 6:
            Eq.crea_archivo()
        opcion = int(input("op 1:cargar equipos \n op2: cargar fechas \n op3:informe Equipo \n op4 : actualizar fecha \n op5: ordenar tabla de posiciones\n op 6 generar archivo con la tabla de posiciones \n op 0; salir \n"))
