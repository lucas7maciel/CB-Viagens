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
import { onMounted, onUnmounted, ref } from 'vue'

defineProps<{
  page: string | null
  setPage: (page: string) => void
}>()

// Defines dashboard display (sidebar or navbar)
const isPortrait = ref<boolean>(window.innerWidth <= 900)
// Defines pages modal
const options = ref<HTMLDivElement | null>(null) // Modal container
const menuOptions = ref<boolean>(false)          // If modal is open

function handleResize() {
  isPortrait.value = window.innerWidth <= 900
}

// If the options modal is open and the user clicks elsewhere, the modal closes
function handleClickOutside() {
  if (!menuOptions.value) return
    
  const options = document.querySelector('.menu_options') as HTMLElement;
    
  if (options) {
    menuOptions.value = false;
  }
}

onMounted(() => {
  handleResize() // Sets initial dashboard display

  document.addEventListener('click', handleClickOutside)
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
  window.removeEventListener('resize', handleResize)
})
</script>

<template>
  <div class="dashboard_bar" v-if="!isPortrait">
    <header class="header">
      <img class="logo" src="../../assets/logo.png" />
      <hr />
    </header>
    <!-- Section that displays application pages -->
    <div class="links">
      <Link :Icon="CalculatorIcon" :title="'Calcular Viagem'" @click="setPage('Calculate')" />
      <Link :Icon="PremiumIcon" :title="'Viagens Comfort'" @click="setPage('Comfort')" />
      <Link :Icon="PlaneIcon" :title="'Minhas Viagens'" @click="setPage('My Trips')" />
      <Link :Icon="QuestionIcon" :title="'Sobre Nós'" @click="setPage('About Us')" />
    </div>
    <hr />
    <!-- Profile section. If you click, it opens its options -->
    <Profile />
  </div>
  <!-- Dashboard in portrait mode -->
  <div class="dashboard_bar" v-else>
    <MenuIcon @click.stop="menuOptions = !menuOptions" class="menu" />
    <div v-if="menuOptions" ref="options" class="menu_options">
      <p @click="setPage('Calculate')">Calcular Viagem</p>
      <p @click="setPage('Comfort')">Viagens Comfort</p>
      <p @click="setPage('My Trips')">Minhas Viagens</p>
      <p @click="setPage('About Us')">Sobre Nós</p>
    </div>
    <h1 class="title">{{ page || 'Welcome' }}</h1>
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
  top: 90%;
  left: 1.2rem;
  z-index: 5;

  background: #03a8b5;

  padding: 0.5rem 0.8rem;

  border-radius: 1rem;

  animation: show_options 0.3s;
}

.menu_options p {
  width: 100%;

  padding: 0.3rem 0.8rem;;
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
