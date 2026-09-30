def calcularCustoMoradia (valor_aluguel, valor_condominio, valor_agua):
  totalContas = valor_aluguel + valor_condominio + valor_agua
  if totalContas < 2500:
    return f"Dentro do orçamento R${totalContas}"
  else:
    return f"Atenção ao orçamento: R${totalContas}"
mes1 = calcularCustoMoradia (2000, 350, 90)
mes2 = calcularCustoMoradia (2300, 350, 100)
mes3 = calcularCustoMoradia (2000, 350, 150)

print(mes1)
print(mes2)
print(mes3)