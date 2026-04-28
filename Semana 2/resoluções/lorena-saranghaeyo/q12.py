altura = 5

for _ in range(altura):
    espacos = " " * (altura - _ - 1)
    estrelas = "*" * (2 * _ + 1)
    print(espacos + estrelas)