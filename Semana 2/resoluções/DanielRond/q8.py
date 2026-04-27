"""## Questão 8:
Peça 3 números ao usuário e verifique se é um triângulo. Caso seja um triângulo, diga se é equilátero, isósceles ou escaleno."""
lado1 = float(input("Lado 1:"))
lado2 = float(input("Lado 2:"))
lado3 = float(input("Lado 3:"))
if (lado1+lado2>lado3) and (lado1+lado3>lado2) and (lado2+lado3>lado1):    
    if lado1==lado2 and lado2==lado3:
            print("O triângulo é equilátero")
    elif lado1!=lado2!=lado3:
            print("O triângulo é escaleno")
    else:
            print("O triângulo é isósceles")
else:
        print("Os valores não formam um triâgulo")