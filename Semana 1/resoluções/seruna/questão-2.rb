puts("Responda \"sim\" em caso afirmativo.")
puts("O aluno é bolsista?")
bolsista = (gets().chomp() == "sim")
puts("Se não for bolsista, tem créditos suficientes?")
creditos_suficientes = (gets().chomp() == "sim")
puts("O restaurante está aberto?")
restaurante_aberto = (gets().chomp() == "sim")
entrada_liberada = (bolsista or creditos_suficientes) and restaurante_aberto
puts(entrada_liberada)
