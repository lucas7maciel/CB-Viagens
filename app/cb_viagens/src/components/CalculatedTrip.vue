<script lang="ts">
export default {
  props: ['title', 'trip']
}
</script>

<template>
  <div v-if="trip" class="container">
    <div class="trip">
    <h1 class="title">{{ title }}</h1>
    <p class="company">{{ trip?.name || 'Sem Nome' }}</p>
    <div class="subinfos">
      <p class="prop">Leito</p>
      <p class="prop">Preço</p>
      <p class="prop">Duração</p>
      <p class="value">{{ trip?.seat || '?' }}</p>
      <p class="value">R$ {{ trip?.price_econ || '???' }}</p>
      <p class="value">{{ trip?.duration || '? ' }}h</p>
    </div>
  </div>
  </div>
</template>

<style scoped>
.container {
    flex: 1;

    display: flex;
    justify-content: center;
    align-items: center;
}

.trip {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 0.6rem;

  padding-bottom: 1rem;

  color: #2a3041;
  user-select: none;
  white-space: nowrap;
  text-align: center;
  text-overflow: ellipsis;
  cursor: pointer;

  box-shadow: 0 4px 2px rgba(0, 0, 0, 0.05);
  background-color: white;
  border-radius: 1rem;

  transition: transform 0.3s;
  animation: fadein 0.6s;
}

.trip:hover {
  transform: translateY(-1rem);
}

.trips .trip .title {
  font-weight: bold;

  width: 20rem;

  padding: 1rem 1rem 0.5rem 1rem;
  border-top-left-radius: 1rem;
  border-top-right-radius: 1rem;

  color: white;
  background-color: #2a3041;
}


.trips .trip .company {
  margin-top: 0.5rem;
  font-size: 1.4rem;
  font-weight: bold;
}

.trip .subinfos {
  display: flex;
  text-align: center;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
}

.trip .subinfos * {
  flex: 1 1 29%;
}

.trips .trip .prop {
  color: gray;
  font-weight: 500;
}

.trips .trip .value {
  font-weight: bold;
}

@keyframes fadein {
  0% {
    transform: translateY(3rem);
    opacity: 0;
  }

  80% {
    opacity: 1;
  }

  100% {
    transform: translateY(0rem);
  }
}

</style>
