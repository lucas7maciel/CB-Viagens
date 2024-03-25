# Servidor do site da CB Viagens feito com Django!
Nele podemos manusear e conferir as informações das viagens armazenadas em um banco de dados PostgreSQL

## Requerimentos
- Python;
- PostgreSQL;

## Rotas
- /trips (GET) (city, date)                 | Retorna as viagens filtradas;
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
### Passo 1: Variáveis de Ambiente
Para que o servidor se conecte ao seu banco de dados, é necessário que suas credenciais sejam informadas. Para isto, crie um arquivo .env na raíz do projeto e preencha com as seguintes informações:

```
SECRET_KEY=<sua_secret_key>
DB_NAME=<nome_do_banco>
DB_USER=<username_do_banco>
DB_PASSWORD=<senha_do_banco>
DB_HOST=<host_do_banco>
DB_PORT=<port_do_banco>
```

### Passo 2: Instale as Dependências
Na raíz do projeto, abra o prompt de comandos e execute a seguinte linha:

```
pip install -r requirements.txt
```

Este comando irá instalar todas as dependências listadas no arquivo **requirements.txt**, que serão necessárias para executar o projeto.

### Passo 3: Ligue o servidor
Para executar o servidor, execute o seguinte comando
```
py manage.py runserver <port_desejada>
```