from controllerVenda import controllerVenda, Venda
from controllerProduto import controllerProduto, Produto
from controllerFuncionario import controllerFuncionario, Funcionario
from controllerCliente import controllerCliente, Cliente
from Layout import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error
import sys

def main():
    connection = mysql.connector.connect(
        host='localhost',          # Endereço do servidor MySQL
        user='root',               # Nome de usuário
        password='admin',  # Senha do usuário
        database='SupermercadoDB',   # Nome do banco de dados
        auth_plugin='mysql_native_password'
    )

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, connection)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 