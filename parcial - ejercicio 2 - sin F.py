H = float(input("Profundidad del pozo (en metros): "))
Ld = float(input("Distancia ascendida durante el día (en metros): "))
Ln = float(input("Distancia descendida durante la noche (en metros): "))

if Ld - Ln <= 0:
    print("El caracol no logra salir del pozo.")
else:
    distancia_recorrida = 0
    dias = 0

    while distancia_recorrida < H:
        dias += 1
        distancia_recorrida += Ld

        if distancia_recorrida >= H:
            print(f"El caracol sale del pozo en {dias} días.")
            break

        distancia_recorrida -= Ln