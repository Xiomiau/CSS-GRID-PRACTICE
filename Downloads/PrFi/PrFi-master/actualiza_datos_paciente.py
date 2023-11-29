from lista_de_pacientess import mostrar_lista_pacientes
from utilerias import lista_de_pacientes, listadoPacienteActualizar, formatoImpresion
def actualizaPaciente(lista_de_pacientes): 
    mostrar_lista_pacientes(lista_de_pacientes)  #mostrar lista de pacientes 
    respuesta="s"
    #
    while respuesta=="s":
        Num_paciente_a_actualizar = int(input("Ingrese un número de paciente valido: "))  #Numero de paciente que se desea modificar
        i = 0 
        actualizado="" #variable auxiliar que ayuda a saber si algo es verdadero o falso  #flag
        while i < len(lista_de_pacientes):
            if  Num_paciente_a_actualizar == lista_de_pacientes[i][0] :
                formatoImpresion([lista_de_pacientes[i]]) #imprime de la lista de pacientes, el paciente 
                paciente_viejo = lista_de_pacientes[i] 
                confirmacion=input("Es correcto el paciente que desea modificar (S/N)")
                if confirmacion.lower() == "s": 
                    #pide los datos para actualizar  #si el campo esta en blanco se deja el dato
                    actualizado=True
                    nombre_paciente = input("Nombre: ")  #Se pide el nombre del paciente
                    if nombre_paciente == "" : 
                        nombre_paciente= lista_de_pacientes[i][1]
                    direccion_paciente = input("Dirección: ")  #Se pide la direccion
                    if direccion_paciente == "" :
                        direccion_paciente = lista_de_pacientes[i][2]
                    sexo_paciente = input("Sexo: ")  #Se pide el sexo
                    if sexo_paciente == "" :
                        sexo_paciente = lista_de_pacientes [i][3]
                    año_nacimiento = input("Año de nacimiento: ")  #se pide el año de nacimiento
                    if año_nacimiento == "" : 
                        año_nacimiento = lista_de_pacientes [i][4]
                    alergias_paciente = input("Alergias: ")  #Se piden las alergias del paciente
                    if alergias_paciente == "" :
                        alergias_paciente = lista_de_pacientes [i][5]
                    #ahora este es paciente nuevo
                    paciente_nuevo = [Num_paciente_a_actualizar, nombre_paciente, direccion_paciente, sexo_paciente, año_nacimiento, alergias_paciente] 
                    listadoPacienteActualizar(paciente_viejo, paciente_nuevo)
                    confirmar_cambios=input("¿Desea confirmar los cambios? (S/N)")
                    if confirmar_cambios.lower() == "s" :
                        lista_de_pacientes[i]=[Num_paciente_a_actualizar, nombre_paciente, direccion_paciente, sexo_paciente, año_nacimiento, alergias_paciente] 
                        listadoPacienteActualizar(paciente_viejo, paciente_nuevo)
            i += 1
        if actualizado==True:
            mostrar_lista_pacientes(lista_de_pacientes)
            respuesta=input("¿Deseas modificar otro paciente?, (S/N)")
            
        else:
            print("Proceso de actualización interrumpida")
            respuesta=input("¿Deseas intentar de nuevo?, (S/N)") 
    
        


        


'''existe=False
buscando=int(input("que paciente buscas=>"))

for paciente in lista_de_pacientes:
    if buscando in paciente:
        existe=True
if existe:
    print("SI")
else:
    print("NO")'''


