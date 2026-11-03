
calificaciones = []


for i in range(8):
    while True:
        try:
            nota = float(input(f"Ingrese la nota del estudiante {i + 1}: "))

            if 0 <= nota <= 100:
                calificaciones.append(nota)
                break
            else:
                print("La nota debe estar entre 0 y 100.")

        except ValueError:
            print("Ingrese un número válido.")


print("\n--- RESULTADOS ---")
print("Calificaciones registradas:", calificaciones)


promedio = sum(calificaciones) / len(calificaciones)
print("Promedio:", round(promedio, 2))


print("Nota más alta:", max(calificaciones))
print("Nota más baja:", min(calificaciones))

aprobados = []

for nota in calificaciones:
    if nota >= 61:
        aprobados.append(nota)

print("Cantidad de estudiantes aprobados:", len(aprobados))


print("Calificaciones aprobadas:", aprobados)
