agenda = open("agendatelefonica.csv",'a') #Abrimos y creamos el archivo
nombre = input("Nombre de contacto: ")#Capturamos el nombre del contacto
telefono = input("Teléfono: ")#Capturamos el telefonos del contacto
print("Se ha guardado en la agenda el contacto: ",nombre,"con el número de teléfono",telefono)
agenda.write(nombre)
agenda.write(",")
agenda.write(telefono)
agenda.write(",")
agenda.write("\n")
agenda.close()
