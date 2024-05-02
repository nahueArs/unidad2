class Cuenta:
    __nombre:str
    __apellido:str
    __dni : str
    __telefono:str
    __saldo: float
    __cvu:str
    porcentajeRendimient=68
    
    def __init__(self,nom,app,dni,tel,saldo,cvu):
        self.__nombre=nom
        self.__apellido=app
        self.__dni=dni
        self.__telefono=tel
        self.__saldo=saldo
        self.__cvu=cvu
    
    def __str__(self) -> str:
        return f"{self.__nombre} , {self.__apellido} , {self.__dni} , {self.__telefono} , {self.__saldo} , {self.__cvu}"

    def getdni(self):
        return self.__dni
    def getsaldo(self):
        return self.__saldo
    def getcvu(self):
        return self.__cvu
    
    def getnombre(self):
        return self.__nombre
    
    def getapellido(self):
        return self.__apellido
    @classmethod
    def getporcentaje(cls):
        return  cls.porcentajeRendimient

    
    def setsaldo(self,valor):
        self.__saldo=valor
    def actualizarsaldo(self,imp):
        self.__saldo=self.__saldo-imp
        
    def muestra(self):
        return f"{self.__nombre} , {self.__apellido} , {self.__dni} , {self.__telefono} , {self.__saldo} , {self.__cvu}"

    @classmethod
    def porcentajeRendimiento(cls,porcentaje):
        cls.porcentajeRendimient=porcentaje/365