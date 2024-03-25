<script setup lang="ts">
import AlertIcon from '../icons/IconSpend.vue'

//colocar em script
interface TripProps {
  id: number
  name: string
  price_confort: string
  price_econ: string
  city: string
  duration: string
  seat: string
  bed: string
}
</script>

<template>
  <div class="trip">
    <div class="infos">
      <div class="icon"><AlertIcon /></div>
      <div class="text">
        <p class="company">Teste</p>
        <p>Tem 50 bancos</p>
        <p>Tempo estimado: 6h</p>
      </div>
    </div>
    <div class="price">
      <p class="title">Preço</p>
      <p class="value">R$1300</p>
    </div>
  </div>
</template>

<style scoped>
.trip {
  padding: 1rem 0.5rem;

  display: flex;
  align-items: stretch;
}

.infos {
  flex: 1;

  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 1rem;

  overflow: hidden;
  background-color: #f3f3f3;
  box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.2);
}

.icon {
  width: 6rem;
  height: 6rem;

  padding: 2.5rem 1.5rem;

  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #03a8b4;
}

.icon * {
  object-fit: cover;
  filter: invert(1);
}

.text {
  flex: 1;
  padding-inline: 1.5rem;
}

.company {
  font-weight: bold;
}

.price {
  border-radius: 1rem;

  display: flex;
  flex-direction: column;
  justify-content: center;

  padding: 1rem 2.5rem;
  margin-left: 1.5rem;

  background-color: #f3f3f3;
  box-shadow: 0px 1px 10px rgba(0, 0, 0, 0.2);
}

.price .title {
  font-weight: bold;
}
</style>
