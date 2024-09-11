class DibujoCuadrado:
    def ingresoLado(self):
        lado = int(input("Ingrese el tamaño del lado del cuadrado: "))
        return lado

    def dibujarCuadrado(self, lado):
        for i in range(lado):
            print("* " * lado)

if __name__ == '__main__':
    operacion = DibujoCuadrado()
    lado = operacion.ingresoLado()
    operacion.dibujarCuadrado(lado)
