from utilerias import lista_de_pacientes
def mostrar_lista_pacientes(lista_de_pacientes):
    print("Listado de Pacientes".center(120))
    print("-" * 120)
    print("{:<10} {:<30}{:<25} {:<5} {:<20} {:<20}".format("Número", "Nombre", "Dirección", "Sexo", "Año de nacimiento", "Alergias"))
    print("-" * 120)

    for paciente in lista_de_pacientes:
        print("{:<10} {:<30}{:<25} {:<5} {:<20} {:<20}".format(paciente[0], paciente[1], paciente[2], paciente[3], paciente[4], paciente[5]))

    print("-" * 120)
    print(f"Total de Pacientes: {len(lista_de_pacientes)}")


