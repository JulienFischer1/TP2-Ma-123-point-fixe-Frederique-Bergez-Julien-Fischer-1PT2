"""TP n°2 génie mathematique (Ma123) 
Julien Fischer, Frédérique Bergez"""

import math

def g1(x):
    return (9-3*x)**(1/4)
def g1bis(x):
    return -1*((9-3*x)**(1/4))
def g2(x):
    return math.acos((2+x)/3)
def g3(x):
    return math.log(7)-math.log(x)
def g4(x):
    return math.log(10+x)
def g5(x):
    return math.atan((x+5)/2)
def g6(x):
    return math.log((x**2)+3)
def g7(x):
    return (7-(4*math.log(x)))/3
def g8(x):
    return (2*(x**2)-4*x+17)**(1/4)
def g9(x):
    return math.log(2*(math.sin(x))+7)
def g10(x):
    return math.log(10)-math.log(math.log((x**2)+4))
    

def PointFixe(g,x0,epsilon,Nitermax):
    xold = x0
    xnew = g(xold)
    erreur = xnew - xold
    n = 1
    while abs(erreur) > epsilon and n < Nitermax:
        xnew = g(xold)
        erreur = xnew - xold
        xold = xnew
        n += 1
        print(xnew,n,xnew - xold)
    return xnew

print("-----"*10)
print("solution de g1(x) = x pour f1 :")
PointFixe(g1,3/2,1e-4,1e4)
print("-----"*10)

print("solution de g1bis(x) = x pour f1 :")
PointFixe(g1bis,-2,1e-4,1e4)
print("-----"*10)

print("solution de g2(x) = x pour f2 :")
PointFixe(g2,0.54,1e-4,1e4)
print("-----"*10)

print("solution de g3(x) = x pour f3 :")
PointFixe(g3,1.5,1e-4,1e4)
print("-----"*10)

print("solution de g4(x) = x pour f4 :")
PointFixe(g4,2.5,1e-4,1e4)
print("-----"*10)

print("solution de g5(x) = x pour f5 :")
PointFixe(g5,1.5,1e-4,1e4)
print("-----"*10)

print("solution de g6(x) = x pour f6 :")
PointFixe(g6,1.8,1e-4,1e4)
print("-----"*10)

print("solution de g7(x) = x pour f7 :")
PointFixe(g7,1.4,1e-4,1e4)
print("-----"*10)

print("solution de g8(x) = x pour f8 :")
PointFixe(g8,2,1e-4,1e4)
print("-----"*10)

print("solution de g9(x) = x pour f9 :")
PointFixe(g9,2,1e-4,1e4)
print("-----"*10)

print("solution de g10(x) = x pour f10 :")
PointFixe(g10,1.6,1e-4,1e4)
print("-----"*10)