from utilerias import lista_de_pacientes, formatoImpresion


def darDeBajaPaciente(lista_de_pacientes):
        respuesta="s"
        formatoImpresion(lista_de_pacientes)
        while respuesta.lower()=="s":

                num_paciente=int(input('\n \n Ingresa el número de paciente que quieres dar de baja => \n\n')) #pedimos que se ingrese el numero de paciente para darlo de alta

                existe=False
        
                for paciente in lista_de_pacientes:
                        if paciente[0] == num_paciente:
                                existe=True
                                formatoImpresion([paciente])
                                eliminar=input("\n\n¿Deseas eliminar al paciente?\n\n").lower()
                                if eliminar == "s":
                                        lista_de_pacientes.remove(paciente)          
                                break
                if existe:
                        print("\n\n","-"*25, "El paciente ha sido dado de baja", "-"*25, "\n\n")
                        formatoImpresion(lista_de_pacientes)
                        respuesta=input("\n¿Deseas dar de baja otro paciente?\n")       
                else:
                        print("Este paciente NO existe en el registro")

                               