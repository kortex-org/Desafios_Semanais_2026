"""## Questão 1:  
Faça um programa que leia dois números e mostre qual deles é o maior."""
numero1 = float(input("Número 1"))
numero2 = float(input("Número 2"))
if numero1>numero2:
    print(numero1)
elif numero1<numero2:
    print(numero2)
else:
    print(f"{numero1}={numero2}")