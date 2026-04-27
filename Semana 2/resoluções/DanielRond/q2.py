"""## Questão 2:  
Faça um programa que computa os resultados de uma divisão inteira. Dados um dividendo e um divisor, o programa deve informar o quociente e o resto. Caso não seja possível fazer a divisão, o programa deve escrever erro (letras minúsculas).

Entradas:
- Um número inteiro que representa o dividendo (numerador).
- Um número inteiro que representa o divisor (denominador).

Saídas:
- O quociente da divisão.
- O resto da divisão.
"""
numero1 = int(input())
numero2 = int(input())
try:
    print(numero1//numero2)
    print(numero1%numero2)
except ZeroDivisionError:
    print("erro")