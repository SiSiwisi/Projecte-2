def calcular_preu(preu_peces, cost_ma_obra):
    total = preu_peces + cost_ma_obra
    return total

# Introducir los precios
preu_peces = float(input("Introduce el precio de las piezas: "))
cost_ma_obra = float(input("Introduce el coste de la mano de obra: "))

# Llamar a la función
preu = calcular_preu(preu_peces, cost_ma_obra)

# Mostrar el resultado
print("Coste total de la reparación:", preu, "€")
