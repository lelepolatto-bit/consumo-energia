"""Calculadora de consumo mensal de energia elétrica."""

TARIFA_KWH = 0.75
DIAS_NO_MES = 30


def ler_numero_positivo(mensagem):
    """Lê e devolve um número positivo, aceitando vírgula ou ponto decimal."""
    while True:
        valor_digitado = input(mensagem).strip().replace(",", ".")

        try:
            valor = float(valor_digitado)
            if valor > 0:
                return valor
            print("Digite um valor maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite apenas um número.")


def calcular_consumo_mensal(potencia, horas_dia):
    """Calcula o consumo mensal do aparelho em kWh."""
    return (potencia * horas_dia * DIAS_NO_MES) / 1000


def main():
    """Solicita os dados e exibe o consumo e o custo mensal estimados."""
    print("⚡ Calculadora de Consumo de Energia ⚡\n")

    aparelho = input("Nome do aparelho: ").strip()
    while not aparelho:
        print("O nome do aparelho não pode ficar vazio.")
        aparelho = input("Nome do aparelho: ").strip()

    potencia = ler_numero_positivo("Potência do aparelho (W): ")
    horas_dia = ler_numero_positivo("Tempo médio de uso diário (horas): ")

    consumo_mensal = calcular_consumo_mensal(potencia, horas_dia)
    custo_estimado = consumo_mensal * TARIFA_KWH

    print("\n--- Resultado ---")
    print(f"Aparelho: {aparelho}")
    print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
    print(f"Custo estimado: R$ {custo_estimado:.2f}/mês")
    print(f"(Tarifa considerada: R$ {TARIFA_KWH:.2f} por kWh)")


if __name__ == "__main__":
    main()
