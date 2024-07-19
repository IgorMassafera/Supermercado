from Funcionario import Funcionario
import mysql.connector
from mysql.connector import Error

class controllerFuncionario:
    def __init__(self):
        pass

    def cadastrarFuncionario(self, nome, siape, connection):
        try:
            if connection.is_connected():
                cursor = connection.cursor()

                sql_query = "insert into Funcionario(nome, siape) values(%s, %s)"
                valores = (nome, siape)

                cursor.execute(sql_query, valores)
                connection.commit()

                print("Funcionário inserido com sucesso!")

        except Error as e:
            print(e)
    
    def imprimirFuncionario(self, siape, connection):
        try:
            if connection.is_connected():
                cursor = connection.cursor()

                if siape == '':
                    sql_query = "select* from Funcionario"
                    cursor.execute(sql_query)

                else:    
                    sql_query = "select* from Funcionario where siape = %s"
                    valores = ([siape])
                    cursor.execute(sql_query, valores)

                resultados = cursor.fetchall()

                for r in resultados:
                    print(r)

        except Error as e:
            print(e)