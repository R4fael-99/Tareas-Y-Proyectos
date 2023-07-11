def simular_movimiento_caracol(H, Ld, Ln):
    if Ld - Ln <= 0:
        return -1  # Caracol no sale del pozo
    
    distancia_recorrida = 0
    dias = 0
    
    while distancia_recorrida < H:
        dias += 1
        distancia_recorrida += Ld
        
        if distancia_recorrida >= H:
            break
        
        distancia_recorrida -= Ln
    
    return dias if distancia_recorrida >= H else -1

def main():
    H = float(input("Profundidad del pozo (en metros): "))
    Ld = float(input("Distancia ascendida durante el día (en metros): "))
    Ln = float(input("Distancia descendida durante la noche (en metros): "))
    
    dias = simular_movimiento_caracol(H, Ld, Ln)
    
    if dias != -1:
        print(f"El caracol sale del pozo en {dias} días.")
    else:
        print("El caracol no logra salir del pozo.")

if __name__ == '__main__':
    main()