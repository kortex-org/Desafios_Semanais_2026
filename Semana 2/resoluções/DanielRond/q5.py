"""## Questão 5:
Escreva um programa que leia três números e determine quantos deles são pares e quantos são ímpares. Resolva sem utilizar uma estrutura de repetição.

Entrada: 
- Três números inteiros

Saída: 
- Total de pares e total de ímpares.
"""
numero1 = float(input("Número 1:"))
numero2 = float(input("Número 2:"))
numero3 = float(input("Número 3:"))
pares = int(numero1%2==0)+int(numero2%2==0)+int(numero3%2==0)
impares = int(numero1%2==1)+int(numero2%2==1)+int(numero3%2==1)
print(f"Total de pares:{pares}")
print(f"Total de impares:{impares}")