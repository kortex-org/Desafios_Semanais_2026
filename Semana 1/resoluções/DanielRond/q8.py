"""## Questão 8:
Faça um programa que receba dois números e exiba a soma, subtração, multiplicação e divisão entre eles."""
n1 = float(input("numero 1:"))
n2 = float(input("numero 2:"))
print(f'''
soma : {n1}+{n2} = {n1+n2}
subtração : {n1}-{n2} = {n1-n2}
multiplicação : {n1}x{n2} = {n1*n2}
divisão : {n1}/{n2} = {n1/n2}
''')