class farmacia:
    __list1: list

    def __init__(self):
        self.__list1 = []

    def crear(self):
        f = 5
        c = 7

        for i in range(f):
            fila = []
            for j in range(c):
                fila.append(0)
            self.__list1.append(fila)

    def llenar(self):
        x = int(input("dia : "))
        while x != -1:
            y = int(input(" sucursal"))
            importe = float(input("importe "))
            self.__list1[y][x] += importe
            x = int(input("dia : "))

    def informe(self, sucursal):
        sum = 0
        semana = 7
        for i in semana:
            sum = sum+self.__list1[sucursal][i]
        print(f"total recaudado por la sucursal{sucursal} fue de {sum}")

    def diaSemana(self, opc):
        maximporte = -1
        for i in self.__list1:
            if self.__list1[i][opc] > maximporte:
                maximporte = self.__list1[i][opc]
                aux = i
        print(f"la sucursal que mas facturo el dia {
              opc} fue la sucursal {aux}")

    def minSemana(self):
        min = 9999999999
        aux: int
        aux2: int
        for i in 5:
            for j in 7:
                if self.__list1[i][j] < min:
                    min = self.__list1[i][j]
                    aux = i
                    aux2 = j
        print(f" la sucursal que menos vendio fue {
              i} en el dia{j} un total de {min}")

    def totalSemanal(self):
        sum = 0
        for i in 5:
            for j in 7:
                sum += self.__list1[i][j]
        print(f"total semanal {sum}")


if __name__ == "__main__":
    print("opcion 1: Ingrese datos \n  opcion 2: ingrese sucursal a informar \n opcion 3: Dia de semana a informar \n opcion 4: Menor fscuracion en la semana \n opcion 5: Total semanal \n opcion 0 para salir")
    opcion = int(input("opcion..."))
    c = farmacia()
    c.crear()
    while opcion != 0:
        if opcion == 1:
            c.llenar()
        if opcion == 2:
            sucursal = int(input("ingrese numero de sucursal"))
            c.informe(sucursal)
        if opcion == 3:
            sucursal = int(input("ingrese dia de semana "))
            opcion = int(input("opcion..."))
            c.diaSemana(opcion)
        if opcion == 4:
            sucursal = int(input("ingrese dia de semana "))
        c.minSemana()
        if (opcion == 5):
            c.totalSemanal()
        print("opcion 1: Ingrese datos \n  opcion 2: ingrese sucursal a informar \n opcion 3: Dia de semana a informar \n opcion 4: Menor fscuracion en la semana \n opcion 5: Total semanal \n opcion 0 para salir")
        opcion = int(input("opcion..."))
