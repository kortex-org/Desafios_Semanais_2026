"""## Questão 7:
Faça um programa que determine se um determinado ano lido é bissexto."""
ano = int(input("ANO:"))
if ((ano%4==0) and not(ano%100==0)) or ano%400==0:
    print(f"o ano de {ano} é bissexto")
else:
    print(f"o ano de {ano} NÃO é bissexto")