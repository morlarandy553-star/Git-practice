# =========================================================
# ASIGNATURA: Introducción a la Programación
# PROYECTO: Sistema de Calificaciones (Arreglos y Vectores)
# =========================================================

def main():
    # Vector inicial con 5 calificaciones
    calificaciones = [85, 67, 92, 74, 58]
    UMBRAL_APROBACION = 70

    print("==================================================")
    print("      SISTEMA DE GESTIÓN DE CALIFICACIONES        ")
    print("==================================================\n")

    # 1. Mostrar todas las calificaciones
    print("1. Lista de todas las calificaciones:")
    for i in range(len(calificaciones)):
        print(f"   Estudiante {i}: {calificaciones[i]}")
    print()

    # 2. Mostrar una calificación determinada utilizando su índice
    indice_consulta = 2
    print(f"2. Calificación en el índice {indice_consulta}:")
    print(f"   El estudiante en el índice {indice_consulta} tiene: {calificaciones[indice_consulta]}\n")

    # 3. Calcular el promedio
    suma_total = sum(calificaciones)
    promedio = suma_total / len(calificaciones)
    print(f"3. Promedio general de la clase: {promedio:.2f}\n")

    # 4. Identificar la calificación más alta
    nota_maxima = max(calificaciones)
    print(f"4. Calificación más alta: {nota_maxima}\n")

    # 5. Identificar la calificación más baja
    nota_minima = min(calificaciones)
    print(f"5. Calificación más baja: {nota_minima}\n")

    # 6 y 7. Contar cuántos estudiantes aprobaron y reprobaron
    aprobados = 0
    reprobados = 0

    for nota in calificaciones:
        if nota >= UMBRAL_APROBACION:
            aprobados += 1
        else:
            reprobados += 1

    print(f"6. Estudiantes aprobados (>= {UMBRAL_APROBACION}): {aprobados}")
    print(f"7. Estudiantes reprobados (< {UMBRAL_APROBACION}): {reprobados}\n")

    # 8. Modificar una calificación
    indice_modificar = 4
    nueva_nota = 80
    print(f"8. Modificando calificación en la posición {indice_modificar}...")
    print(f"   Nota anterior: {calificaciones[indice_modificar]}")
    calificaciones[indice_modificar] = nueva_nota
    print(f"   Nueva nota asignada: {nueva_nota}\n")

    # 9. Mostrar nuevamente el vector actualizado
    print("9. Vector de calificaciones actualizado:")
    for i, nota in enumerate(calificaciones):
        print(f"   Estudiante {i}: {nota}")

    print("\n==================================================")
    print("         PROCESAMIENTO COMPLETADO CON ÉXITO       ")
    print("==================================================")

if __name__ == "__main__":
    main()