"""## Questão 2:
A catraca do Restaurante Universitário (RU) foi programada para liberar a entrada de um aluno avaliando uma única expressão lógica.
A entrada é liberada se o aluno for bolsista (não paga nada) **OU** se ele tiver créditos suficientes na carteirinha **E** o restaurante estiver no horário de funcionamento.
Escreva um programa que leia esses dados e imprima $1$ se a entrada for permitida ou $0$ caso contrário. Não é permitido usar estruturas condicionais.
"""
bolsista = bool(input())
creditos = bool(input())
funcionamento = bool(input())
entrada = (bolsista or creditos) and funcionamento
print(f"${int(entrada)}$")