"""## Questão 11:
Faça um programa que receba a hora do início e a hora final de uma partida de Super Power Flash Turbo Dragon. Cada hora é composta por duas variáveis inteiras: hora e minuto.   Calcule e mostre a duração do jogo (horas e minutos), sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia seguinte.  

Entrada:
- horário de início (horas e minutos)	
- horário de término (horas e minutos)

Saída:
- Duração do jogo (horas e minutos)
"""
horaInicio,minutoInicio = map(int,input().split())
horaFinal,minutoFinal = map(int,input().split())
totalInicio = horaInicio*60 + minutoInicio
totalFinal = horaFinal*60 + minutoFinal
duracao = (totalFinal - totalInicio)%1440
horaDuracao = duracao//60
minutoDuracao = duracao%60
print(horaDuracao,minutoDuracao)