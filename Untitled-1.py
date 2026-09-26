"""
Projeto: atividade-py-2
Repositório: https://github.com/luizmariz660-sudo/atividade-py-2
Descrição: calcula o valor final de uma compra com descontos por faixa de preço.
"""


def calcular_desconto(valor_compra):
    if valor_compra < 200:
        percentual_desconto = 0.05
    elif valor_compra < 300:
        percentual_desconto = 0.10
    else:
        percentual_desconto = 0.15

    valor_desconto = valor_compra * percentual_desconto
    valor_pago = valor_compra - valor_desconto
    return percentual_desconto, valor_desconto, valor_pago


def main():
    print("=== Loja do Luiz ===")
    print("Sistema de cálculo de desconto por valor da compra\n")

    try:
        valor_compra = float(input("Digite o valor total da compra: R$ ").replace(",", "."))
        if valor_compra <= 0:
            raise ValueError
    except ValueError:
        print("Valor inválido. Digite um número maior que zero.")
        return

    percentual_desconto, valor_desconto, valor_pago = calcular_desconto(valor_compra)

    print(f"\nValor da compra: R$ {valor_compra:.2f}")
    print(f"Percentual de desconto: {percentual_desconto * 100:.0f}%")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Valor total a pagar: R$ {valor_pago:.2f}")


if __name__ == "__main__":
    main()
