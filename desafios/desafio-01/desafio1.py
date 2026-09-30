def chamar_pet (nome, especie):
  if especie == "Cachorro":
    return(f"Hora de passear, {nome}")
  else:
    return(f"Hora de dormir, {nome}")


resultado1 = chamar_pet ("Alaska", "Cachorro")
resultado2 = chamar_pet ("Thor", "Gato")
resultado3 = chamar_pet ("Summer", "Gato")
print(resultado1)
print(resultado2)
print(resultado3)