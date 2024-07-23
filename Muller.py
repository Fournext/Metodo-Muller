import cmath
from Grafica import Graficar
import numpy as np
from matplotlib import pyplot as plt

def muller(f, x0, x1, x2, epsilon=1e-10, max_iter=100):
    h1 = x1 - x0
    h2 = x2 - x1
    y1 = (f(x1) - f(x0)) / h1
    y2 = (f(x2) - f(x1)) / h2
    a = (y2 - y1) / (h2 + h1)
    n_iter = 3
    x = None
    while n_iter <= max_iter:
        b = y2 + h2*a
        c=f(x2)
        D = cmath.sqrt(b**2 - 4*c*a) #sacar el valor de la raiz de la cuadratica
        if abs(b-D) < abs(b+D): #sacar el signo de b
            E = b + D
        else:
            E = b - D
        h = -2*c/E 
        p = x2 + h #obtiene todo el valor de la cuadrtica 
        if abs(h) < epsilon: #pregunta si el error a llegado al limite y sale de la funcion si es asi
            x = p
            break
        #actualizamos los valores para las nuevas iteraciones
        x0, x1, x2 = x1, x2, p
        h1 = x1 - x0
        h2 = x2 - x1
        y1 = (f(x1) - f(x0)) / h1
        y2 = (f(x2) - f(x1)) / h2
        a = (y2 - y1) / (h2 + h1)
        n_iter += 1
    if x is None:
        raise ValueError("El método no converge")
    return x

def MullerGraf(f, x0, x1, x2):
    fun = lambda x: eval(f) #x**3+3*x**2-2
    res=muller(fun, x0, x1, x2)    #-10,-6,-1

    #grafica
    x=np.linspace(-10.00,10.00,101)
    #f=y**3+3*y**2-2
    Graficar(eval(f),x) 
    return res

#g=(input("dame la funcion: "))
#x0=float(input("dame x0: "))
#x1=float(input("dame x1: "))
#x2=float(input("dame x2: "))

#fun = lambda x: eval(g) #x**3+3*x**2-2
#print("La aproximacion es:",muller(fun, x0, x1, x2))    #-10,-6,-1

#grafica
#x=np.linspace(-10.00,10.00,101)
#f=y**3+3*y**2-2
#Graficar(eval(g),x) 


