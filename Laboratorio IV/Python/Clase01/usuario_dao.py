from usuario import Usuario
from cursor_del_pool import CursorDelPool
from logger_base import log

class usuarioDAO:
    
    """
    DAO = Data Access Object para la tabla de usuarios
    CRUD = Create - Read - Update - Delete 
    """

    _SELECT = 'SELECT * FROM usuarios ORDER BY id_usuario'
    _INSERT = 'INSERT INTO usuarios (username, password) VALUES (%s, %s)'
    _UPDATE = 'UPDATE usuarios SET username = %s, password = %s WHERE id_usuario = %s'
    _DELETE = 'DELETE FROM usuarios WHERE id_usuario = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionamos usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios=[]
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
    
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores=(usuario.username, usuario.password)
            cursor.execute(cls._INSERT, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a actualizar: {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._UPDATE, valores)
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a eliminar: {usuario}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._DELETE, valores)
            return cursor.rowcount


if __name__ == '__main__':
    #Eliminar usuario
    #usuario = Usuario(id_usuario=4)
    #usuario_eliminado = usuarioDAO.eliminar(usuario)
    #log.debug(f'Usuario eliminado: {usuario_eliminado}')

    #Modificar usuario
    #usuario = Usuario(id_usuario=4, username='maria', password='159753')
    #usuario_modificado = usuarioDAO.actualizar(usuario)
    #log.debug(f'Usuario modificado: {usuario_modificado}')

    #Insertar usuario
    #usuario = Usuario(username='maria', password='111111')
    #usuario_agregado = usuarioDAO.insertar(usuario)
    #log.debug(f'Usuario agregado: {usuario_agregado}')
    
    #Listar Usuarios
    usuarios = usuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
