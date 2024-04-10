<script lang="ts">
import DashboardBar from '../components/dashboardBar/DashboardBar.vue'
//Pages
import Welcome from '@/views/Dashboard/WelcomeView.vue'
import CalculateTrip from '../views/Dashboard/CalculateTripView.vue'
import MyTrips from '@/views/Dashboard/MyTripsView.vue'
import AboutUs from '@/views/Dashboard/AboutUsView.vue'
import ComfTrips from '@/views/Dashboard/ComfTrips.vue'
//
import { markRaw } from 'vue'
import axios from 'axios'
// Types
import { type Component } from 'vue'

interface PagesProps {
  [key: string]: Component;
}

export default {
  data() {
    return {
      current: 'welcome' as string,
      pages: {
        calculate: markRaw(CalculateTrip),
        mytrips: markRaw(MyTrips),
        aboutus: markRaw(AboutUs),
        welcome: markRaw(Welcome),
        comftrips: markRaw(ComfTrips)
      } as PagesProps
    }
  },
  beforeCreate() {
    document.title = 'Dashboard'
  },
  beforeMount() {
    //checks if user is logged
    const provisorio: number = 1;

    if (provisorio) return

    axios
      .get('http://127.0.0.1:3000/auth/users/me/')
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
  components: {
    DashboardBar,
    CalculateTrip,
    MyTrips
  },
  methods: {
    setCurrent(current: string) {
      this.current = current
    }
  }
}
</script>

<template>
  <div class="container">
    <DashboardBar :setPage="setCurrent" />
    <div class="page"><component :is="pages[current]" /></div>
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
