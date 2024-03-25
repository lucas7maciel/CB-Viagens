<script lang="ts">
import { RouterView } from 'vue-router'
import axios from 'axios'

export default {
  name: 'App',
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token
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
