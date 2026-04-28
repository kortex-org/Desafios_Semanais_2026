numeros = [1, 2, 3]
value = []

for i in range(len(numeros) - 1):
    if numeros[i] < numeros[i + 1]:
        value.append(numeros[i]) 

print(sum(value))