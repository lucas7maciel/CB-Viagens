<script lang="ts">
// Components
import Intro from '@/components/signUp/Intro.vue'
// Types
import { type Router } from 'vue-router'
// Functions
import {
  checkUsername,
  checkPassword,
  checkFirstName,
  checkLastName,
  confirmPassword
} from '@/utils/checkInputs'
import { translateError } from '@/utils/translateError'
import { apiURL } from '@/utils/authData'

export default {
  components: {
    Intro
  },
  data() {
    return {
      message: 'Digite suas credenciais'
    }
  },
  methods: {
    setMessage(value: string): void {
      this.message = value
    },
    checkInputs(): boolean {
      // Checks if inputs are correctly filled before submitting
      const firstnameInput = this.$refs.firstname as HTMLInputElement
      const lastnameInput = this.$refs.lastname as HTMLInputElement
      const usernameInput = this.$refs.username as HTMLInputElement
      const passwordInput = this.$refs.password as HTMLInputElement
      const confirmInput = this.$refs.confirm as HTMLInputElement

      if (!checkFirstName(firstnameInput, this.setMessage)) {
        return false
      }

      if (!checkLastName(lastnameInput, this.setMessage)) {
        return false
      }

      if (!checkUsername(usernameInput, this.setMessage)) {
        return false
      }

      if (!checkPassword(passwordInput, this.setMessage)) {
        return false
      }

      if (!confirmPassword(passwordInput.value, confirmInput, this.setMessage)) {
        return false
      }

      return true
    },
    navigate(route: string) {
      ;(this.$router as Router).push(route)
    },
    async submitForm() {
      if (!this.checkInputs()) return

      this.message = 'Enviando dados...'

      // Gets input data
      const usernameInput = this.$refs.username as HTMLInputElement
      const passwordInput = this.$refs.password as HTMLInputElement
      const frstnameInput = this.$refs.firstname as HTMLInputElement
      const lastnameInput = this.$refs.lastname as HTMLInputElement

      const forms = {
        username: usernameInput.value,
        password: passwordInput.value,
        first_name: frstnameInput.value,
        last_name: lastnameInput.value
      }

      const options: object = {
        method: 'POST',
        body: JSON.stringify(forms),
        headers: {
          'Content-type': 'application/json; charset=UTF-8'
        }
      }

      try {
        const res = await fetch(`${import.meta.env.VITE_API_URL || apiURL}/auth/users/`, options)
        const data: Object = await res.json()

        if (Object.hasOwnProperty.call(data, 'success')) {
          this.message = 'Usuário criado com sucesso!'
        } else {
          const errors: Array<string> = Object.values(data)[0]

          this.message = translateError(errors[0])
        }
      } catch (error) {
        this.message = 'Falha ao registrar usuário'

        console.error(error)
      }
    }
  },
  beforeCreate() {
    document.title = 'Sign Up'
  }
}
</script>

<template>
  <div class="container">
    <!-- Only decorative (propaganda) -->
    <Intro />

    <!-- Sign up section -->
    <div class="inputs">
      <h1>Registrar</h1>
      <h2>Digite suas credenciais para que possamos registrá-lo no sistema</h2>

      <form class="forms" @submit.prevent="submitForm">
        <div class="name">
          <div>
            <label>Nome</label><br />
            <input 
              ref="firstname" 
              type="text" 
              placeholder="Digite seu nome" 
            />
          </div>
          <div>
            <label>Sobrenome</label><br />
            <input 
              ref="lastname" 
              type="text" 
              placeholder="Digite seu sobrenome" 
            />
          </div>
        </div>

        <label>Username</label>
        <input 
          ref="username" 
          type="text" 
          placeholder="Digite seu username"
        />

        <label>Senha</label>
        <input 
          ref="password" 
          type="password"
          placeholder="Digite sua senha"
        />

        <label>Confirmar Senha</label>
        <input 
          ref="confirm" 
          type="password"
          placeholder="Confirme sua senha" 
        />

        <p class="message">{{ message }}</p>
        <div class="buttons">
          <button class="signup" type="submit">Criar Conta</button>
        </div>

      </form>

      <p 
        @click="navigate('/signin')"
        class="back" 
        >Voltar
      </p>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  align-items: stretch;
  gap: 1rem;

  height: 100vh;
  height: 100dvh;
  width: 100vw;
  width: 100dvw;

  padding: 1rem 1rem;
}

/** General */
h1,
h2,
label,
br {
  user-select: none;
}

/** Sign up section */
.inputs {
  flex: 1;

  display: flex;
  flex-direction: column;
  align-items: stretch;
  justify-content: center;

  padding-inline: 8%;
}

.inputs h1 {
  font-weight: 600;
}

.inputs h2 {
  font-weight: 500;
  font-size: 1.2em;
}

.inputs .forms {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: stretch;

  margin-top: 0.3rem;
}

.inputs .forms .name,
.inputs .forms .buttons {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  column-gap: 1.5rem;
}

.inputs .forms .name div {
  flex: 1 1 40%;
}

.inputs .forms .name div * {
  width: 100%;
}

.inputs .forms label {
  font-weight: 500;

  margin-top: 0.5rem;
  margin-bottom: 0.3rem;
}

.inputs .forms input {
  padding: 0.5rem 0.9rem;
  border-radius: 0.5rem;
}

/** Message and Button */
.message {
  font-weight: bold;
  text-align: center;

  margin-top: 1rem;
}

.signup {
  font-weight: bold;
  font-size: 1.2rem;
  color: white;

  padding: 0.4rem 1.5rem;
  margin-top: 0.7rem;

  border-radius: 3rem;
  border: none;
  background-color: black;

  cursor: pointer;
  transition: background-color 0.5s;

  align-self: center;
  user-select: none;
}

.signup:hover {
  background-color: lightgray;
}

.back {
  font-size: 1rem;
  font-weight: bold;
  margin-top: 0.3rem;
  align-self: center;
  text-align: center;

  cursor: pointer;
  user-select: none;
}

/** Queries */
@media (max-width: 900px) {
  .intro {
    display: none;
  }

  .inputs h1,
  .inputs h2 {
    text-align: center;
  }

  .inputs .forms {
    margin-top: 3rem;
  }

  .message {
    margin-top: 3rem;
    padding-inline: 5%;
  }
}
</style>
