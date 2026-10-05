print("""A. "Mover a la derecha"
B. "Mover a la izquierda"
C. "Mover hacia el frente"
D. "Mover hacia atrás"
E. "Apagar""")

while True:
    comando= input("Ingrese un comando (A,B,C,D,E): ")


    match comando:
        case "A":
            print("El robot se mueve a la derecha")
        case "B":
            print("El robot se mueve a la izquierda")
        case "C":
            print("El robot se mueve hacia el frente")
        case "D":
            print("El robot se mueve hacia atrás")
        case "E":
            print("El robot se apaga")
            break
        case _:
            print("Comando no reconocido. Intente nuevamente.")
