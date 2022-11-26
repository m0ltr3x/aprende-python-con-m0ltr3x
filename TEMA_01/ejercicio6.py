#                                               EJERCICIO 6 | TEMA 1 | Tipos de Datos Simples
#Escribir un programa que lea un entero porsitivo,  n , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta  n . 
# La suma de los  n  primeros enteros positivos puede ser calculada de la siguiente forma: suma=n*(n+1)/2



numero=int(input("Introduzca un numero positivo: "))

suma=numero*(numero+1)/2

print("La suma de los numeros enteros desde 1 hasta " + str(numero) + "es " + str(suma))