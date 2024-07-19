Autor: Igor Massafera, graduando em Engenharia da Computação pela UNIVERSIDADE FEDERAL DE ITAJUBÁ - UNIFEI, nono período.

Trabalho final de Tópicos Especiais em Computação - ECO921

Objetivo: Realizar um software na linguagem Python para simular o funcionamento de um supermercado usando o modelo MVC(Model View Control) em programação orientada a objetos. 
O sistema deve contar com uma interface gráfica e um banco de dados para armazenar os dados. Foi utilizado o QTDesigner (biblioteca PYQT5) para modelagem da interface gráfica.
Já para o banco de dados foi utilizado o MYSQL, para fazer a conexao com o sistema foi usado a biblioteca MYSQL-Connector.

Requisitos:  Um software de gerenciamento de supermercado 
. Crie um software que possua cadastro de clientes, funcionários, produtos e vendas; 
. É necessário manter um estoque de produtos; 
. Quando um cliente compra um produto, é necessário criar uma venda; 
. A venda possui um cliente, um funcionário responsável pela venda e uma lista de 
produtos; 
. Quando uma venda é realizada, é necessário diminuir as quantidades dos produtos 
comprados em estoque; 
. É necessário então manter registro das vendas para conferências, caso necessário; 

Funcionamento: A classe Cliente conta com os atributos nome e cpf;
	       A classe Funcionário tem nome e siape como atributos;
	       A classe produto tem os atributos nome, quantidade e código(int);
	       A classe Venda tem um cpf do cliente, um siape do funcionario, o código e quantidade do produto;

Cada classe tem uma classe Controller para sua manipulação, com métodos de cadastrar e imprimir.

CPF(Cliente), SIAPE(Funcionário) e Código(Produto) sao chaves primárias do banco de dados e não podem ser repetidas.

A interface permite adicionar clientes, funcionarios, produtos e vendas, cada um com seus respectivos atributos. Ao clicar em cadastrar o objeto é inserido no banco de dados por meio do método Cadastrar, implementado nas classes Controller.
Para realizar uma busca no banco de dados basta digitar a chave primária a ser buscada e clicar no botão Buscar. Caso nao seja informado nenhuma chave primária(CPF, SIAPE CÓDIGO) o banco retorna todos elementos cadastrados.
