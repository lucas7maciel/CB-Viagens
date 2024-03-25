<script lang="ts">
export default {
  props: ['Icon', 'title']
}
</script>

<template>
  <div class="link">
    <component :is="Icon" class="icon" />
    <p>{{ title }}</p>
  </div>
</template>

<style scoped>
.link {
  display: flex;
  align-items: center;

  padding: 0.6rem 0.8rem;
  margin-inline: 0.4rem;
  cursor: pointer;
  border-radius: 3rem;

  transition:
    filter 0.5s,
    background-color 0.5s;
}

.link:hover {
  filter: invert(1);
  background-color: black;
}

.link .icon {
  max-height: 1.5em;
  max-width: 1.5em;
}

.link p {
  padding-left: 0.6rem;
  font-weight: 600;
  font-size: 0.9rem;
}
</style>
