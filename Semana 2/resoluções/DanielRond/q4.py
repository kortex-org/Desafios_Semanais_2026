"""## Questão 4:
Elabore um programa que, leia da entrada padrão a idade de um nadador, classifique-o em uma das seguintes categorias e exiba a sua categoria:
<img width="392" height="261" alt="image" src="https://github.com/user-attachments/assets/4a3b4e2c-73ab-435a-ad5c-c20254cd8cf4" />"""
idade = int(input())
if idade<=7 and idade>=5:
    print("Infantil A")
if idade<=10 and idade>=8:
    print("Infantil B")
if idade<=13 and idade>=11:
    print("Juvenil A")
if idade<=17 and idade>=14:
    print("Juvenil B")
if idade>=18:
    print("Adulto")