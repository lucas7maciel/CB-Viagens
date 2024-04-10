<script lang="ts">
import { useStore } from 'vuex';
import axios from 'axios'

export default {
  name: 'App',
  beforeCreate() {
    const store = useStore();

    const token = store.state.token
    console.log(`Token ${token}`)
    if (token) {
      axios.defaults.headers.common['Authorization'] = `Token ${token}`
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  }
}
</script>

<template>
  <RouterView />
</template>

<style scoped></style>
