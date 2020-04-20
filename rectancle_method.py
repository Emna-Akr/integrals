import numpy as np
import matplotlib.pyplot as plt

def rect(f,xmin,xmax,nbr):    
    #METHODE DES RECTANGLE CALCUL ET GRAPH 
    x=np.linspace(xmin,xmax,nbr+1)
    y = f(x)
    integrale_rectangle = 0
    for i in range(nbr):
        integrale_rectangle = integrale_rectangle + y[i]*(x[i+1]-x[i]) 
        x_rect = [x[i], x[i], x[i+1], x[i+1], x[i]] 
        y_rect = [0 , y[i], y[i] , 0 , 0 ] 
        plt.plot(x_rect, y_rect,"c") 
        
    plt.title('Courbe calcul intégrale méthode de réctangle',loc='center')
    
    X=np.linspace(xmin,xmax,501)
    Y=f(X)
    plt.plot(X,Y,"0.4")
    
    plt.show()
    print("\tintegrale_rectangle =", integrale_rectangle)
    return(integrale_rectangle)