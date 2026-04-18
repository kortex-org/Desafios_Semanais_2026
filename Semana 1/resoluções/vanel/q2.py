bolsista = int(input("Aluno bolsista?\n1 - Sim\n0 - Não\nResposta: "))
print("-" * 20)
creditos = int(input("Possui créditos suficiente?\n1 - Sim\n0 - Não\nResposta: "))
print("-" * 20)
horario = int(input("Restaurante está no horário de funcionamento?\n1 - Sim\n0 - Não\nResposta: "))

print("-" * 20)
entrada = (bolsista or creditos) and horario

print(entrada)
