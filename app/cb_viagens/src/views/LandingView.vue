<script lang="ts">
import Guy from '@/assets/LandingSvg.vue'
export default {
  components: {
    Guy
  },
  methods: {
    signin() {
      this.$router.push('/signin')
    }, handleKeyboard(e: KeyboardEvent) {
      if (e.key === 'Enter' || e.key === ' ') {
        this.signin()
      }
    }
  },
  beforeCreate() {
    document.title = 'Home'
  }, mounted() {
    document.addEventListener("keydown", this.handleKeyboard)
  }, beforeUnmount() {
    document.removeEventListener("keydown", this.handleKeyboard)
  }
}
</script>

<template>
  <div class="container">
    <div class="intro">
      <h1 class="title">Amplie seu mundo.</h1>
      <h2 class="subtitle">
        Encontre as melhores ofertas para realizar a sua viagem ideal conosco.
      </h2>
      <button class="signin" @click="signin">Entrar</button>
      <div class="logo">
        <img src="../assets/logo.png" />
      </div>
    </div>
    <div class="art"><Guy class="guy" /></div>
  </div>
</template>

<style scoped>
.container {
  height: 100vh;
  height: 100dvh;
  width: 100vw;
  width: 100dvw;

  display: flex;
  align-items: stretch;

  background-color: var(--primary-color);
  color: white;

  user-select: none;
  overflow: hidden;
}

.container .intro,
.container .art {
  flex: 1;
}

/**Intro */
.intro {
  display: flex;
  align-items: start;
  justify-content: center;
  flex-direction: column;

  padding: 2rem 3rem 0.5rem 3rem;

  animation: show_intro 0.8s both;
  animation-delay: 0.5s;
}

@keyframes show_intro {
  0% {
    transform: translateY(-3rem);
    opacity: 0;
  }

  80% {
    opacity: 1;
  }

  100% {
    transform: translateY(0);
  }
}

.intro .title {
  margin-top: auto;
  font-size: 3rem;
}

.signin {
  font-weight: bold;
  font-size: 1.7rem;
  color: white;

  padding: 0.7rem 2.6rem;
  margin-top: 1.6rem;

  border-radius: 3rem;
  border: none;
  background-color: #05a8b4;

  cursor: pointer;
  transition: background-color 0.5s;

  align-self: center;
}

.signin:hover {
  background-color: #08bbc8;
}

.intro .logo {
  margin-top: auto;
  justify-self: center;
  align-self: center;
}

.intro .logo img {
  max-height: 3rem;
  max-width: 10rem;
}

/**Art */
.art {
  text-align: center;

  display: flex;
  justify-content: end;

  animation: show_art 0.8s both;
}

.art .guy {
  max-width: 100%;
  max-height: 100%;

  align-self: end;

  transform: translateY(1.2rem);
}

@keyframes show_art {
  0% {
    transform: translate(3rem, 1.2rem);
    opacity: 0;
  }

  80% {
    opacity: 1;
  }

  100% {
    transform: translate(0, 1.2rem);
  }
}

/** Media queries */
@media (max-width: 1000px) {
  .container {
    flex-direction: column-reverse;
  }

  .intro {
    align-items: center;
    text-align: center;
  }

  .intro .title, .intro .subtitle, .intro .signin {
    transform: translateY(-3rem);
  }

  .art {
    justify-content: center;

    max-height: 15%;
  }
}

@media (max-width: 300px) {
  .intro .title {
    font-size: 2rem;
  }

  .intro .title, .intro .subtitle, .intro .signin {
    transform: translateY(0);
  }

  .art {
    display: none;
  }
}
</style>
