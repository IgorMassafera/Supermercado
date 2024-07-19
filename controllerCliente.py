from Cliente import Cliente
import mysql.connector
from mysql.connector import Error

class controllerCliente:
    def __init__(self):
        pass

    def cadastrarCliente(self, nome, cpf, connection):
        try:
            if connection.is_connected():
                cursor = connection.cursor()

                sql_query = "insert into Cliente(nome, cpf) values(%s, %s)"
                valores = (nome, cpf)

                cursor.execute(sql_query, valores)
                connection.commit()

                print("Cliente inserido com sucesso!")

        except Error as e:
            print(e)
    
    def imprimirCliente(self, cpf, connection):
        try:
            if connection.is_connected():
                cursor = connection.cursor()

                if cpf == '':
                    sql_query = "select* from Cliente"
                    cursor.execute(sql_query)

                else:    
                    sql_query = "select* from Cliente where cpf = %s"
                    valores = ([cpf])
                    cursor.execute(sql_query, valores)

                resultados = cursor.fetchall()

                for r in resultados:
                    print(r)

        except Error as e:
            print(e)