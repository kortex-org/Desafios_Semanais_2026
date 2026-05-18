"""## Questão 9:
Crie um programa que receba 3 números e retorne a soma dos 2 menores números."""
numero1 = float(input("Número 1:"))
numero2 = float(input("Número 2:"))
numero3 = float(input("Número 3:"))
if numero1>numero2 and numero1>numero3:
    print(f"{numero2}+{numero3}={numero3+numero2}")
if numero2>numero1 and numero2>numero3:
    print(f"{numero1}+{numero3}={numero3+numero1}")
if numero3>numero2 and numero3>numero1:
    print(f"{numero1}+{numero2}={numero1+numero2}")
else:
    print("entrada inválida")