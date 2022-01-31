#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Practica de Decoradores
"""
import random

# Genera matriz random
matriz = [random.randint(1,100) for x in range(1000)]

def sort(*args):        # Ordenamiento con la funcion sort
    matriz.sort()
    print(matriz)

def bubble(*args):     # Ordenamiento con metodo burbuja
    n = len(matriz)

    # Se recorren todos los elementos
    for i in range(n-1):

        # Se recorren los elementos de dos en dos con el elemnto siguiente
        for j in range(0, n-i-1):

            # Realiza un cambio si el elemento siguiente es mayor
            if matriz[j] > matriz[j + 1] :
                matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]

    print ("La matriz arreglado: ")
    for i in range(len(matriz)):
        print (matriz[i],end=" ")

print("Este programa tiene dos tipos de ordenamiento\n(1)-Sort\n(2)-Bubble")
menu = int(input("Ingresa el tipo de ordenamiento que deseas utilizar: "))

if menu == 1:
    sort(matriz)
elif menu == 2:
    bubble(matriz)
else:
    print("La funcion ingresada es incorrecta\n")
