<script lang="ts">
import PlaneIcon from '@/components/icons/IconPlane.vue'

export default {
  props: ['trip', 'header', 'openTrip'],
  components: {
    PlaneIcon
  }
}

/**
 * .properties {
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

.header {
  overflow: auto;
  scrollbar-width: thin;
  scrollbar-gutter: stable;
}
 */
</script>

<template>
  <div class="properties" :class="header ? 'header' : ''">
    <PlaneIcon class="plane" @click="openTrip(trip)" />
    <span>{{ header ? 'Cidade' : trip.city }}</span
    ><span>{{ header ? 'Compania' : trip.name }}</span
    ><span>{{ header ? 'Duração' : `${trip.duration}h` }}</span>
    <span>{{ header ? 'Preço' : trip.price_confort }}</span>
  </div>
  <hr v-if="header" />
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

.header { /** Aligns header with rows list (padding caused by scrollbar) */
  overflow: auto;
  scrollbar-width: thin;
  scrollbar-gutter: stable;
}

</style>