from Produto import Produto
import mysql.connector
from mysql.connector import Error

class controllerProduto:
    def __init__(self):
        pass

    def cadastrarProduto(self, nome, codigo, quantidade, connection):
        try:
            if connection.is_connected():
                cursor = connection.cursor()

                sql_query = "insert into Produto(nome, codigo, quantidade) values(%s, %s, %s)"
                valores = (nome, codigo, quantidade)

                cursor.execute(sql_query, valores)
                connection.commit()

                print("Produto inserido com sucesso!")

        except Error as e:
            print(e)
    
    def imprimirProduto(self, codigo, connection):
        try:
            if connection.is_connected():
                cursor = connection.cursor()

                if codigo == '':
                    sql_query = "select* from Produto"
                    cursor.execute(sql_query)

                else:    
                    sql_query = "select* from Produto where codigo = %s"
                    valores = ([codigo])
                    cursor.execute(sql_query, valores)

                resultados = cursor.fetchall()

                for r in resultados:
                    print(r)

        except Error as e:
            print(e)