from Dibujo_Cuadrado import DibujoCuadrado

if __name__ == '__main__':
    operacion = DibujoCuadrado()
    lado = operacion.ingresoLado()
    operacion.dibujarCuadrado(lado)
