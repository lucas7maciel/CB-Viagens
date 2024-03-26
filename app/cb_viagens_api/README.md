# Servidor do site da CB Viagens feito com Django!
Nele podemos manusear e conferir as informações das viagens armazenadas em um banco de dados PostgreSQL

## Requerimentos
- Python;

## Rotas
- /trips (GET) (city, date)                 | Retorna as viagens filtradas;
- /trips/cities (GET)                       | Retorna todas as cidades disponíveis;
- /trips/book (POST) (customer, trip)       | Associa uma viagem a um cliente;
- /auth/users (POST) (username, password)   | Registra um usuário
- /auth/login/ (POST) (username, password)  | Realiza o login do usuário

## Models
Alguns dos modelos utilizados nas tabelas

### Trips
```
id : number (pr)
name : CharField(max_length=40)
price_confort : CharField(max_length=15)
price_econ : CharField(max_length=15)
city : CharField(max_length=40)
duration : CharField(max_length=10)
seat : CharField(max_length=3)
bed : models.CharField(max_length=3)

customerId : IntegerField(blank=True, null=True)
```

### Users
```
firstname : CharField(max_length=30)
lastname : CharField(max_length=30)
username : CharField(max_length=50)
email : charField(max_length=100)
last_loged : DateField()
```

## Como Executar
### Passo 1: Instale as Dependências
Na raíz do projeto, abra o prompt de comandos e execute a seguinte linha:

```
pip install -r requirements.txt
```

Este comando irá instalar todas as dependências listadas no arquivo **requirements.txt**, que serão necessárias para executar o projeto.

### Passo 2: Execute as migrações
```
py manage.py migrate
```
_Necessário apenas na primeira vez_

### Passo 3: Popule o banco de dados
```
py manage.py loaddata path/to/json/data.json
# Se você baixou o repositório inteiro, path = ../data.json
# Caso contrário, baixe-o em /apps
```
_Necessário apenas na primeira vez_

### Passo 4: Ligue o servidor
Para executar o servidor, execute o seguinte comando
```
py manage.py runserver 3000
```
