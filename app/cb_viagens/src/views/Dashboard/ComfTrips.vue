<script lang="ts">
// Components
import Modal from '@/components/Modal.vue'
import TripInfos from '@/components/TripInfos.vue'
import Row from '@/components/Row.vue'
import SectionHeader from '@/components/SectionHeader.vue'
import DateInput from '@/components/DateInput.vue'
import LayoutInput from '@/components/LayoutInput.vue'
// Types
import type { TripProps, TripModalProps } from '@/types/trip'

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
      trips: [] as TripProps[],
      cityInput: '' as string,
      layout: 'list' as 'grid' | 'list',
      tripModal: {
        active: false as boolean,
        current: null as TripProps | null
      } as TripModalProps
    }
  },
  methods: {
    getTrips() {
      fetch(
        `${import.meta.env.VITE_API_URL}/trips/${this.cityInput ? `?city=${this.cityInput}` : ''}`
      )
        .then((res) => res.json())
        .then((data) => {
          this.trips = data
        })
    },
    setLayout() {
      if (this.layout == 'grid') this.layout = 'list'
      else this.layout = 'grid'
    },
    openTrip(trip: TripProps) {
      this.tripModal.active = true
      this.tripModal.current = trip
    },
    closeTrip() {
      this.tripModal.active = false
    }, handleResize() {
      this.layout = window.innerWidth <= 950 ? 'grid' : 'list'
    }
  },
  mounted() {
    this.getTrips()
    this.handleResize()

    window.addEventListener("resize", this.handleResize.bind(this))
  }, beforeUnmount() {
    window.removeEventListener("resize", this.handleResize.bind(this))
  }
}
</script>

<template>
  <div class="calculate_trip">
    <SectionHeader title="Viagens Comfort"></SectionHeader>
    <div class="content">
      <div class="inputs">
        <div class="city">
          <input placeholder="Cidade" v-model="cityInput" @input="getTrips()" />
        </div>
        <DateInput />
        <LayoutInput :layout="layout" :setLayout="setLayout" />
      </div>
      <hr />
      <Row v-if="layout == 'list'" :header="true" />
      <div class="results" :class="layout == 'grid' ? 'grid' : ''">
        <Row
          v-for="(trip, key) in trips"
          :header="false"
          :grid="layout == 'grid'"
          :trip="trip"
          :openTrip="openTrip"
          :key="key"
        />
      </div>
    </div>
  </div>

  <transition name="custom-animation"
    ><Modal :close="closeTrip" title="Adicionar Viagem" v-if="tripModal.active"
      ><template #content> <TripInfos :trip="tripModal.current" :add="true" /> </template></Modal
  ></transition>
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
  overflow-y: scroll;
  scrollbar-width: thin;
  scrollbar-gutter: stable;
}

.results.grid { /** in grid mode */
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); /* Adjust the width as needed */
  gap: 1.2rem;

  padding-top: 0.6rem;
}

/* Modal*/
.custom-animation-leave-active {
  animation: fade-out 0.2s;
}

@keyframes fade-out {
  0% {
    opacity: 1;
  }

  100% {
    opacity: 0;
  }
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
