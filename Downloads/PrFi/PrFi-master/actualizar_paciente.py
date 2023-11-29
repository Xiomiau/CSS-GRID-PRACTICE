from utilerias import lista_de_pacientes, formatoImpresion

def modificarPaciente(lista_de_pacientes):
    respuesta="s"
    
    formatoImpresion(lista_de_pacientes)
    while respuesta.lower()=="s": #convierte en minuscula la respuesta para que no haya problema al validar
        paciente_a_actualizar=int(input("Ingrese un número de paciente valido: "))
        modificar=""
        
        for i, paciente in enumerate(lista_de_pacientes): 
                if paciente[0] == paciente_a_actualizar:   
                    formatoImpresion([paciente])
                    modificar=input("Es correcto el paciente que desea modificar (S/N)")
 
                    if modificar.lower()=="s":
                        cambios=""
                        nombre_paciente=input("Nombre: ") or paciente [1]

                        direccion_paciente=input("Dirección: ") or paciente[2]
                        sexo_paciente=input("Sexo: ") or paciente[3]
                        año_nacimiento=input("Año de nacimiento: ") or paciente[4]
                        alergias_paciente=input("Alergias: ") or paciente[5]
                                        
                        paciente_actualizado=[paciente_a_actualizar,nombre_paciente,direccion_paciente,sexo_paciente,año_nacimiento,alergias_paciente]
                        lista_de_pacientes[i]=paciente_actualizado
                        formatoImpresion([lista_de_pacientes[i]])
                        cambios=input("¿Desea confirmar los cambios? (S/N)")
                        if cambios.lower()=="s":
                                formatoImpresion(lista_de_pacientes)
                                respuesta=input("¿Deseas modificar otro paciente?")
                                if respuesta=="s":
                                    break