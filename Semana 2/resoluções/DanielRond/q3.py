"""## Questão 3:
Uma loja oferece 5% de desconto para os clientes que pagarem utilizando cartão de crédito, nenhum para quem utilizar cartão de débito e 10% para quem utilizar pix.  
Faça um programa que receba o valor da compra, a forma de pagamento e exiba o valor final da compra.
"""
valor = float(input("Valor da compra:"))
forma_pagamento = input("forma de pagamento:")
if forma_pagamento=="debito":
    valor_final =valor
if forma_pagamento=="credito":
    valor_final = valor*0.95
if forma_pagamento=="pix":
    valor_final = valor*0.9
else:
    print("forma de pagamento inválida")

print(f"valor:{valor}")
print(f"forma de pagamento:{forma_pagamento}")
print(f"valor final:{valor_final}")