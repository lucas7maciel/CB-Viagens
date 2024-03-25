<script setup lang="ts">
import Profile from './Profile.vue'
import Link from './Link.vue'
//Icons
import CalculatorIcon from '../icons/IconCalculator.vue'
import PlaneIcon from '../icons/IconPlane.vue'
import QuestionIcon from '../icons/IconQuestion.vue'
import PremiumIcon from '@/components/icons/IconPremium.vue'

defineProps<{
  setPage: void
}>()
</script>

<template>
  <div class="dashboard_bar">
    <header class="header">
      <img class="logo" src="../../assets/logo.png" />
      <hr />
    </header>
    <div class="links">
      <Link :Icon="CalculatorIcon" :title="'Calcular Viagem'" @click="setPage('calculate')" />
      <Link :Icon="PremiumIcon" :title="'Viagens Comfort'" @click="setPage('comftrips')" />
      <Link :Icon="PlaneIcon" :title="'Minhas Viagens'" @click="setPage('mytrips')" />
      <Link :Icon="QuestionIcon" :title="'Sobre Nós'" @click="setPage('aboutus')" />
    </div>
    <hr />
    <Profile />
  </div>
</template>

<style scoped>
.dashboard_bar {
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

/** */
@media (max-width: 55rem) {
  .dashboard_bar {
    flex: 0;

    flex-direction: row;
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
}
</style>
