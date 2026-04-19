"""Um professor resolve fazer na sua disciplina três avaliações com pesos diferentes. Faça um algoritmo que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada dessas notas.
Entradas:
Três números reais representando as notas nas avaliações
Três números reais correspondendo aos pesos das avaliações
Saídas:
Número real correspondente a média ponderada das notas"""
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
peso1 = float(input())
peso2 = float(input())
peso3 = float(input())
media = ((nota1*peso1) + (nota2*peso2) + (nota3*peso3))/(peso1+peso2+peso3)
print(media)
