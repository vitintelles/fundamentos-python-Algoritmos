def avaliarEstoqueDeFraldas (quantidade, tamanho):
    if quantidade < 100:
        return f"Atenção! Comprar mais fraldas tamanho {tamanho}."
    else:
        return f"Estoque de fraldas tamanho {tamanho} está tranquilo!"
FraldaRN = avaliarEstoqueDeFraldas (70, "RN")
FraldaP = avaliarEstoqueDeFraldas (150, "P")
FraldaM = avaliarEstoqueDeFraldas (90, "M")
FraldaG = avaliarEstoqueDeFraldas (200, "G")
FraldaXG = avaliarEstoqueDeFraldas (50, "XG")

print(FraldaRN)
print(FraldaP)
print(FraldaM)
print(FraldaG)
print(FraldaXG)