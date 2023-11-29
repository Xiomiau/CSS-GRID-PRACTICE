from agregar_paciente import agregarPaciente #importa la funcion para agregar el paciente y ejecutarla si el usuario elige 1 del menu
from utilerias import lista_de_pacientes, impresionMed, lista_medicamentos #importa la lista de pacientes
from lista_de_pacientess import mostrar_lista_pacientes #importa la funcion que muestra los pacientes registrados
from actualiza_datos_paciente import actualizaPaciente #importa la funcion para modificar los datos de los pacientes
from dar_de_baja_paciente import darDeBajaPaciente #importa la funcion para eliminar pacientes de la lista
from generar_receta import generarReceta
from actualiza_datos_paciente import actualizaPaciente



def menu():
    opciones=[1,2,3,4,5,6,7,8,9,10] #opciones que tiene el usuario para elegir 
    while True:
        
        #menu que se mostrara al usuario
        opcion_usuario=int(input("\n\n\tRegistro y gestión de recetas médicas \n\n"
                    "1. Agregar un nuevo paciente al catálogo\n"
                    "2. Dar de baja un paciente del catálogo\n"
                    "3. Actualizar los datos de un paciente\n"
                    "4. Mostrar el listado de pacientes\n"
                    "5. Generar una receta a un paciente \n"
                    "6. Eliminar una receta generada a un paciente\n"
                    "7. Actualizar datos de una receta (presentación, gramaje y/o la dosis)\n"
                    "8. Mostrar el listado de recetas generadas a determinado paciente\n"
                    "9. Mostrar un listado medicamentos.\n"
                    "10. Salir \n \n"
                    "Tecleé su opción => ")) #Aqui esperamos la respuesta del usuario la cual se convertira a un numero (int) para compararla mas adelante

        #Aqui comparamos y validamos la respuesta del usuario y asignamos una funcion segun la respuesta
        if opcion_usuario not in opciones:
            print("\n",">"*20,"ERROR Opción no válida, ingrese una del 1 al 10 \n","<"*20)
        elif opcion_usuario == 1: #Agregamos un paciente a la lista
            agregarPaciente(lista_de_pacientes)
        elif opcion_usuario==2: #Eliminamos un paciente de la lista
            darDeBajaPaciente(lista_de_pacientes)
        elif opcion_usuario==3: #Modificamos un dato del paciente
            actualizaPaciente(lista_de_pacientes)
        elif opcion_usuario == 4: #Mostramos la lista de pacientes
            mostrar_lista_pacientes(lista_de_pacientes)
        elif opcion_usuario==5:
            generarReceta(lista_de_pacientes,lista_medicamentos)
        elif opcion_usuario==9:
            impresionMed(lista_medicamentos)
            input(" \nPresiona Enter para salir => ")
        elif opcion_usuario==10:
            break
            
menu()