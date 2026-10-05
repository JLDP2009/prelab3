pesos_piezas = [12.5, -5.0, 14.2, 0.0, 18.1, 10.5]

piezas_validas = 0

for peso in pesos_piezas:
    if peso <= 0:
        print(f"Peso {peso} kg. Error de lectura: Flujo negativo descartado.")
    elif 1 <= peso <= 13:
        print(f"Peso {peso} kg. Pieza Ligera aprobada.")
        piezas_validas += 1
    elif peso > 13:
        print(f"Peso {peso} kg. Pieza Pesada aprobada.")
        piezas_validas += 1
    else:
        print(f"Peso {peso} kg. Peso entre 0 y 1 kg: caso no especificado.")

print(f"Total de piezas válidas: {piezas_validas}")