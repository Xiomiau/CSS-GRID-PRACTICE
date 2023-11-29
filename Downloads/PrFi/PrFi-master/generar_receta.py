import datetime
from lista_de_pacientess import mostrar_lista_pacientes
from utilerias import lista_medicamentos,lista_de_pacientes

# Función para generar una receta médica
def generarReceta(pacientes, medicamentos):
    mostrar_lista_pacientes(pacientes)

    # Seleccionar paciente
    numero_paciente = input("Ingrese el número de paciente: ")
    paciente = next((p for p in pacientes if p['numero'] == numero_paciente), None)

    if not paciente:
        print("Error: Paciente no encontrado en el catálogo.")
        return

    # Confirmar paciente
    print("\n--------------------------Información del Paciente----------------------------")
    print(f"{paciente['numero']:<8} {paciente['nombre']:<15} {paciente['direccion']:<15} {paciente['sexo']:<4} {paciente['año_nacimiento']:<14} {paciente['alergias']:<20}\n")

    # Generar folio y solicitar fecha del servicio
    folio_receta = len(pacientes) + 1
    fecha_programada = input("Ingrese la fecha programada (formato: dd/mm/yyyy): ")
    fecha_programada = datetime.datetime.strptime(fecha_programada, "%d/%m/%Y").date()

    # Ingresar datos de medicamentos
    medicamentos_receta = []
    while True:
        codigo_medicamento = input("Ingrese el código del medicamento (o presione <Enter> para finalizar): ")
        if not codigo_medicamento:
            break

        medicamento = next((m for m in medicamentos if m['codigo'] == codigo_medicamento), None)
        if not medicamento:
            print("Error: Código de medicamento no válido.")
            continue

        medicamentos_receta.append(medicamento)

    # Mostrar resumen de receta
    print("\n--------------------------Información del Paciente----------------------------")
    print(f"{paciente['numero']:<8} {paciente['nombre']:<15} {paciente['direccion']:<15} {paciente['sexo']:<4} {paciente['año_nacimiento']:<14} {paciente['alergias']:<20}\n")

    # Mostrar resumen de receta
    print("--------------------------Información Receta Médica----------------------------")
    print(f"Folio: {folio_receta}")
    print(f"Fecha programada: {fecha_programada.strftime('%d/%m/%Y')}\n")

    print("--------------------------Información de Medicamentos------------------------")
    for medicamento in medicamentos_receta:
        print(f"Código: {medicamento['codigo']}")
        print(f"Nombre científico: {medicamento['nombre_cientifico']}")
        print(f"Presentación: {medicamento['presentacion']}")
        print(f"Gramaje: {medicamento['gramaje']}\n")
        print("-" * 80)

    print("Código: <Enter>\n")
    print("-----------------------------Datos de la Receta Médica -----------------------")
    print(f"Folio: {folio_receta}")
    print(f"Fecha programada: {fecha_programada.strftime('%d/%m/%Y')}\n")

    print("-----------------------------Datos de la Receta Médica -----------------------")
    for medicamento in medicamentos_receta:
        print(f"Código: {medicamento['codigo']}")
        print(f"Nombre científico: {medicamento['nombre_cientifico']}")
        print(f"Presentación: {medicamento['presentacion']}")
        print(f"Gramaje: {medicamento['gramaje']}\n")
        print("-" * 80)

    print("Dosis:", end=" ")
    for medicamento in medicamentos_receta:
        print(f"{medicamento['codigo']} {medicamento['nombre_cientifico']} 1 diaria por tiempo indefinido;", end=" ")
    print("\nTomar 3 veces al día x 5 días\n")

# Ejecutar la aplicación
    while True:
        generar_receta(pacientes, medicamentos)
        continuar = input("¿Continuar con otro paciente(s/n)? ")
        if continuar.lower() != 's':
            break

#generar_receta(lista_de_pacientes, lista_medicamentos)