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
  <div class="layout">
    <div class="container" @click="setLayout">
      <div
        class="selected"
        :class="{ grid_mode: layout === 'grid_mode', list_mode: layout === 'list_mode' }"
      ></div>
      <div class="grid" style="filter: invert(1)">
        <GridIcon class="icon" />
        <span>Grid</span>
      </div>
      <div class="list">
        <ListIcon class="icon" />
        <span>Lista</span>
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

  padding: 0 /*.5rem*/ 1rem;
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

.layout .selected:hover {
  background-color: gray;
}

.layout .selected.list_mode {
  left: 50%;
}

.layout .container .grid,
.layout .container .list {
  position: relative;

  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 0.5rem;

  padding-inline: 0.7rem;

  z-index: 2;
}

.grid .icon,
.list .icon {
  max-height: 1rem;
  max-width: 1rem;
}
</style>
