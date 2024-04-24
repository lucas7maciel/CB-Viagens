<script lang="ts">
// Icons
import GridIcon from '@/components/icons/IconGrid.vue'
import ListIcon from '@/components/icons/IconList.vue'

export default {
  props: ['layout', 'setLayout'],
  components: {
    GridIcon,
    ListIcon
  }
}
</script>

<template>
  <!-- Grid mode state is stored in parent component -->
  <!-- But toggle function is passed as props -->
  <div class="layout" :class="`${layout}_mode`">
    <div class="container" @click="setLayout">
      <!-- Black section that stands behind selected mode -->
      <div class="selected"></div>

      <!-- List Mode -->
      <div class="list">
        <ListIcon class="icon" />
        <span>Lista</span>
      </div>

      <!-- Grid Mode -->
      <div class="grid">
        <GridIcon class="icon" />
        <span>Grid</span>
      </div>

    </div>
  </div>
</template>

<style scoped>
.layout .container {
  position: relative;

  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;

  padding: 0 1rem;
  background-color: white;

  border-radius: 2rem;
  cursor: pointer;

  user-select: none;

  z-index: 2;
}

.layout .selected {
  position: absolute;
  top: 0;
  left: 0;

  width: 50%;
  height: 100%;

  background-color: black;

  border-radius: 2rem;
  border: none;

  transition:
    left 0.2s ease-out,
    background-color 0.5s;

  z-index: 1;
  backdrop-filter: invert(100%);
}

.layout:hover .selected  {
  background-color: rgb(92, 92, 92);
}

.layout.grid_mode .selected {
  left: 50%;
}

.layout.list_mode .list, .layout.grid_mode .grid {
  filter: invert(1);
}

.layout .grid,
.layout .list {
  position: relative;
  z-index: 2;

  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 0.5rem;

  padding-inline: 0.7rem;

  transition: filter 0.6s 0.05s;
}

.grid span, .list span {
  font-weight: semibold;
}

.grid .icon,
.list .icon {
  max-height: 1rem;
  max-width: 1rem;
}
</style>
