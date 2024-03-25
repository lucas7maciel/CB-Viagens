# Frontend da CB Viagens feito com Vue.js!
Com esta interface podemos conferir e manusear as informações guardadas no servidor!

## Páginas
- Landing Page - "/";
- Página de login - "/signin";
- Página de cadastro - "/signup";
- Dashboard - "/dashboard"
- Calculate Trip - (Seção do dashboard);
- Minhas Viagens - (Seção do dashboard);
- Sobre Nós - (Seção do dashboard);

## Requerimentos
- Node.js;
- Npm / Yarn;
- Vue Cli;

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

### Passo 1: Setup

```sh
npm install
```

### Passo 2: Compilar e Hot-Reload (Desenvolvimento)

```sh
npm run dev
```

### Passo 3: Type-Check, Compilar e Minificar (Produção)

```sh
npm run build
```

### Lint com [ESLint](https://eslint.org/)

```sh
npm run lint
```
