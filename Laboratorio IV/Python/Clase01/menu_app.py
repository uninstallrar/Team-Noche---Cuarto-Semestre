from usuario_dao import *

option = None

while option != 5:
    print("\t Opciones")
    print("""
        1- Lista de usuarios
        2- Agregar usuario
        3- Modificar usuario
        4- Eliminar usuario
        5- Salir
    """)
    option = int(input('Digite la opcion: '))
    if option == 1:
        #Listar Usuarios
        usuarios = usuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
        
    elif option == 2:
        #Insertar usuario
        name=input('Ingrese el nombre del usuario: ')
        password=input('Digite la clave: ')
        usuario = Usuario(username=name, password=password)
        usuario_agregado = usuarioDAO.insertar(usuario)
        log.info(f'Usuario agregado: {usuario_agregado}')

    elif option == 3:
        #Modificar usuario
        id = int(input('Digite el ID del ario a modificar: '))
        name = input('Digite el nombre del usuario: ')
        password = input('Digite la clave: ')
        usuario = Usuario(id_usuario=id, username=name, password=password)
        usuario_modificado = usuarioDAO.actualizar(usuario)
        log.info(f'Usuario modificado: {usuario_modificado}')

    elif option == 4:
        #Eliminar usuario
        id = int(input('Digite el ID del usuario a eliminar: '))
        usuario = Usuario(id_usuario=id)
        usuario_eliminado = usuarioDAO.eliminar(usuario)
        log.info(f'Usuario eliminado: {usuario_eliminado}')

    elif option == 5:
        print('Hasta pronto')
        break

    else:
        print("\n\t Opción incorrecta \n")
    