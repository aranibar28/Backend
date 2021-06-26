import os
import time
import json


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Persona:
    def __init__(self, nombre, sexo, dni):
        self.nombre = nombre
        self.sexo = sexo
        self.dni = dni


class Empleado(Persona):
    def __init__(self, nombre, sexo, dni, codEmpleado=0):
        super().__init__(nombre, sexo, dni)
        if codEmpleado == 0:
            self.codEmpleado = self.codEmpleado + 1
        else:
            self.codEmpleado = codEmpleado

    def __str__(self) -> str:
        return self.nombre + " ---- " + str(self.codEmpleado)

    def toDic(self):
        d = {
            "nombre": self.nombre,
            "sexo": self.sexo,
            "dni": self.dni,
            "codEmpleado": self.codEmpleado
        }
        return d


class Archivo:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo

    def leerArchivo(self):
        try:
            file = open(self.nombreArchivo, 'r')
            return file.read()
        except Exception as e:
            return e

    def borrarArchivo(self):
        directorioActual = os.getcwd()
        path = directorioActual+"\\"+self.nombreArchivo
        print(path)
        if(os.path.isfile(path)):
            try:
                os.remove(path)
                print("removiendo archivo")

            except Exception as error:
                print(error)

    def escribirArchivo(self, linea):
        try:
            directorioActual = os.getcwd()
            path = directorioActual+"\\"+self.nombreArchivo
            if(os.path.isfile(path)):
                try:
                    #escribir el archiv
                    file = open(self.nombreArchivo, 'a')
                    file.write(linea + "\n")
                except Exception as e:
                    print(e)
                finally:
                    file.close()
            else:
                file = open(self.nombreArchivo, 'w')
                file.close()
                file = open(self.nombreArchivo, 'a')
                file.write(linea + "\n")
        except Exception as error:
            print(error)


print("Sistema de Asistencia")
print("=====================")

listaEmpleados = []
listaEmpleadosDic = []
listaAsistencia = []
fileEmpleado = Archivo("personas.txt")

while True:
    opMenu = int(
        input("\n◤--------------◥" +
              "\n 1 = Usuario" +
              "\n 2 = Asistencia" +
              "\n 3 = Reporte" +
              "\n 9 = Salir" +
              "\n◣--------------◢" +
              "\n -> "))
    if opMenu == 9:
        print("\nSaliendo...")
        break
    elif opMenu == 1:
        opEmpleado = int(
            input("\n◤--------------◥" +
                  "\n 1 = Agregar Usuario" +
                  "\n 2 = Buscar Usuario" +
                  "\n 3 = Quitar Usuario" +
                  "\n 9 = Listar Usuario" +
                  "\n◣--------------◢" +
                  "\n -> "))
        if opEmpleado == 9:
            print("\nSaliendo...")
            break
        elif opEmpleado == 1:
            nombre = input("\nEscribe tu nombre: ")
            sexo = input("Escribe tu sexo [ M - F ]: ")
            dni = input("Escribe tu DNI: ")
            empleado = Empleado(nombre, sexo, dni, 3)
            listaEmpleados.append(empleado)
            listaEmpleadosDic.append(empleado.toDic())
            jsonString = json.dumps(listaEmpleadosDic)
            fileEmpleado.borrarArchivo()
            fileEmpleado.escribirArchivo(jsonString)
            print("\nUsuario Agregado")
        elif opEmpleado == 2:
            print(listaEmpleados)
