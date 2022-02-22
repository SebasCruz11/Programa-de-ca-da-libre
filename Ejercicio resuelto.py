# Lógica de programación
# Resolver el ejercicio que desee de mecánica

import numpy as np
import matplotlib.pyplot as plt

# EJERCICIO
# Un niño lanza un juguete desde el suelo de un eficio con una velocidad de 15 m/s. Después de 6 segundos otro
# niño observa a través de su ventana que el juguete se detiene y baja de nuevo.
# Calcular la distancia a la que se encuentra el segundo niño.
# Calcular la 

'''
V=Velocidad Final
Vo=Velocidad Inicial
G=Gravedad 10
D=Distancia
T=Tiempo
'''

import math
x="s"
while x=="s" or x=="S":
    n=0
    v=0
    vo=0
    t=0
    g=9.8
    h=0
    r=0
    print ("Programa de caida libre: ")
    print ("1.-V=Vo-G*T")
    print ("2.-D=Vo*T-1/2G*T^2")
    print ("3.-D=((Vo+V)/2)*T")
    print ("Después de analizar los datos que tenemos en el ejercicio, sabemos que tenemos una velocidad inicial de 15m/s, una velocidad final de 0m/s porque alcanza su punto máximo, y un tiempo de 6 segundos.")
    print ("Por lo que procederemos a usar la ecuación 3")
    n=input("Indique que ecuación desea usar: ")
    while int(n)<1 or int(n)>4:
        n=input("Indique que ecuacion desea usar(de la lista): ")
    if int(n)==1:
        vo=input("Ingrese la velocidad inicial: ")
        t=input("Ingrese el tiempo: ")
        while int(t)<=0:
            t=input("Ingrese el tiempo(positivo): ")
        v=int(vo)-g*int(t)
        print ("La velocidad final es: ",round(v,3))
    elif int(n)==2:
        vo=input("Ingrese la velocidad inicial: ")
        t=input("Ingrese el tiempo: ")
        while int(t)<=0:
            t=input("Ingrese el tiempo(positivo): ")
        h=int(vo)*int(t)+1/2*g*int(t)**2
        print ("La distancia recorrida es: ",round(h,3))
    elif int(n)==3:
        vo=input("Ingrese la velocidad inicial: ")
        v=input("Ingrese la velocidad final: ")
        t=input("Ingrese el tiempo: ")
        while int(t)<=0:
            t=input("Ingrese el tiempo(positivo): ")
        h=(((int(v)+int(vo))/2)*int(t))
        print ("La distancia recorrida es: ",round(h,3))
    print ("Como el ejercicio solamente nos pide la distancia entonces no deseamos usarla [n]")
    x=input("Desea usar otra formula(s/n): ")

print ("Entonces, obtenemos que la distancia a la que se encuentra el segundo niño desde el suelo, es de 45m")
print ("Gracias :)")
