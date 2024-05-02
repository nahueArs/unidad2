# clase Cajas de ahorro
class CajaAhorro:
    __nrocuenta: str
    __cuil: str
    __apellido: str
    __nombre: str
    __saldo: float
# contructor

    def __init__(self, nro, cuil, apellido, nombre, saldo):
        self.__nrocuenta = nro
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__saldo = saldo
# metodo que muestra los datos

    def mostrarDatos(self):
        print(f"apellido:{self.__apellido} nombre:{self.__nombre}, cuil: {
              self.__cuil} numero de cuenta {self.__nrocuenta}, saldo :{round(self.__saldo, 2)}")
# Metodo que resuelve una extraccion de la caja de ahorro

    def extraer(self, importe):
        if importe > self.__saldo:
            print("error no fue posible la extraccion")
        if (self.__saldo > importe):
            self.__saldo -= importe
            print("extraccion exitosa")
# metodo de deposito

    def depositar(self, importe):
        if importe > 0:
            self.__saldo += importe
            print(f"nuevo importe {self.__saldo}")
        else:
            print("no ingreso dinero")
# metodo que valida el cuil ingresado

    def validarCUIL(self, cuil_Ingresado):
        cuil = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        validar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        calculo = 0
        for i in range(len(cuil_Ingresado)):
            if i in validar:
                calculo = calculo + (int(cuil_Ingresado[i])*cuil[i])
                print(f"({calculo})")
            if (i == "-"):
                pass

        calculo1 = calculo % 11
        calculo1 = calculo - (11 * calculo1)
        if (calculo1 == 0):
            calculo1 = 0
            self.__cuil = cuil_Ingresado+"0"
        if calculo1 >= 1:
            if ("20" in f"({cuil_Ingresado})"):
                self.__cuil = self.__cuil+"9"
            if ("27" in cuil_Ingresado):
                self.__cuil = self.__cuil+"4"
            if ("30" in cuil_Ingresado):
                calculo1 = 11-calculo1
                self.__cuil = self.__cuil+f"{calculo1}"
