<script lang="ts">
import Title from '@/components/Title.vue'

export default {
  components: {
    Title
  }
}
</script>

<template>
  <div class="about_us">
    <Title title="Quem Somos Nós?" />
    <div class="content">
      <h1>Somos uma rede de aeroportos</h1>
      <h2>Em breve informações serão adicionadas</h2>
    </div>
  </div>
</template>

<style scoped>
.about_us {
  display: flex;
  flex-direction: column;
  align-items: stretch;

  height: calc(100vh - 1rem);
  overflow: hidden;

  user-select: none;
}

.content {
  flex: 1;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  background-color: #f3f3f3;
  border-radius: 1rem;
  padding: 1rem 1rem;

  overflow: hidden;
}
</style>
