"""## Questão 6:
Durante um combate no Canal da Mancha o capitão de um navio avistou um submarino inimigo que atacava navios cargueiros. Uma bomba foi jogada na posição X,Y. Dado que o submarino se encontrava na posição I,J você deve fazer um programa que determina se a bomba acertou o submarino. Caso a bomba não acerte, o programa mostra a distância entre a bomba e o submarino. É considerado acerto no submarino se a distância for menor que 300 metros. Lembre-se que o cálculo da distância entre dois pontos pode ser feito utilizando a fórmula da distância euclidiana que é: $d = \sqrt{(x - I)^2 + (J - Y)^2}$. 

Entradas:
- Posição I do submarino (número real);
- Posição J do submarino (número real);
- Posição X da bomba (número real);
- Posição Y da bomba (número real).

Saídas:
- A palavra "ACERTOU" ou a distância (número real).
<img width="633" height="525" alt="image" src="https://github.com/user-attachments/assets/bc9280dc-65a5-4ebb-b52d-3d4934062bab" />"""
i = float(input())
j = float(input())
x = float(input())
y = float(input())
distancia = ((x - i)**2 + (j - y)**2)**(1/2)
if distancia<300:
    print("ACERTOU")
else:
    print(distancia)