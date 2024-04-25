<script lang="ts">
// Components
import Modal from '@/components/Modal.vue'
import TripInfos from '@/components/TripInfos.vue'
import Row from '@/components/Row.vue'
import SectionHeader from '@/components/SectionHeader.vue'
// Functions
import { apiURL, getHeaders, getId } from '@/utils/authData'
// Types
import type { TripProps } from '@/types/trip'
import type { ModalProps } from '@/types/modal'

export default {
  components: {
    Modal,
    Row,
    TripInfos,
    SectionHeader
  },
  data() {
    return {
      cityInput: '' as string,
      layout: 'grid' as 'grid' | 'list',
      trips: [] as TripProps[],
      selectedTrip: null as TripProps | null,
      message: '' as string
    }
  },
  methods: {
    async getTrips() {
      this.message = 'Pesquisando...'

      try {
        const id = await getId()

        if (!id) {
          this.message = "Usuário não autorizado"
          return
        }        

        const url: string = `${import.meta.env.VITE_API_URL || apiURL}/trips/booked/${id}/`
        const res = await fetch(url, getHeaders())

        if (!res.ok) {
          this.message =
            res.status === 401 ? 'Usuário não autorizado' : 'Falha ao pesquisar viagens'
          this.trips = []

          throw new Error(res.status === 401 ? 'Unauthorized request' : '')
        }

        this.trips = await res.json()

        if (!this.trips.length) {
          this.message = this.cityInput
            ? `Sem viagens para ${this.cityInput}`
            : 'Sem viagens disponíveis'
        }
      } catch (error) {
        this.message = 'Falha ao pesquisar viagens'
        this.trips = []

        console.error(error)
      }
    },
    setLayout() {
      this.layout = this.layout == 'grid' ? 'list' : 'grid'
    },
    // Trip infos modal
    openTrip(trip: TripProps) {
      this.selectedTrip = trip

      const modal = this.$refs.modal as ModalProps | null
      modal?.open()
    },
    // Event listeners
    handleResize() {
      this.layout = window.innerWidth <= 950 ? 'grid' : 'list'
    }
  },
  mounted() {
    this.getTrips()
    this.handleResize()

    window.addEventListener('resize', this.handleResize.bind(this))
  },
  beforeUnmount() {
    window.removeEventListener('resize', this.handleResize.bind(this))
  }
}
</script>

<template>
  <div class="my_trips">
    <SectionHeader>Minhas Viagens</SectionHeader>

    <div class="content">
      <!-- Trips list -->
      <Row v-if="layout == 'list'" :header="true" />
      <div class="results" :class="layout == 'grid' ? 'grid' : ''">
        <Row
          v-for="(trip, key) in trips"
          :key="key"
          :trip="trip"
          :openTrip="openTrip"
          :grid="layout == 'grid'"
        />

        <!-- In case there aren't trips or exception -->
        <div v-if="!trips.length" class="message">
          <h1>{{ message }}</h1>
        </div>
      </div>
    </div>
  </div>

  <Modal ref="modal" title="Conferir Viagem" :on_close="getTrips">
    <TripInfos :trip="selectedTrip" :cancel="true"/>
  </Modal>
</template>

<style scoped>
/** Page container */
.my_trips {
  display: flex;
  flex-direction: column;
  align-items: stretch;

  height: calc(100vh - 1rem);
  overflow: hidden;
}

/** Content section (rows) */
.content {
  flex: 1;

  display: flex;
  flex-direction: column;
  align-items: stretch;

  background-color: #f3f3f3;
  border-radius: 1rem;
  padding: 1rem 1rem;

  overflow: hidden;
}

.content hr {
  color: #d9d9d9;
}

/* Rows container */
.results {                /** Default (List mode) */
  position: relative;

  flex: 1;

  overflow-y: auto;
  scrollbar-width: thin;
  scrollbar-gutter: stable;
}

.results.grid {           /** Grid mode */
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1.2rem;

  padding-top: 0.6rem;
}

/** Message (in case of exceptions or no rows) */
.results .message {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;

  /** Absolute positioned so the div wont be affected
  by results' display */
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  width: 100%;
  height: 100%;

  padding-inline: 4%;
}

.results .message h1 {
  font-weight: bold;
  color: rgb(67, 67, 67);
}

/** Queries */
@media (max-width: 950px) {
  .properties.header {
    display: none;
  }
}
</style>
