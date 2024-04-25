<script lang="ts">
//import axios from 'axios'
//import type { ComponentOptions } from 'vue';

export default {
  name: 'App',
  /*beforeCreate(this: ComponentOptions<any>) {
    const store = this.$store as any;
    const token = store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = `Token ${token}`
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  }*/
}
</script>
<template>
  <RouterView />
</template>

<style scoped></style>
