<script lang="ts">
import DashboardBar from '../components/dashboardBar/DashboardBar.vue'
//Pages
import Welcome from '@/views/Dashboard/WelcomeView.vue'
import CalculateTrip from '@/views/Dashboard/CalculateTripView.vue'
import MyTrips from '@/views/Dashboard/MyTripsView.vue'
import AboutUs from '@/views/Dashboard/AboutUsView.vue'
import ComfTrips from '@/views/Dashboard/ComfTrips.vue'
//
import { markRaw } from 'vue'
import axios from 'axios'
// Types
import type { PagesProps } from '@/types/pages'

export default {
  components: {
    DashboardBar,
    Welcome
  },
  data() {
    return {
      current: null as string | null,
      pages: {
        calculate: markRaw(CalculateTrip),
        mytrips: markRaw(MyTrips),
        aboutus: markRaw(AboutUs),
        comftrips: markRaw(ComfTrips)
      } as PagesProps
    }
  },
  methods: {
    setCurrent(current: string) {
      this.current = current
    }
  },
  beforeCreate() {
    document.title = 'Dashboard'
  },
  beforeMount() {
    //checks if user is logged
    const provisorio: number = 1

    if (provisorio) return

    axios
      .get(`${import.meta.env.VITE_API_URL}/auth/users/me/`)
      .then((data: any /*Ajeitar isso*/) => {
        if (data.response?.status == 401 || !localStorage.getItem('token')) {
          this.$router.push('/signin')
          return
        }
      })
      .catch(() => {
        this.$router.push('/signin')
      })
  },
}
</script>

<template>
  <div class="container">
    <DashboardBar :setPage="setCurrent" />
    <div class="page">
      <component v-if="current" :is="pages[current]" />
      <Welcome v-if="!current" :setPage="setCurrent" />
    </div>
  </div>
</template>

<style scoped>
.container {
  height: 100vh;
  height: 100dvh;
  width: 100vw;
  width: 100dvw;

  padding: 0.5rem 0.5rem;

  display: flex;
  gap: 1rem;
}
.page {
  flex: 1;
}

/** */
@media (max-width: 55rem) {
  .container {
    flex-direction: column;
  }
}
</style>
