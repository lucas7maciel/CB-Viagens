<script lang="ts">
// Components
import DashboardBar from '../components/dashboardBar/DashboardBar.vue'
import Welcome from '@/views/Dashboard/WelcomeView.vue'
// Views
import CalculateTrip from '@/views/Dashboard/CalculateTripView.vue'
import MyTrips from '@/views/Dashboard/MyTripsView.vue'
import AboutUs from '@/views/Dashboard/AboutUsView.vue'
import ComfTrips from '@/views/Dashboard/ComfTrips.vue'
// Types
import type { PagesProps } from '@/types/pages'
// Functions
import { apiURL, getHeaders } from '@/utils/authData'
import { markRaw } from 'vue'

export default {
  components: {
    DashboardBar,
    Welcome
  },
  data() {
    return {
      current: null as string | null,
      pages: {
        'Calculate': markRaw(CalculateTrip),
        'My Trips': markRaw(MyTrips),
        'About Us': markRaw(AboutUs),
        'Comfort': markRaw(ComfTrips)
      } as PagesProps
    }
  },
  methods: {
    // Switches page
    setCurrent(current: string) {
      this.current = current
    }
  },
  beforeCreate() {
    document.title = 'Dashboard'
  },
  beforeMount() {
    // Checks if user is logged
    fetch(`${import.meta.env.VITE_API_URL || apiURL}/auth/users/me/`, getHeaders())
      .then(res => {
        if (res.status === 401) {
          this.$router.push('/signin')
        }
      })
      .catch(error => {
        console.log(error)

        this.$router.push('/signin')
      })
  },
}
</script>

<template>
  <div class="container">
    <DashboardBar :setPage="setCurrent" :page="current" />
    <div class="page">
      <component v-if="current" :is="pages[current]" />
      <Welcome v-else :setPage="setCurrent" />
    </div>
  </div>
</template>

<style scoped>
/** Whole page */
.container {
  height: 100vh;
  height: 100dvh;
  width: 100vw;
  width: 100dvw;

  padding: 0.5rem 0.5rem;

  display: flex;
  gap: 1rem;
}

/** Current Section */
.page {
  flex: 1;
}

/** Queries */
@media (max-width: 900px) {
  .container { /** Changes dashboard bar display */
    flex-direction: column;
  }
}
</style>
