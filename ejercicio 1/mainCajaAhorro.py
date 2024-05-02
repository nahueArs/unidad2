from test1 import test
# Main del ejercicio
if __name__ == "__main__":
    x = 1
    while x:
        print("ingrese 1 para registar 2 para mostrar")
        x = int(input("ingrese opcion"))
        if x == 1:
            test()
