# Clase manejador de cajas de ahorro



class ManejadorCajaAhorro:
    __cajas: list

    def __init__(self):
        self.__cajas = []
# metodo que agrega cajas a la lsita

    def agregarCaja(self, caja):
        self.__cajas.append(caja)
# metodo que muestra los datos de la lista

    def mostrarDatos(self):
        for caja in self.__cajas:
            caja.mostrarDatos()
