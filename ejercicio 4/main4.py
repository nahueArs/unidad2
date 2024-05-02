from clasePedidos import *
from claseConductor import *
from gestorDeMotos import *
from gestorDePedidos import *

if __name__ == "__main__":
    opcion = int(input("ingrese opcion \n op1:carga de motos \n op2; carga pedidos \n op3: agregar pedidos \n op4: tiempo real de pedidos \n op5: tiempo de conductor\n op6:comision total \n op 0 : fin \n\n"))
    while opcion != 0:
        if opcion == 1:
            gestorMotos = GestorMoto()
            gestorMotos.Carga_Motos()
            gestorMotos.muestra()
        elif opcion == 2:
            gestorPedido = gestorPedidos()
            gestorPedido.cargar_Pedidos()
            gestorPedido.mostrar()
        elif opcion == 3:
            gestorPedido.cargar_nuevo()
            gestorPedido.ordenar_gestor()
            gestorPedido.mostrar()
        elif opcion == 4:
            gestorPedido.Modifica_Tiempo()
            gestorPedido.mostrar()
        elif opcion == 5:
            gestorPedido.InformarConductor(gestorMotos)
        elif opcion == 6:
            patente= input("ingrese patene : \n")
            gestorPedido.comisiones(patente)
        opcion = int(input("ingrese opcion \n op1:carga de motos \n op2; carga pedidos \n op3: agregar pedidos \n op4: tiempo real de pedidos \n op5: tiempo de conductor\n op6:comision total \n op 0 : fin \n\n"))
