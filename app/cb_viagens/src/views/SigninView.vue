<script lang="ts">
// Components
import Art from '@/components/signIn/Art.vue'
// Functions
import { checkUsername, checkPassword } from '@/utils/checkInputs'

export default {
  components: { Art },
  data() {
    return {
      message: 'Digite suas credenciais',
      username: '',
      password: ''
    }
  },
  methods: {
    setMessage(value: string): void {
      this.message = value
    },
    checkInputs() {
      // Checks all required inputs in login process, before submit
      const usernameInput = this.$refs.username as HTMLInputElement
      const passwordInput = this.$refs.password as HTMLInputElement

      if (!checkUsername(usernameInput, this.setMessage)) {
        return false
      }

      if (!checkPassword(passwordInput, this.setMessage)) {
        return false
      }

      return true
    },
    async submitForm() {
      if (!this.checkInputs()) return

      this.message = 'Conferindo dados...'

      // Request settings
      const usernameInput = this.$refs.username as HTMLInputElement
      const passwordInput = this.$refs.password as HTMLInputElement

      const forms = {
        username: usernameInput.value,
        password: passwordInput.value
      }

      const options = {
        method: 'POST',
        body: JSON.stringify(forms),
        headers: {
          'Content-type': 'application/json; charset=UTF-8'
        }
      }

      try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/auth/token/login/`, options)

        // If login is incorrect, Djoser (used in backend) returns 401
        if (!res.ok) {
          this.message = 'Senha ou usuário incorretos'
        }

        const data = await res.json()

        const token = data.auth_token
        const store = this.$store as any

        // Stores my access token for future requests
        store.commit('setToken', token)
        localStorage.setItem('token', token)

        if (token) {
          this.$router.push('dashboard')
        } else {
          this.message = 'Senha ou usuário incorretos'
        }
      } catch (error) {
        this.message = 'Erro ao fazer login'

        console.error(error)
      }
    }
  },
  beforeCreate() {
    document.title = 'Sign In'
  }
}
</script>

<template>
  <div class="page">
    <!-- Art and Login section -->
    <div class="container">
      <!-- Placed on the left -->
      <div class="forms_section">
        <img class="logo" src="../assets/logo.png" />

        <form class="inputs" @submit.prevent="submitForm">
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

          <span 
            class="forgot" 
            @click="setMessage('Ainda não disponível')"
            >Esqueceu a senha?
          </span>

          <span class="message">{{ message }}</span>
          <button class="signin" type="submit">Entrar</button>
        </form>

        <span class="signup" @click="$router.push('/signup')">Registrar</span>
      </div>

      <!-- Only decorative -->
      <Art />
    </div>
  </div>
</template>

<style scoped>
.page {
  width: 100vw;
  width: 100dvw;
  height: 100vh;
  height: 100dvh;

  display: flex;
  justify-content: center;
  align-items: center;
}

/** Inputs Section */
.container {
  display: flex;
  max-width: 60%;
  background-color: #cceaf7;
  color: white;

  border-radius: 1.5rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);

  overflow: hidden;
  user-select: none;
}

.forms_section {
  flex: 1 1 45%;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;

  padding: 3rem 2rem;

  background-color: var(--primary-color);

  border-top-right-radius: 1.5rem;
  border-bottom-right-radius: 1.5rem;
}

.forms_section * {
  width: 100%;
}

.logo {
  max-width: 80%;
  max-height: 100%;

  margin-bottom: 1.7rem;
}

.forms_section .inputs {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  text-align: start;
}

.forms_section .inputs label {
  margin-top: 0.8rem;
  font-size: 1rem;
  font-weight: bold;
}

.forms_section .inputs input {
  font-size: 1rem;
  font-weight: 600;
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;

  user-select: text;
}

.forms_section .inputs .forgot {
  font-weight: bold;
  cursor: pointer;

  margin-top: 0.8rem;
}

/** Message and buttons */
.message {
  text-align: center;
  font-weight: bold;
  margin-top: 0.5rem;

  user-select: text;
}

.signin,
.signup {
  cursor: pointer;
}

.signin {
  font-weight: bold;
  font-size: 1.3rem;
  color: white;

  width: 12rem;

  padding: 0.5rem 2rem;
  margin-top: 0.8rem;
  margin-bottom: 0.25rem;

  border-radius: 999px;
  border: none;
  background-color: black;

  transition: background-color 0.5s;
}

.signin:hover {
  background-color: lightgray;
}

.signup {
  color: white;
  font-weight: 600;

  margin-top: 0.3rem;

  transition: color 0.5s;
}

.signup:hover {
  color: rgb(216, 216, 216);
}

/** */
@media (max-width: 1000px) {
  .signin {
    width: 9rem;
  }
}

@media (max-width: 900px) or (orientation: portrait) or (max-height: 550px) {
  .container {
    flex: 1;
    align-self: stretch;
    max-width: 100%;
    border-radius: 0;
  }

  .forms_section {
    padding-inline: 10%;
    border-radius: 0;
  }

  .message {
    margin-top: 2rem;
  }

  .svg_section {
    display: none;
  }
}

@media (max-height: 550px) and (orientation: landscape) {
  .page {
    background-color: var(--primary-color);
  }

  .container {
    max-width: 60%;
    box-shadow: none;
  }
}
</style>
