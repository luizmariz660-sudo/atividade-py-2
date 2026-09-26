"""
Projeto: cálculo de desconto por valor da compra
Descrição: Programa que calcula o valor final de uma compra com desconto.
"""


def calcular_desconto(valor_compra):
    if valor_compra < 200:
        percentual = 0.05
    elif valor_compra < 300:
        percentual = 0.10
    else:
        percentual = 0.15

    valor_desconto = valor_compra * percentual
    valor_final = valor_compra - valor_desconto
    return percentual, valor_desconto, valor_final


def main():
    print("=== Loja do Luiz ===")
    print("Sistema de cálculo de desconto\n")

    try:
        valor_compra = float(input("Digite o valor total da compra: R$ ").replace(",", "."))
        if valor_compra <= 0:
            raise ValueError
    except ValueError:
        print("Valor inválido. Digite um número maior que zero.")
        return

    percentual, valor_desconto, valor_final = calcular_desconto(valor_compra)

    print(f"\nValor da compra: R$ {valor_compra:.2f}")
    print(f"Percentual de desconto: {percentual * 100:.0f}%")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Valor total a pagar: R$ {valor_final:.2f}")


if __name__ == "__main__":
    main()
