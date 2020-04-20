import numpy as np

from rectancle_method import rect
from trapezoid_method import trapz

f=lambda x : np.sin(4*x)*np.exp(-x**2+3*x)

xmin,xmax,nbr=0,5,20

rect(f,xmin,xmax,nbr)
trapz(f,xmin,xmax,nbr)
