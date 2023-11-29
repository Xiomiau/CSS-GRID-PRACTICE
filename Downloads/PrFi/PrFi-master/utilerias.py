#Lista de pacientes para tener algo con lo que trabajar y no estar metiendo datos a cada rato
lista_de_pacientes=[
    [254, "Juan López", "Colima #4", "M", "1967", "Penicilina"],
    [263, "Ana Juárez", "Del Río #8", "F", "1983", "Ninguna"],
    [271, "María Gómez", "Tímuris #7", "F", "2001", "Polen"],
]


#tupla con el directorio de los tipos de medicamentos existentes 
tipos_med=("Ampolletas", "Cápsulas", "Pastillas")
#
lista_medicamentos=(
    ("A10-1", "Insulina","Ampolletas",4),
    ("H03AA-02", "Novotiral","Cápsulas",50),
    ("A08-4", "Anfrepanona","Cápsulas",80),
    ("H03AA-01", "Levotiroxine Sódica","Pastilla",100),
    ("A08", "Catina","Pastilla",100),
    ("A02BD01", "Omeprazol","Pastilla",80),
    ("A02BD02", "Tetraciclina","Cápsulas",25),
    ("A07-1", "Antidiarreico","Suspensión",280),
)

#Funcion que imprime con formato, nomas la importan a donde deseen usarla, le pasan el parametro que que deseen imprimir. Aun no se si sirva de algo  pero ahi ta
def formatoImpresion(lista_de_pacientes):
    print("Listado de Pacientes".center(80))
    print("-" * 120)
    print("{:<10} {:<30}{:<25} {:<5} {:<20} {:<20}".format("Número", "Nombre", "Dirección", "Sexo", "Año de nacimiento", "Alergias"))
    print("-" * 120)

    for paciente in lista_de_pacientes:
        print("{:<10} {:<30}{:<25} {:<5} {:<20} {:<20}".format(paciente[0], paciente[1], paciente[2], paciente[3], paciente[4], paciente[5]))

    print("-" * 120)
    print(f"Total de Pacientes: {len(lista_de_pacientes)}")


#función que imprime el listado de medicamentos 
def impresionMed(lista_medicamentos):
    print("Listado de Medicamentos".center(80))
    print("-" * 120)
    print("{:<15} {:<30}{:<25} {:<10}".format("Clave", "Nombre Científico", "Presentación", "Gramaje/Ml",))
    print("-" * 120)

    for medicamento in lista_medicamentos:
        print("{:<15} {:<30} {:<25} {:<10}".format(medicamento[0], medicamento[1], medicamento[2], medicamento[3]))

    print("-" * 120)
    print(f"Materiales en el catálogo: {len(lista_medicamentos)}")

#función para el ticket de actualización de paciente 
def listadoPacienteActualizar(paciente_viejo,paciente_nuevo) : 
    print("-"*40,"Información del Paciente","-"*40)
    print("-" *107) #paciente_viejo 
    print("{:<10} {:<30}{:<25} {:<5} {:<20} {:<20}".format("Número", "Nombre", "Dirección", "Sexo", "Año de nacimiento", "Alergias"))
    print("-" *110)
    print("{:<10}{:<30}{:<25} {:<5} {:<25} {:<20}".format(paciente_viejo[0],paciente_viejo[1],paciente_viejo[2],paciente_viejo[3],paciente_viejo[4], paciente_viejo[5]))
    print("-"*35,"Actualización de datos del paciente","-"*30) #como sería el paciente nuevo 
    print("{:<20}{:<20}".format("Nombre", paciente_nuevo[1]).center(100))
    print("{:<20}{:<20}".format("Dirección",paciente_nuevo[2]).center(100))
    print("{:<20}{:<20}".format("Sexo",paciente_nuevo[3]).center(100))
    print("{:<20}{:<20}".format("Año de nacimiento",paciente_nuevo[4]).center(100))
    print("{:<20}{:<20}".format("Alergias",paciente_nuevo[5]).center(100))
    #paciente nuevo 
    print("-"*35,"Información Actualizada","-"*35)
    print("-" *107) #paciente a actualizar (nuevo)
    print("{:<10} {:<30}{:<25} {:<5} {:<20} {:<20}".format("Número", "Nombre", "Dirección", "Sexo", "Año de nacimiento", "Alergias"))
    print("-" *110) 
    print("{:<10}{:<30}{:<25} {:<5} {:<25} {:<20}".format(paciente_nuevo[0],paciente_nuevo[1],paciente_nuevo[2],paciente_nuevo[3],paciente_nuevo[4], paciente_nuevo[5]))

