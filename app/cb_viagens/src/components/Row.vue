<script lang="ts">
import PlaneIcon from '@/components/icons/IconPlane.vue'

export default {
  props: ['trip', 'grid', 'header', 'openTrip'],
  components: {
    PlaneIcon
  }
}

/**
 * .properties.list{
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;

  margin-block: 0.5rem;
}

.properties.header .plane {
  opacity: 0.2;
}

.properties.list.plane {
  max-height: 1rem;
  max-width: 1rem;

  filter: invert(1);

  cursor: pointer;
}

.properties.header span {
  font-weight: bold;
  color: #d9d9d9;
}

.properties.listspan {
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
  <div class="properties" :class="`${grid ? 'grid' : 'list'} ${header ? 'header' : ''}`" @click="openTrip(trip)">
    <PlaneIcon class="plane" />
    <span class="city">{{ header ? 'Cidade' : trip.city }}</span
    ><span class="company">{{ header ? 'Compania' : trip.name }}</span
    ><span class="duration">{{ header ? 'Duração' : `${trip.duration}h` }}</span>
    <span class="price">{{ header ? 'Preço' : trip.price_confort }}</span>
  </div>
  <hr v-if="header" />
</template>

<style scoped>
/** List */
.properties.list {
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;

  margin-block: 0.5rem;

  cursor: pointer;
}

.properties.list.header { /** Aligns header with rows list (padding caused by scrollbar) */
  overflow: auto;
  scrollbar-width: thin;
  scrollbar-gutter: stable;
}

.properties.list.header .plane {
  opacity: 0.2;
}

.properties.list .plane {
  max-height: 1rem;
  max-width: 1rem;

  filter: invert(1);

  cursor: pointer;
}

.properties.list.header span {
  font-weight: bold;
  color: #d9d9d9;
}

.properties.list span {
  flex: 1;

  font-weight: 600;
}

/** Grid */
.properties.grid {
  display: flex;
  flex-wrap: wrap;

  justify-content: center;
  align-items: center;
  text-align: center;
  gap: 0.2rem;

  width: 100%;

  white-space: nowrap;
  text-overflow: ellipsis;
  cursor: pointer;

  background-color: white;
  border-radius: 1rem;
}

.properties.grid .city {
  flex: 1 1 100%;

  font-size: 1.4rem;
  font-weight: bold;
  color: white;

  padding: 0.2rem 0.4rem;

  border-top-left-radius: 1rem;
  border-top-right-radius: 1rem;
  background-color: black;
}

.properties.grid .company {
  flex: 1 1 100%;
  
  font-size: 1.1rem;
  font-weight: 600;
}

.properties.grid .duration::after {
  content: "  -  ";
}

.properties.grid .price::before {
  content: "R$ ";
}

.properties.grid .plane {
  display: none;
}

</style>