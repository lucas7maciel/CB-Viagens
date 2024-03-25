<script lang="ts">
import PlaneIcon from '../icons/IconPlane.vue'

export default {
  components: {
    PlaneIcon
  },
  props: ['trip', 'header', 'openTrip']
}
</script>

<template>
  <div class="properties" :class="header ? 'header' : ''">
    <PlaneIcon class="plane" @click="openTrip(trip)" />
    <span>{{ header ? 'Cidade' : trip.city }}</span
    ><span>{{ header ? 'Compania' : trip.name }}</span
    ><span>{{ header ? 'Leito' : trip.seat }}</span
    ><span>{{ header ? 'Duração' : trip.duration }}</span>
  </div>
</template>

<style scoped>
.properties {
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;

  margin-block: 0.5rem;
}

.properties.header .plane {
  opacity: 0.2;
}

.properties .plane {
  max-height: 1rem;
  max-width: 1rem;

  filter: invert(1);

  cursor: pointer;
}

.properties.header span {
  font-weight: bold;
  color: #d9d9d9;
}

.properties span {
  flex: 1;

  font-weight: 600;
}
</style>
