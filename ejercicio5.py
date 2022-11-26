#EJERCICIO 5 | TEMA 1 | Tipos de Datos Simples
#Escribe un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.


horas = float(input("Introduce el numero de horas trabajadas: "))
coste = float(input("Introduce el coste por hora: "))
paga=horas*coste

print("tu pagas es de:",paga)