# DataOps Montadora de Veiculo

Este repositório contém um script em Python para realizar a criação e agregação de dados em um banco de dados MongoDB. O script utiliza a biblioteca Pandas para manipulação dos dados e a biblioteca PyMongo para interação com o MongoDB.

# Passos para Execução
## 1. Criação do Ambiente Local MongoDB
Instale o MongoDB localmente em sua máquina e crie duas coleções: "Carros" e "Montadoras". Você pode utilizar o MongoDB Compass ou outra interface de sua preferência para gerenciar os dados.

## 2. Criação dos Pandas Dataframes
O script Python contém a criação de dois Pandas Dataframes, um para armazenar informações sobre carros e outro para armazenar informações sobre montadoras.

## 3. Salvando os Pandas Dataframes no MongoDB
Os Pandas Dataframes criados anteriormente serão salvos nas coleções correspondentes no MongoDB. Para fazer isso, o script estabelece uma conexão com o MongoDB usando a biblioteca PyMongo e persiste as informações nas coleções "Carros" e "Montadoras".

## 4. Criando Agregação no MongoDB
Com os dados salvos no MongoDB, o próximo passo é criar uma agregação que relaciona as coleções "Carros" e "Montadoras" com base no campo "Montadora". O objetivo é extrair informações sobre o país de cada montadora e apresentar os resultados.

## 5. Agrupando Informações
Dentro da mesma agregação criada no passo anterior, as informações dos carros serão agrupadas pelo campo "País" da montadora. O resultado será inserido em um elemento chamado "Carros".
