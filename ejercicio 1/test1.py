from cajaAhorro import *



def test():
    nro_cuenta = input("ingrese numero de cuenta : ")
    nombre = input("nombre : ")
    apellido = input("apellido : ")
    cuil = input("cuil : ")
    saldo = 0
    caja = CajaAhorro(nro_cuenta, cuil, apellido, nombre, saldo)
    caja.mostrarDatos()
    importe = 1000
    caja.validarCUIL(cuil)
    caja.depositar(importe)
    #c = ManejadorCajaAhorro()
    #c.agregarCaja(caja)
    
    #c.mostrarDatos()
