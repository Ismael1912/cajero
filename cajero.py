#prueba cabecera
import os

from typing import Sequence
from os import system
import re

def saldo_final(saldo_inicial, saldo_a_retirar):
    saldo_1 = saldo_inicial - saldo_a_retirar
    return saldo_1
    

def mostrar_menu_principal(contador):
    if contador == 0:
        print("******BIENVENIDO*****")
    
    
    opcion = input("""Seleccione una opcion a realizar
    Consulta saldo (C) 
    Retiro         (R)
    Deposito       (D)
    Salir          (S)
    """)
    return opcion


def run():
    contador = 0
    respuesta = ''
    saldo = 4000
    retiro = 0
    opcion = ''
    opcion_retiro = 0
    opcion = mostrar_menu_principal(contador)
    contador += 1
    resto = 0
    while opcion != 's':
        if opcion == 'c':
            system ('cls')
            print('Su saldo es de $' + str(saldo) + ' pesos')
            input('Presione ENTER para continuar')
            system ("cls")
            opcion = mostrar_menu_principal(contador)   
        elif opcion == 'r':
            system ('cls')
            while True:
                try:
                    opcion_retiro = int(input("""Seleccione la opcion para retirar
                    (1) Para $100
                    (2) Para $200
                    (3) Para $500
                    (4) Para $1000 
                    (5) Otra cantidad
                    """))
                    if opcion_retiro > 5 or opcion_retiro < 1:
                        system ('cls')
                        print("La opcion ingresada no es la correcta")    
                        continue
                    break
                except ValueError:
                    system ('cls')
                    print("La opcion ingresada no es la correcta")
                    os.system("pause")
                    system ("cls")
            if opcion_retiro == 1:
                resto = saldo_final(saldo, 100)
            elif opcion_retiro == 2:
                resto = saldo_final(saldo, 200)
            elif opcion_retiro == 3:
                resto = saldo_final(saldo, 500)
            elif opcion_retiro == 4:
                resto = saldo_final(saldo, 1000)
            elif opcion_retiro == 5:
                system ("cls")
                while True:
                    try:
                        cantidad_a_retirar = int(input('Ingrese la cantidad a retirar: '))
                        if cantidad_a_retirar < 0:
                            system ("cls")
                            print('La cantidad no puede ser negativa')
                            continue
                        if cantidad_a_retirar == 0:
                            system ("cls")
                            print('La cantidad no puede ser de 0')
                            continue
                        resto = saldo_final(saldo, cantidad_a_retirar)
                        break
                    except ValueError:
                        system ('cls')
                        print("El valor ingresado no es el correcto")
            if resto < 1000:
                system ('cls')
                print('Su saldo no puede ser menor a $1000 pesos')
            else:
                system ("cls")
                saldo = resto
                print(f'Su saldo es de ${saldo}')
            os.system("pause")
            system ("cls")
            opcion = mostrar_menu_principal(contador)
        elif opcion == 'd':
            system ("cls")
            while True:
                try:
                    cantidad_a_depositar = int(input('Ingrese la cantidad a depositar: '))
                    if cantidad_a_depositar < 0:
                        system ("cls")
                        print('La cantidad no puede ser negativa')
                        continue
                    elif cantidad_a_depositar == 0:
                        system ("cls")
                        print('La cantidad no puede ser de 0')
                        continue
                    else:
                        system ("cls")
                        saldo = saldo + cantidad_a_depositar
                        print(f'Su saldo es de ${saldo}')
                        os.system("pause")
                        break
                except:
                    system ("cls")
                    print("El valor ingresado no es el correcto")
            system ("cls")
            opcion = mostrar_menu_principal(contador)
        elif opcion == "s":
            print('GRACIAS POR SU PREFERENCIA')
            os.system("pause")
            #quit()
        else:
            system ('cls')
            print('Elija otra opcion')
            input('Presione ENTER para continuar')
            system ('cls')
            opcion = mostrar_menu_principal(contador)


if __name__ == '__main__':
    run ()