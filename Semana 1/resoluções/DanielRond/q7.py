"""Crie um programa que recebe dois valores e depois troca os valores entre eles."""
valor1 = input("V1:")
valor2 = input("V2:")
temporaria = valor1
valor1 = valor2
valor2 = temporaria
print(f"V1:{valor1}\nV2:{valor2}")