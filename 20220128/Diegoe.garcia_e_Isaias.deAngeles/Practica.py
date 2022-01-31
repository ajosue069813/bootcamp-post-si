import random
import time
import os


def f1(funcion):
    def wrapper(*args, **kwargs):
        print("La lista ordenada con el metodo seleccionado es:   ")
        print(lista)
        nuevo = "Log.txt"
        f = open(nuevo,"w")
        start_time = time.time()
        res = funcion(*args, **kwargs)
        f.write(f"El tiempo logrado fue de {time.time() - start_time} segundos")
        return res

    return wrapper


@f1  # suma = f1(suma)
def burbuja(*args):  #Ordenamiento con Burbuja
    for n in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                temp = lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=temp
    print(lista)

@f1
def sort(*args):
    lista.sort()
    print(lista)


numeros = int(input("Ingresa el tamano de lista que deseas --> "))
lista = []

for n in range(numeros):
    lista.append(random.randint(0,999))

funcion = input("Ingresa la funcion que quieras utilizar, sort o burbuja: ")

if funcion == 'burbuja':
    burbuja(lista)
elif funcion == 'sort':
    sort(lista)
else: 
    print("Funcion no reconocida pana, intenta de nuevo")

