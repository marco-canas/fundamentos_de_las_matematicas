def graficar(funcion):
    '''
    INPUT: 
    funcion: función a graficar dada en lenguaje python
    '''
    import numpy as np 
    import matplotlib.pyplot as plt
    dominio=np.array([-4,4])
    rango=f(dominio)
    plt.plot(dominio, rango)