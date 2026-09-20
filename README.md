# atividade-py-2
valor_compra = float(input("Digite o valor total da compra: R$ "))

if valor_compra < 200:
    percentual_desconto = 0.05
elif valor_compra < 300:
    percentual_desconto = 0.10
else:
    percentual_desconto = 0.15

valor_desconto = valor_compra * percentual_desconto
valor_final = valor_compra - valor_desconto

print(f"\nValor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
print(f"Total a pagar: R$ {valor_final:.2f}")
