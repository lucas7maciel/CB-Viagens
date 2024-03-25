<script lang="ts">
import Link from '@/components/dashboardBar/Link.vue'
import CalculatorIcon from '@/components/icons/IconCalculator.vue'
import PlaneIcon from '@/components/icons/IconPlane.vue'
import QuestionIcon from '@/components/icons/IconQuestion.vue'

export default {
  components: {
    Link,
    CalculatorIcon,
    PlaneIcon,
    QuestionIcon
  }
}
</script>

<template>
  <div class="welcome">
    <h1>Seja bem vindo ao dashboard</h1>
    <h2>Utilize os links da <span class="navbar">Navbar</span> para navegar entre nossas opções</h2>
    <div class="links">
      <Link :Icon="CalculatorIcon" :title="'Calcular Viagem'" />
      <Link :Icon="PlaneIcon" :title="'Minhas Viagens'" />
      <Link :Icon="QuestionIcon" :title="'Sobre Nós'" />
    </div>
  </div>
</template>

<style scoped>
.welcome {
  flex: 1;

  height: 100%;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;

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
}

.links .link {
  background-color: #2a3041;
  color: white;
}
</style>
