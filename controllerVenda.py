from Venda import Venda
from Produto import Produto
from Funcionario import Funcionario
from Cliente import Cliente
import mysql.connector
from mysql.connector import Error

class controllerVenda:
    def __init__(self):
        pass

    def cadastrarVenda(self, cpf, siape, codigo, quantidade, connection):
        try:
            if connection.is_connected():
                cursor = connection.cursor()

                sql_query = "select quantidade from Produto where codigo = %s"
                valores = ([codigo])
                cursor.execute(sql_query, valores)
                resultado = cursor.fetchall()
                resultado = ''.join(map(str, resultado))
                resultado = resultado[1:len(resultado)-2]
                resultado = int(resultado)
                
                if(int(quantidade) <= resultado):

                    sql_query = "insert into Venda(cpf, siape, codigo, quantidade) values(%s, %s, %s, %s)"
                    valores = (cpf, siape, codigo, quantidade)

                    cursor.execute(sql_query, valores)
                    connection.commit()

                    print("Venda cadastrada com sucesso!")

                    sql_query = "update Produto set quantidade = %s where codigo = %s"
                    valores = (resultado-int(quantidade), codigo)
                    cursor.execute(sql_query, valores)
                    connection.commit()

                else:
                    print("Quantidade insuficiente em estoque!")

        except Error as e:
            print(e)
    
    def imprimirVenda(self, cpf, siape, connection):
        try:
            if connection.is_connected():
                cursor = connection.cursor()

                if cpf == '':
                    sql_query = "select* from Venda"
                    cursor.execute(sql_query)

                else:    
                    sql_query = "select* from Venda where cpf = %s and siape = %s"
                    valores = ([cpf, siape])
                    cursor.execute(sql_query, valores)

                resultados = cursor.fetchall()

                for r in resultados:
                    print(r)

        except Error as e:
            print(e)