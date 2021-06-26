def agregar_contacto():     
    add_archivo = open("contactos.txt","a") #Agregar
    nombre1 = input("➣ Ingrese Primer Nombre: ")
    apellido1 = input("➣ Ingrese Apellido Paterno: ")
    apellido2 = input("➣ Ingrese Apellido Materno: ")
    telefono = input("➣ Ingrese Número: ")
    add_archivo.write(nombre1+","+apellido1+","+apellido2+","+telefono)
    add_archivo.write("\n")
    add_archivo.close
    
#Opcion 2    
def eliminar_contacto():
    eliminar_contacto = input("Nombre a eliminar: ")
    
    add_archivo = open('contactos.txt')
    lista_contactos = []             #lista bidimensional donde se almacenarán todos los contactos
    for linea in add_archivo:
        valores = linea.strip().split(',')  #se lee línea a línea el archivo 
        lista_contactos.append(valores)       #se añade el contacto a la lista bidimensional 
    add_archivo.close()

    add_archivo = open('contactos.txt', 'w') #se sobreescribe el archivo    
    for contacto in lista_contactos:
        if contacto[0]!=eliminar_contacto:
            add_archivo.write(contacto[0]+","+contacto[1]+","+contacto[2]+","+contacto[3]+"\n")
    add_archivo.close()
    
#Opcion 3
def buscar_contactos():
    nombre_buscar = input("Apellido a buscar: ")
    add_archivo = open('contactos.txt')
    for linea in add_archivo:
        valores = linea.strip().split(',')  #se lee línea a línea el archivo
        if valores[1]==nombre_buscar:
            print(valores[0]+" "+valores[1]+" "+valores[2]+" "+valores[3])
    add_archivo.close()
    
#Opcion 4  
def listado_contactos():
    leer_archivo = open("contactos.txt") 
    for linea in leer_archivo:
        lista = linea.strip().split(",")      
        print(lista[0]+" "+lista[1]+" "+lista[2]+" "+lista[3])
    leer_archivo.close
  
    
#Main
archivo = "contactos.txt"
salir = False
op = 0
while (salir==False):
    print()
    print("MENÚ DE CONTACTOS")
    print("◤-------------------------------◥")
    print("1.-Ingresar un nuevo contacto")
    print("2.-Eliminar un contacto")
    print("3.-Buscar datos por el apellido")
    print("4.-Ver todos los contactos")
    print("5.-Salir")
    print("◣-------------------------------◢")
    op = int(input("Elija opción: "))
    if(op==5): 
        salir=True
        print()
        print("Saliendo...")
    elif (op==1):
        agregar_contacto()
    elif (op==2):
        eliminar_contacto()
    elif (op==3):
        buscar_contactos()    
    elif (op==4):
        listado_contactos()
    else:
        print("Opcion Inválida, intente nuevamen")