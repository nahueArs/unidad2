from gestorTransaccion import *
from gestorCuentas import *
from claseCuenta import *

if __name__ == "__main__":
    print ("***MENU*** \n")
    opcion = int(input("op 1:cargar transacciones \n op2: cargar cuentas  \n op 3: Informar DNI \n op 4: Actualizar Porcentaje Anual \n op 5: Realizar transaccion e informar \n op 6: crear archivo \nop 0; salir \n"))
    while opcion != 0:
        if opcion == 1:
            Gt= gestorTransaccion()
            Gt.cargarTransaccion()
            Gt.mostrar()
        if opcion == 2:
            Gc= gestorCuentas(2)
            Gc.crear()
            Gc.mostrar()
        if opcion ==3:
            dni=input("ingrese dni : \n")
            Gc.informe(dni)
        if opcion == 4:
            Gc.actualizar()
            Gc.mostrar()
            print(Cuenta.getporcentaje())
        if opcion == 5:
            cvu=input("ingrese cvu : \n")
            Gc.buscarcvu(cvu,Gt)
        if opcion == 6:
            Gc.crearArchivo()
        opcion = int(input("op 1:cargar transacciones \n op2: cargar cuentas  \n op 3: Informar DNI \n op 4: Actualizar Porcentaje Anual \n op 5: Realizar transaccion e informar \n op 6: crear archivo \nop 0; salir \n"))