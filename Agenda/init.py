try:

    usuario = []
    control = True
    
    while control:
        pedirDatos = int(input("\nGESTION DE USUARIOS"
                               + "\n==================="
                               + "\n1 = Agregar Usuario"
                               + "\n2 = Borrar Usuario"
                               + "\n3 = Buscar Usuario"
                               + "\n4 = Mostrar Usuario"
                               + "\n0 = Salir"
                               + "\nOpcion : "))
                
        if(pedirDatos == 1):
            print("\nAgregar Nombre, Apellidos, DNI, telefono y direccion")
            nombre = input("Ingrese su nombre: ")
            apellidoP = input("Ingrese su apellido paterno: ")
            apellidoM = input("Ingrese su apellido materno: ")
            dni = input("Ingrese el número de DNI: ")
            telefono = input("Ingrese su telefono: ")
            direccion = input("Ingrese su direccion: ")

            usuario.append(nombre)
            usuario.append(apellidoP)
            usuario.append(apellidoM)
            usuario.append(dni)
            usuario.append(telefono)
            usuario.append(direccion)

        if(pedirDatos == 2):
            
            if not usuario:          
                print("\nLista vacía.")
            else:
                nombre = input("Escribe el Nombre del USUARIO a Borrar: ")      
                if (nombre in usuario[0]):
                    usuario.remove(nombre)
                    usuario.remove(apellidoP)
                    usuario.remove(apellidoM)
                    usuario.remove(dni)
                    usuario.remove(telefono)
                    usuario.remove(direccion)
                    print("\nUsuario eliminado.")
                else:
                    print("\nLo sentimos no hay resultados.")

        if(pedirDatos == 3):
            if not usuario:          
                print("\nLista vacía.")
            else:
                apellidoP = input("Escribe el Apellido del USUARIO a Buscar: ")
                if apellidoP in usuario[1]:
                    print(f"\nDATOS DEL USUARIO")
                    print(f"Nombre: {usuario[0]}")
                    print(f"Apellido Paterno: {usuario[1]}")
                    print(f"Apellido Paterno: {usuario[2]}")
                    print(f"DNI: {usuario[3]}")
                    print(f"Telefono: {usuario[4]}")
                    print(f"Direccion: {usuario[5]}")
                else:
                    print("\nLo sentimos no hay resultados.")

        if(pedirDatos == 4):
            if not usuario:          
                print("\nLista vacía.")
            else:   
                print(f"\nDATOS DEL USUARIO")
                print(f"Nombre: {usuario[0]}")
                print(f"Apellido Paterno: {usuario[1]}")
                print(f"Apellido Paterno: {usuario[2]}")
                print(f"DNI: {usuario[3]}")
                print(f"Telefono: {usuario[4]}")
                print(f"Direccion: {usuario[5]}")

        if(pedirDatos == 0):
            control = False

    print(f"\x1b[1;31m\nPROCESANDO...\033[0;m")
    print(f"\x1b[1;32mSe ha guardado los datos correctamente: \033[0;m")
    archivo = open("Agenda.txt", "w")
    archivo.write(f"DATOS DEL USUARIO \n")
    archivo.write(f"Nombre: {usuario[0]} \n")
    archivo.write(f"Apellido Paterno: {usuario[1]} \n")
    archivo.write(f"Apellido Paterno: {usuario[2]} \n")
    archivo.write(f"DNI: {usuario[3]} \n")
    archivo.write(f"Telefono: {usuario[4]} \n")
    archivo.write(f"Direccion: {usuario[5]} ")
    archivo.close()

except Exception as error:
    print("\nLo sentimos hubo un error: ", error)
