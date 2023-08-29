from psycopg2 import pool
from logger_base import log
import sys

class conexion:
   _DATABASE='usuarios'
   _USER='postgres'
   _PASSWORD='Admin'
   _DB_PORT='5432'
   _HOST='localhost'
   _MIN_CON=1
   _MAX_CON=5
   _POOL=None

   @classmethod
   def get_conn(cls):
      conn = cls.get_pool().getconn()
      log.debug(f'Conexion exitosa {conn}')
      return conn
   
   @classmethod
   def get_pool(cls):
      if cls._POOL is None:
         try:
            log.info('Creando Pool de conexiones')
            cls._POOL = pool.SimpleConnectionPool (cls._MAX_CON,
                                                   cls._MIN_CON,
                                                   host=cls._HOST,
                                                   port=cls._DB_PORT,
                                                   database=cls._DATABASE,
                                                   user=cls._USER,
                                                   password=cls._PASSWORD)
            log.debug(f'Creacion exitosa del pool: {cls._POOL}')
            return cls._POOL
         except Exception as e:
            log.error("Error al crear el pool",e," ",sys.exc_info()[0])
      else:
         return cls._POOL
      
   @classmethod
   def free_conn(cls, conexion):
      cls.get_pool().putconn(conexion)
      log.debug(f'Regresamos la conexion del pool: {conexion}')

   @classmethod
   def close_conn(cls):
      cls.get_pool().closeall()
   

if __name__=='__main__':
   print ('Test de Conexión a la base de datos...')
   conexion1 = conexion.get_conn()
 