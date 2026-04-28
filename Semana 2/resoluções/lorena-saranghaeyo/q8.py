valores = [3, 1, 3]

if valores[0] == valores [1] and valores[1] == valores[2]:
    print("Equilátero")
elif valores[0] == valores[1] or valores[1] == valores[2] or valores[0] == valores[2]:
    print("Isósceles")
else:
    print("Escaleno")