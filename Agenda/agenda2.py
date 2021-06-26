
def get_phone(file, client):

    try:
        f = open(file, 'r')
    except FileNotFoundError:
        return('¡El fichero ' + file + ' no existe!\n')
    else:
        directory = f.readlines()
        f.close()
        directory = dict([tuple(line.split(',')) for line in directory])
        if client in directory:
            return directory[client]
        else:
            return('¡El cliente ' + client + ' no existe!\n')


def add_phone(file, client, telf):

    try:
        f = open(file, 'a')
    except FileNotFoundError:
        return('¡El fichero ' + file + ' no existe!\n')
    else:
        f.write(client + ',' + telf + '\n')
        f.close()
        return('El teléfono ha sido añadido.\n')


def remove_phone(file, client):

    try:
        f = open(file, 'r')
    except FileNotFoundError:
        return('¡El fichero ' + file + ' no existe!\n')
    else:
        directory = f.readlines()
        f.close()
        directory = dict([tuple(line.split(',')) for line in directory])
        if client in directory:
            del directory[client]
            f = open(file, 'w')
            for name, telf in directory.items():
                f.write(name + ',' + telf)
            f.close()
            return ('¡El cliente ha sido borrado!\n')
        else:
            return('¡El cliente ' + client + ' no existe!\n')


def create_directory(file):

    import os
    if os.path.isfile(file):
        answer = input('El fichero ' + file +
                       ' ya existe. ¿Desea vaciarlo (S/N)? ')
        if answer == 'N':
            return 'No se ha creado el fichero porque ya existe.\n'
    f = open(file, 'w')
    f.close()
    return 'Se ha creado el fichero.\n'


def menu():

    print('Gesión del listín telefónico')
    print('============================')
    print('1 - Consultar un teléfono')
    print('2 - Añadir un teléfono')
    print('3 - Eliminar un teléfono')
    print('4 - Crear el listín')
    print('0 - Terminar')
    option = input('Introduzca el número de la opción deseada: ')
    return option


def directory():

    file = 'listin.txt'
    while True:
        option = menu()
        if option == '1':
            name = input('Introduce el nombre del cliente: ')
            print(get_phone(file, name))
        elif option == '2':
            name = input('Introduce el nombre del cliente: ')
            telf = input('Introduce el teléfono del cliente: ')
            print(add_phone(file, name, telf))
        elif option == '3':
            name = input('Introduce el nombre del cliente: ')
            print(remove_phone(file, name))
        elif option == '4':
            print(create_directory(file))
        else:
            break
    return


directory()
