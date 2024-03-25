<script lang="ts">
//components
import Modal from '@/components/Modal.vue'
import AddTrip from '@/components/calculateTrip/AddTrip.vue'
import Row from '@/components/calculateTrip/Row.vue'
import Title from '@/components/Title.vue'
import DateInput from '@/components/calculateTrip/DateInput.vue'
import LayoutInput from '@/components/calculateTrip/LayoutInput.vue'
import Trip from '@/components/calculateTrip/Trip.vue'

interface TripProps {
  id: number
  name: string
  price_confort: string
  price_econ: string
  city: string
  duration: string
  seat: string
  bed: string
}

interface TripModalProps {
  active: boolean
  current: TripProps | null
}

export default {
  mounted() {
    this.getCities()
    this.getTrips()
  },
  data() {
    return {
      cities: [] as string[],
      trips: [] as TripProps[],
      cityInput: '' as string,
      layout: 'grid_mode' as 'grid_mode' | 'list_mode',
      tripModal: {
        active: false as boolean,
        current: null as TripProps | null
      } as TripModalProps
    }
  },
  components: {
    Trip,
    Modal,
    Row,
    AddTrip,
    Title,
    DateInput,
    LayoutInput
  },
  methods: {
    getCities() {
      fetch('http://localhost:3000/trips/cities')
        .then((res) => res.json())
        .then((data) => {
          this.cities = data
        })
    },
    getTrips(city: string) {
      fetch(`http://localhost:3000/trips/${city ? `?city=${city}` : ''}`)
        .then((res) => res.json())
        .then((data) => {
          this.trips = data
        })
    },
    setLayout() {
      if (this.layout == 'grid_mode') this.layout = 'list_mode'
      else this.layout = 'grid_mode'
    },
    openTrip(trip: TripProps) {
      this.tripModal.active = true
      this.tripModal.current = trip
    },
    closeTrip() {
      this.tripModal.active = false
    }
  },
  watch: {
    cityInput(newValue) {
      this.getTrips(newValue)
    }
  }
}
</script>

<template>
  <div class="calculate_trip">
    <Title title="Viagens Comfort"></Title>
    <div class="content">
      <div class="inputs">
        <div class="city"><input placeholder="Cidade" v-model="cityInput" /></div>
        <DateInput />
        <LayoutInput :layout="layout" :setLayout="setLayout" />
      </div>
      <hr />
      <Row :header="true" />
      <hr />
      <div class="results">
        <Row
          v-for="(trip, key) in trips"
          :header="false"
          :trip="trip"
          :openTrip="openTrip"
          :key="key"
        />
      </div>
    </div>
  </div>

  <transition name="custom-animation"
    ><Modal :close="closeTrip" title="Adicionar Viagem" v-if="tripModal.active"
      ><template #content> <AddTrip :trip="tripModal.current" /> </template></Modal
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

/*Tabela*/
.results {
  flex: 1;
  overflow-y: scroll;
}

/*Modal*/
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
</style>
