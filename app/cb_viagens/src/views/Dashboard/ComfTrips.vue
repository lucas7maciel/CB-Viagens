<script lang="ts">
// Components
import Modal from '@/components/Modal.vue'
import TripInfos from '@/components/TripInfos.vue'
import Row from '@/components/Row.vue'
import SectionHeader from '@/components/SectionHeader.vue'
import DateInput from '@/components/DateInput.vue'
import LayoutInput from '@/components/LayoutInput.vue'
// Types
import type { TripProps } from '@/types/trip'
// Functions
import { getHeaders } from '@/utils/authData'

export default {
  components: {
    Modal,
    Row,
    TripInfos,
    SectionHeader,
    DateInput,
    LayoutInput
  },
  data() {
    return {
      cityInput: '' as string,
      layout: 'list' as 'grid' | 'list',
      trips: [] as TripProps[],
      selectedTrip: null as TripProps | null,
      message: '' as string
    }
  },
  methods: {
    async getTrips() {
      this.message = "Pesquisando..."

      try {
        const url: string = `${import.meta.env.VITE_API_URL}/trips/${this.cityInput ? `?city=${this.cityInput}` : ''}`
        const res = await fetch(url, getHeaders())

        if (!res.ok) {
          this.message = res.status === 401 ? "Usuário não autorizado" : "Falha ao pesquisar viagens"
          this.trips = []

          throw new Error(res.status === 401 ? 'Unauthorized request' : '')
        }
        
        this.trips = await res.json()

        if (!this.trips.length) {
          this.message = this.cityInput ? `Sem viagens para ${this.cityInput}` : 'Sem viagens disponíveis'
        }
      
      } catch(error) {
        this.message = 'Falha ao pesquisar viagens'
        this.trips = []

        console.error(error)
      }
    },
    // Layout input
    toggleLayout() {
      this.layout = this.layout === 'grid' ? 'list' : 'grid'
    },
    // Modal
    openTrip(trip: TripProps) {
      this.selectedTrip = trip // Modal's content

      const modal = this.$refs.modal as any;
      modal?.open()
    },
    // Event Listeners
    handleResize() {
      // Toggles between grid and list mode based on screen size (list for wider screens)
      this.layout = window.innerWidth <= 950 ? 'grid' : 'list'
    }, 
    handleKeyboard(e: KeyboardEvent) {
      if (window.innerWidth <= 950) return

      if (e.key === 'ArrowRight') {
        this.layout = 'grid'
      } else if (e.key === 'ArrowLeft') {
        this.layout = 'list'
      } else if (e.key === ' ' || e.key === 'Enter') {
        this.toggleLayout()
      }
    }
  },
  mounted() {
    this.getTrips()
    this.handleResize()

    window.addEventListener("resize", this.handleResize.bind(this))
    document.addEventListener("keydown", this.handleKeyboard)
  }, 
  beforeUnmount() {
    window.removeEventListener("resize", this.handleResize.bind(this))
    document.removeEventListener("keydown", this.handleKeyboard)
  }
}
</script>

<template>
  <div class="calculate_trip">
    <SectionHeader title="Viagens Comfort"></SectionHeader>
    <div class="content">
      <!-- Header inputs (city, date, layout) -->
      <div class="inputs">
        <div class="city">
          <input placeholder="Cidade" v-model="cityInput" @input="getTrips()" />
        </div>
        <DateInput />
        <LayoutInput :layout="layout" :setLayout="toggleLayout" />
      </div>
      <hr />

      <!-- Comfort trips list -->
      <Row v-if="layout == 'list'" :header="true" />
      <div class="results" :class="layout == 'grid' ? 'grid' : ''">
        <Row
          v-for="(trip, key) in trips"
          :trip="trip"
          :openTrip="openTrip"
          :grid="layout == 'grid'"
          :key="key"
        />

        <!-- In case of exception or no trips available -->
        <div v-if="!trips.length" class="message">
          <h1>{{ message }}</h1>
        </div>
      </div>
    </div>
  </div>

  <!-- Displays trip infos -->
  <Modal ref="modal" title="Adicionar Viagem" :on_close="getTrips">
    <TripInfos :trip="selectedTrip" :add="true" />
  </Modal>
</template>

<style scoped>
.calculate_trip {
  display: flex;
  flex-direction: column;
  align-items: stretch;

  height: calc(100vh - 1rem);
  overflow: hidden;
}

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

/*Inputs (header)*/
.inputs {
  display: flex;
  align-items: stretch;
  gap: 0.2rem;

  height: 2rem;

  margin-bottom: 0.8rem;
}

.inputs .city,
.inputs .date,
.inputs .layout {
  display: flex;
  align-items: stretch;
}

.inputs .city,
.inputs .date {
  flex: 1 1 25%;
  justify-content: start;
}

.inputs .layout {
  flex: 1 1 50%;
  justify-content: end;
}

/*Inputs -> City*/
.inputs .city input {
  border-radius: 1.5rem;

  padding: 0 2.2rem;

  border: none;

  background-image: url('../../assets/search.svg');
  background-repeat: no-repeat;
  background-position: 0.5rem center;
  background-size: 1.2rem 1.2rem;
}

/* Tabela*/

.results {
  flex: 1;

  position: relative;

  overflow-y: scroll;
  scrollbar-width: thin;
  scrollbar-gutter: stable;
}

.results.grid { /** in grid mode */
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1.2rem;

  padding-top: 0.6rem;
}

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

/** */
@media (max-width: 950px) {
  /** Inputs */
  .inputs {
    flex-wrap: wrap;
    gap: 0.5rem;

    height: auto;

    margin-bottom: 0.7rem;
  }

  .inputs .city,
  .inputs .date {
    flex: 1 1 40%;

    justify-content: center;
  }

  /** City */
  .inputs .city input {
    flex: 1;
    padding-block: 0.5rem; /** Ver isso */
  }

  /** */
  .inputs .layout,
  .inputs .properties .header {
    display: none; /** Trocar isso */
  }
}
</style>
