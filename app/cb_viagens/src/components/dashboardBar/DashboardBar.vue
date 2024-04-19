<script setup lang="ts">
// Components
import Profile from './Profile.vue'
import Link from './Link.vue'
// Icons
import CalculatorIcon from '@/components/icons/IconCalculator.vue'
import PlaneIcon from '@/components/icons/IconPlane.vue'
import QuestionIcon from '@/components/icons/IconQuestion.vue'
import PremiumIcon from '@/components/icons/IconPremium.vue'
import MenuIcon from '@/components/icons/IconMenu.vue'
// Functions
import { onMounted, ref } from 'vue'

defineProps<{
  page: string | null,
  setPage: (page: string) => void
}>()

const isPortrait = ref(!(window.innerWidth > 900))
const menuOptions = ref(false)

onMounted(() => {
  window.addEventListener('resize', () => {
    if (window.innerWidth > 900) {
      isPortrait.value = false
    } else {
      isPortrait.value = true
    }
  })
})
</script>

<template>
  <div class="dashboard_bar" v-if="!isPortrait">
    <header class="header">
      <img class="logo" src="../../assets/logo.png" />
      <hr />
    </header>
    <div class="links">
      <Link :Icon="CalculatorIcon" :title="'Calcular Viagem'" @click="setPage('Calculate')" />
      <Link :Icon="PremiumIcon" :title="'Viagens Comfort'" @click="setPage('Comfort')" />
      <Link :Icon="PlaneIcon" :title="'Minhas Viagens'" @click="setPage('My Trips')" />
      <Link :Icon="QuestionIcon" :title="'Sobre Nós'" @click="setPage('About Us')" />
    </div>
    <hr />
    <Profile />
  </div>
  <div class="dashboard_bar" v-else>
    <MenuIcon @click="menuOptions = !menuOptions" class="menu" />
    <div v-if="menuOptions" class="menu_options">
      <p @click="setPage('Calculate')">Calcular Viagem</p>
      <p @click="setPage('Comfort')">Viagens Comfort</p>
      <p @click="setPage('My Trips')">Minhas Viagens</p>
      <p @click="setPage('About Us')">Sobre Nós</p>
    </div>
    <h1 class="title">{{ page || "Welcome" }}</h1>
    <Profile />
  </div>
</template>

<style scoped>
.dashboard_bar {
  position: relative;

  flex: 0 0 16rem;
  align-self: stretch;

  display: flex;
  flex-direction: column;

  /*padding-inline: 1rem;*/
  padding: 1rem 0 0 0;

  color: white;
  background-color: #2a3041;
  border-radius: 1rem;

  user-select: none;
}

.header {
  text-align: center;
}

.header .logo {
  width: calc(100% - 2rem);
  object-fit: contain;

  margin-bottom: 0.8rem;
}

hr {
  color: white;
  margin: 0.3rem 1.5rem;
}

.links {
  flex: 1;
}

/** Menu options *Otimizar com options do perfil */
.menu_options {
  position: absolute;
  top: 100%;
  left: 1.2rem;
  z-index: 5;

  background: gray;
  
  padding: 0.5rem 0.8rem;

  border-radius: 1rem;

  animation: show_options 0.3s;
}

.menu_options p {
  width: 100%;

  padding: 0.3rem 0.4rem;
  margin: 0.1rem 0.2rem;

  border-radius: 1rem;

  transition: background-color 0.5s;
}

.menu_options p:hover {
  background-color: rgba(255, 255, 255, 0.5);
}

/** */
@media (max-width: 900px) {
  .dashboard_bar {
    flex: 0;

    flex-direction: row;
    align-items: center;

    padding: 0.5rem 2rem;
  }

  .dashboard_bar .header {
    display: none;
  }

  .links {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  hr {
    display: none;
  }

  .menu {
    max-width: 2rem;
    max-height: 2rem;

    cursor: pointer;
  }

  .title {
    flex: 1;

    text-align: center;
  }
}
</style>
