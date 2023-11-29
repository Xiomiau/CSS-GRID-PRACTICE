from utilerias import lista_de_pacientes, lista_medicamentos, impresionMed,formatoImpresion

def generarReceta(lista_de_pacientes, lista_medicamentos):
    medicamentos_receta = []
    formatoImpresion(lista_de_pacientes)
    
    respuesta="s"
    folio=0
    while respuesta.lower()=="s": 
        
        num_paciente=int(input('\n \n Ingresa el número de paciente => \n\n'))
        existe=False
        
        for paciente in lista_de_pacientes:
            if paciente[0] == num_paciente:
                existe=True
                formatoImpresion([paciente])
        if  existe:
            folio+=1             
            folio_receta=folio
            fecha=input("Ingresa la fecha: DD/MM/AAA: ")
            codigo_medicamento = input("Ingrese el código del medicamento: ")
            
            
            while respuesta.lower()=="s":
                existe=False
                for medicamento in lista_medicamentos:
                    if codigo_medicamento==medicamento[0]:
                        existe=True
                        if existe:
                            if medicamento not in medicamentos_receta:
                                medicamentos_receta.append(medicamento)
                                impresionMed(medicamentos_receta)
                            else:
                                print(">"*15,"Este medicamento ya ha sido añadido","<"*15)    
                            respuesta=input("\nDeseas agregar otro medicamento?\n")
                            if respuesta.lower()=="s":
                                codigo_medicamento = input("Ingrese el código del medicamento: ")
                            else:
                                print(">"*25,"Información del paciente", "<"*25)
                                print("{:<10} {:<30}{:<25} {:<5} {:<20} {:<20}".format("Número", "Nombre", "Dirección", "Sexo", "Año de nacimiento", "Alergias"))
                                print("{:<10} {:<30}{:<25} {:<5} {:<20} {:<20}".format(paciente[0], paciente[1], paciente[2], paciente[3], paciente[4], paciente[5]))
                                print("-" * 30 + " Información de Recetas " + "-" * 30)
                                print("Folio: {}".format(folio_receta))
                                print("Fecha: {}".format(fecha))
                                
                                for med in medicamentos_receta:
                                    print("-" * 30)
                                    print("Código: {}".format(med[0]))
                                    print("Nombre científico: {}".format(med[1]))
                                    print("Presentación: {}".format(med[2]))
                                    print("Gramaje/mL: {}".format(med[3]))
                                    
                                print("-" * 30)
            respuesta=input("Deseas generar otra receta?")
                                
generarReceta(lista_de_pacientes,lista_medicamentos)
                                
            
        