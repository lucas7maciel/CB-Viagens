<script lang="ts">
import SectionHeader from '@/components/SectionHeader.vue'

export default {
  components: {
    SectionHeader
  }
}
</script>

<template>
  <div class="about_us">
    <SectionHeader>Sobre Nós</SectionHeader>
    <div class="content">
      <h1>Somos uma rede de viagens</h1>
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
  text-align: center;

  background-color: #f3f3f3;
  border-radius: 1rem;
  padding: 1rem 1rem;

  overflow: hidden;
}

.content h1 {
  font-weight: bold;
}

.content h2 {
  font-weight: semibold;
}
</style>
