<script lang="ts">
import PlaneIcon from '@/components/icons/IconPlane.vue'

export default {
  props: ['trip', 'grid', 'header', 'openTrip'],
  components: { PlaneIcon },
  methods: {
    open() {
      if (this.openTrip) {
        this.openTrip(this.trip)
      }
    }
  }
}
</script>

<template>
  <!-- If container has 'header' class, it doesn't display any info -->
  <!-- Only its definition -->
  <div 
    class="properties" 
    @click="open()"
    :class="`
      ${grid ? 'grid' : 'list'}
      ${header ? 'header' : ''}`"
  >
    <!-- Decorative icon (List Mode) -->
    <PlaneIcon class="plane" />

    <!-- Data display -->
    <span class="city">
      {{ header ? 'Cidade' : trip.city }}
    </span>
  
    <span class="company">
      {{ header ? 'Compania' : trip.name }}
    </span>
    
    <span class="duration">
      {{ header ? 'Duração' : `${trip.duration}h` }}
    </span>

    <span class="price">
      {{ header ? 'Preço' : `R$ ${trip.price_confort}` }}
    </span>
  </div>

  <!-- Decorative, used to separate from actual rows -->
  <hr v-if="header" />
</template>

<style scoped>
/** List Mode */
.properties.list {
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;

  margin-block: 0.5rem;

  cursor: pointer;
  user-select: none;
}

.properties.list.header {
  /** Aligns header with rows list (padding caused by scrollbar) */
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
  transition: filter 0.3s;
}

.properties.list.header span {
  font-weight: bold;
  color: #d9d9d9;
}

.properties.list span {
  flex: 1;

  font-weight: 600;
  color: #2c3e50;
}

.properties.list .plane:hover {
  filter: invert(0.3);
}

.properties.list span:hover {
  color: rgb(161, 161, 161);
  transition: color 0.3s;
}

/** Grid Mode */
.properties.grid {
  display: flex;
  flex-wrap: wrap;

  justify-content: center;
  align-items: center;
  text-align: center;
  gap: 0.2rem;

  width: 100%;
  max-height: 8rem;

  padding-bottom: 0.8rem;

  white-space: nowrap;
  text-overflow: ellipsis;
  user-select: none;
  cursor: pointer;

  background-color: white;
  box-shadow: 0 4px 2px rgba(0, 0, 0, 0.05);
  border-radius: 1rem;

  transition: transform 0.2s;
}

.properties.grid:hover {
  transform: translateY(-0.4rem);
}

.properties.grid .city {
  flex: 1 1 100%;
  align-self: start;
  
  font-size: 1.25rem;
  font-weight: bold;
  color: white;

  padding: 0.5rem 0.4rem;

  border-top-left-radius: 1rem;
  border-top-right-radius: 1rem;
  background-color: var(--primary-color);
}

.properties.grid .company, 
.properties.grid .duration, 
.properties.grid .price {
  color: black;
}

.properties.grid .company {
  flex: 1 1 100%;
  
  font-weight: 600;

  margin-top: 0.4rem;
}

.properties.grid .duration::after {
  content: "  -  ";
}

.properties.grid .plane {
  display: none;
}

</style>