# Frontend da CB Viagens feito com Vue.js!
Com esta interface podemos conferir e manusear as informações guardadas no servidor!

## Requerimentos
- Node.js;
- Npm / Yarn;
- Vue Cli;

## Páginas
- Landing Page - "/";
- Página de login - "/signin";
- Página de cadastro - "/signup";
- Dashboard - "/dashboard"
- Calculate Trip - (Seção do dashboard);
- Minhas Viagens - (Seção do dashboard);
- Sobre Nós - (Seção do dashboard);

## Bibliotecas Utilizadas
- vue-datepicker: ^8.3.1;
- axios: ^1.6.8;
- pinia: ^2.1.7;
- vue: ^3.4.21;
- vue-router: ^4.3.0;
- vuex: "^4.0.2";

## Como Executar
_O projeto está sendo executado na port 8080, caso tenha outra preferência, altere em vite.config.ts_
Para executar o projeto inteiro (backend e frontend), você pode executar /app/run.sh ou seguir este passo a passo (apenas front).

### Passo 1: Defina as Variáveis de Ambiente
Para que a aplicação possa ter acesso aos dados do servidor, é necessário que seu url seja específicado para que as requests sejam feitas. Crie um arquivo **.env** na raiz do projeto para que isto seja feito;

```
VITE_API_URL=<url_da_sua_api>
```

### Passo 2: Setup

```sh
# Só é necessário executar este comando na primeira vez
npm install
```

### Passo 3: Compilar e Hot-Reload (Desenvolvimento)

```sh
npm run dev
```

### Passo 4: Type-Check, Compilar e Minificar (Produção)

```sh
npm run build
```

### Lint com [ESLint](https://eslint.org/)

```sh
npm run lint
```
