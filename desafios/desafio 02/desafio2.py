def calcularHoraExtra(horas_trabalhadas, carga_padrao = 12):
  hora_extra = horas_trabalhadas - carga_padrao
  if hora_extra > 0:
    return hora_extra
  else:
    return ("Plantão dentro do horário, sem horas extras.")
plantao1 = calcularHoraExtra(15)
plantao2 = calcularHoraExtra(10)
plantao3 = calcularHoraExtra(12)

print(plantao1)
print(plantao2)
print(plantao3)