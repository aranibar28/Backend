import os
import shutil
from typing import final

print("Manejo de archivos en Python")
# os.makedirs("MiPrimeraCarpeta")
# path = os.getcwd()
# print(path)
# os.removedirs(path+'''/'''+"MiPrimeraCarpeta")
# listaDirectorio = os.listdir(".")
# print(listaDirectorio)
# origen = path+'''/'''+"MiPrimeraCarpeta/archivo.txt"
# destino = path
# shutil.copy(origen, destino)

try:
    file = open("archivo.txt", "r")
    print(file.read())
except Exception as ex:
    print(ex)
finally:
    file.close()

try:
    file = open("archivo.txt", "r")
    for linea in file.readlines():
        print(linea)
        if linea == "linea 3":
            print("Encontre el dato buscado")
except Exception as ex:
    print(ex)
finally:
    file.close()

try:
    file = open("MiPrimeraCarpeta/archivo1.txt", "a")
    file.write("\n")
    for item in range(0,10,1):
        file.write("Estoy escrbiendo desde python "+str(item))
        file.write("\n")
except Exception as ex:
    print(ex)
finally:
    file.close()