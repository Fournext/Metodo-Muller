import numpy as np
from matplotlib import pyplot as plt
def Graficar(f,x):
    #x=np.linspace(-10.00,10.00,101)
    #fun=x**3-3*x**2+x+1
    #fun=f
    plt.figure()
    plt.plot(x, f)
    plt.xlabel("coordenada x")
    plt.ylabel("coordenada y")
    plt.title("Gráfica de la función")
    plt.grid()
    plt.ion()
    plt.show()