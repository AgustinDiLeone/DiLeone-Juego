import sqlite3

def sql_table(sentencia):
    with sqlite3.connect("SQL/puntajes.db") as conexion:
        try:
            cursor = conexion.execute(sentencia)
            lista_nombre_puntos = []
            for fila in cursor:
                lista_nombre_puntos.append(fila)
            return lista_nombre_puntos 
        except:
            print('Error!!!')

sentencia = '''
            create table Jugadores
            (
            id integer primary key autoincrement,
            nombre text,
            puntaje integer
            )
            '''
#sql_table(sentencia)

sentencia_2 = '''
            insert into Jugadores(nombre,puntaje) values("pepe",20)
            '''
#sql_table(sentencia_2)
sentencia_2 = '''
            insert into Jugadores(nombre,puntaje) values("dfg",200558)
            '''
#sql_table(sentencia_2)

sentencia_3 = '''
            select nombre,puntaje
            from Jugadores
            order by puntaje desc limit 2
            '''
#print(sql_table(sentencia_3))
sentencia_3 = '''
            select nombre, puntaje
            from Jugadores
            '''
#print(sql_table(sentencia_3))

sentencia_4 = '''
            update  Jugadores
            set puntaje = 98745
            where nombre = "Juan"
            '''
#sql_table(sentencia_4)

sentencia_5 = '''
            delete from  Jugadores
            
            '''
#sql_table(sentencia_5)

sentencia = '''
            create table Jugadores
            (
            id integer primary key autoincrement,
            nombre text,
            puntaje integer
            )
            '''
    #sql_table(sentencia)
sentencia_1 = '''
            insert into Jugadores(nombre,puntaje) values("pepe",20)
            '''
#sql_table(sentencia_1)
sentencia_2 = '''
                    insert into Jugadores(nombre,puntaje) values("jhthgchc",798858548)
                    '''
#sql_table(sentencia_2)
sentencia_3 = '''
            insert into Jugadores(nombre,puntaje) values("pepe",20)
            '''
#sql_table(sentencia_3)

