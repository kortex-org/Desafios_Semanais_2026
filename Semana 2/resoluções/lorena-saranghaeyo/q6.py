import math

i = float(input("Posição 1 - Submarino: "))
j = float(input("Posição 2 - Submarino: "))
x = float(input("Posição 1 - Bomba: "))
y = float(input("Posição 2 - Bomba: "))

distancia = math.sqrt((x - i) ** 2 + (y - j) ** 2)

if distancia < 300:
    print("Acertou!")
else:
    print(f"Errou, a distância é de {distancia:.2f} metros.")