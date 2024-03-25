<script setup lang="ts">
import AlertIcon from './icons/IconAlert.vue'

defineProps<{
  message: string
  state?: 'normal' | 'alert' | 'error'
}>()
</script>

<template>
  <div class="shadow"></div>
  <div class="modal">
    <AlertIcon class="icon" />

    <p class="message">{{ message }}</p>
    <button class="close">Fechar</button>
  </div>
</template>

<style scoped>
.shadow {
  position: fixed;
  top: 0;
  left: 0;

  width: 100vw;
  width: 100dvw;

  height: 100vh;
  height: 100dvh;

  background-color: rgba(0, 0, 0, 0.3);
}

.modal {
  position: fixed;

  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  width: 50%;
  padding: 1.5rem 1rem;

  text-align: center;

  background-color: white;
  border-radius: 1rem;
  box-shadow: 0px 10px 10px rgba(0, 0, 0, 0.2);
}

.icon {
  max-width: 5rem;
  max-height: 5rem;
}

.message {
  text-align: center;
  width: 80%;
  font-size: 1.7rem;
  margin: 0 auto;
}

.close {
  font-size: 1.5rem;
  color: white;

  padding: 0.5rem 6rem;
  margin-top: 1rem;

  background-color: #03a8b4;

  border: solid 0.3px #048a93;
  border-radius: 0.5rem;
}
</style>
