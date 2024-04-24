<script setup lang="ts">
// Components
import Link from '@/components/dashboardBar/Link.vue'
// Icons
import CalculatorIcon from '@/components/icons/IconCalculator.vue'
import PlaneIcon from '@/components/icons/IconPlane.vue'
import QuestionIcon from '@/components/icons/IconQuestion.vue'
import PremiumIcon from '@/components/icons/IconPremium.vue'

const props = defineProps({
  setPage: {
    type: Function as () => void,
    required: true
  }
})

const setPage = (page: string) => {
  props.setPage(page);
}

</script>

<template>
  <div class="welcome">
    <h1>Seja bem vindo ao dashboard</h1>
    <h2>Utilize os links da <span class="navbar">Navbar</span> para navegar entre nossas opções</h2>
    
    <div class="links">
      <Link :Icon="CalculatorIcon" :title="'Calcular Viagem'" @click="setPage('Calculate')" />
      <Link :Icon="PremiumIcon" :title="'Viagens Comfort'" @click="setPage('Comfort')" />
      <Link :Icon="PlaneIcon" :title="'Minhas Viagens'" @click="setPage('My Trips')" />
      <Link :Icon="QuestionIcon" :title="'Sobre Nós'" @click="setPage('About Us')" />
    </div>
  </div>
</template>

<style scoped>
.welcome {
  flex: 1;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;

  height: 100%;

  padding-inline: 1.5rem;

  background-color: #f3f3f3;
  border-radius: 1rem;
}

.welcome h1 {
  font-weight: bold;
}

.navbar {
  font-weight: 600;
  color: #05a8b4;
}

.links {
  margin-top: 1.5rem;

  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;

  width: 80%;
  row-gap: 1rem;
}

.links .link {
  background-color: black;
  color: white;
}

.links .link:hover {
  filter: invert(1);
}

</style>
