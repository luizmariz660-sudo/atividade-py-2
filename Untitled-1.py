valor_compra = float(input("Digite o valor total da compra: R$ "))

if valor_compra < 200:
    percentual_desconto = 0.05
elif valor_compra < 300:
    percentual_desconto = 0.10
else:
    percentual_desconto = 0.15

valor_desconto = valor_compra * percentual_desconto
valor_pago = valor_compra - valor_desconto

print(f"\nValor da compra: R$ {valor_compra:.2f}")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor total a pagar: R$ {valor_pago:.2f}")

git init
git add .
git commit -m "Primeiro commit"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPO.git
git push -u origin main