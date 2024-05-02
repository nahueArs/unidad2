import csv
class transaccion():
    __cvu:str
    __nrotransaccion:str
    __importe:float
    __tipoTansaccion:str
    
    def __init__(self, cvu, nro, importe, tipo):
        self.__cvu = cvu
        self.__nrotransaccion = nro
        self.__importe = importe
        self.__tipoTansaccion = tipo
    def __str__(self):
        return f"{self.__cvu}, {self.__nrotransaccion}, {self.__importe}, {self.__tipoTansaccion}"
        
    def gettr(self):
        return self.__tipoTansaccion
    
    def getcvu(self):
        return self.__cvu
    
    def getimp(self):
        return self.__importe