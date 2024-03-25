<script>
//must be a flexbox pipipipopopo
export default {
  props: ['title']
}
</script>
<template>
  <div class="title">
    <h1>{{ title }}</h1>
  </div>
</template>

<style scoped>
.title {
  flex: 0;

  display: flex;
  justify-content: center;
  align-items: center;

  padding: 0.5rem;
  margin-bottom: 1rem;

  background-color: #2a3041;
  border-radius: 1rem;
  color: white;

  user-select: none;
}

.title h1 {
  font-weight: bold;
}

/** */
@media (max-width: 55rem) {
  .title {
    display: none;
  }
}
</style>
