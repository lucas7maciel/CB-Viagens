<script lang="ts">
import PlaneIcon from '../icons/IconPlane.vue'

export default {
  components: {
    PlaneIcon
  }
}
</script>

<template>
  <div class="intro">
    <div class="logo">
      <p>CB Viagens</p>
      <PlaneIcon class="icon" />
    </div>

    <div class="slogan">
      <h1>Tome novos ares conosco!</h1>
      <h2>Conheça novos lugares, pessoas e sentimentos com nossas promoções</h2>
    </div>
    <p class="alert">* Seus dados serão protegidos</p>
  </div>
</template>

<style scoped>
.intro {
  display: flex;
  align-items: stretch;
  flex-direction: column;

  color: white;
  background-color: #2a3041;
  user-select: none;

  max-width: 30%;

  padding: 1.3rem 1.5rem;

  border-radius: 1rem;

  box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  animation: show_intro 0.7s;
}

.intro .logo {
  display: flex;
  justify-content: start;
  align-items: center;

  animation: show_text 1s both;
  animation-delay: 0.3s;
}

.intro .logo p {
  font-weight: bolder;
  padding-right: 0.5rem;
}

.intro .logo .icon {
  max-width: 0.8rem;
  max-height: 0.8rem;
}

.intro .slogan {
  flex: 1;

  display: flex;
  flex-direction: column;
  align-items: stretch;
  justify-content: center;

  animation: show_text 1s both;
  animation-delay: 0.3s;
}

.intro .slogan h1 {
  font-weight: bolder;
}

.intro .slogan h2 {
  font-weight: 500;
}

.intro .alert {
  font-weight: 500;
  animation: show_text 1s both;
  animation-delay: 0.3s;
}

@keyframes show_intro {
  from {
    max-width: 0%;
  }
  to {
    max-width: 30%;
  }
}

@keyframes show_text {
  0% {
    opacity: 0;
    transform: translateY(-1rem);
  }

  80% {
    transform: translateY(0);
  }

  100% {
    opacity: 1;
  }
}
</style>
