nome = input("Qual o nome do aparelho: ")
potap = input("Qual a potência do aparelho: ")
tempconsumo = input("Qual o consumo diário em horas do aparelho: ")

if potap.isdigit() and tempconsumo.isdigit():
    potap = float(potap)
    tempconsumo = float(tempconsumo)

    consumo_mensal = (potap * tempconsumo * 30) / 1000
    conta_mensal = consumo_mensal * 0.75

    print(f"- Aparelho: {nome}")
    print(f"- Consumo mensal: {consumo_mensal:.2f} kWh")
    print(f"- O valor total consumido no mês foi de R$ {conta_mensal:.2f}")
else:
    print("Entrada inválida. Digite apenas números para potência e horas de uso.")
