hora_inicio = 23
minuto_inicio = 00
hora_termino = 1
minuto_termino = 0
resultado = 0

calculo_inicio = hora_inicio * 60 + minuto_inicio
calculo_termino = hora_termino * 60 + minuto_termino

if calculo_termino < calculo_inicio:
    calculo_termino += 1440

resultado = calculo_termino - calculo_inicio

horas = resultado // 60
minutos = resultado % 60

print(horas, minutos)