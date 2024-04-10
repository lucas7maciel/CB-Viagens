<script lang="ts">
//components
import Modal from '@/components/Modal.vue'
import AddTrip from '@/components/calculateTrip/AddTrip.vue'
import Row from '@/components/calculateTrip/Row.vue'
import Title from '@/components/Title.vue'
import DateInput from '@/components/calculateTrip/DateInput.vue'
import Trip from '@/components/calculateTrip/Trip.vue'
//icons
import AlertIcon from '@/components/icons/IconAlert.vue'

/**
 * Mudar:
 * Pasta para types
 * .trip para component
 * Responsividade de .trip
 * Dados tratados no back
 */


//types
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

export default {
  mounted() {
    this.getCities()
    //this.getTrips()
  },
  data() {
    return {
      cities: [] as string[],
      cheapestTrip: null as TripProps | null,
      quickestTrip: null as TripProps | null,
      cityInput: '' as string,
      dateInput: null as Date | null,
      modal: false as boolean,
      message: 'Digite os dados para encontrar a viagem ideal' as string
    }
  },
  components: {
    Trip,
    Modal,
    Row,
    AddTrip,
    Title,
    DateInput,
    AlertIcon
  },
  methods: {
    getCities() {
      fetch('http://localhost:3000/trips/cities')
        .then((res) => res.json())
        .then((data) => {
          this.cities = Array.from(new Set(data));
        })
    },
    close() {
      this.modal = false
    },
    setDate(value: Date) {
      this.dateInput = value
    },
    search() {
      if (!this.cityInput || !this.dateInput) {
        this.modal = true
        return
      }

      this.message = 'Sem viagens para a data solicitada'
      fetch(`http://localhost:3000/trips/?city=${this.cityInput}`)
        .then((res) => res.json())
        .then((data) => {
          
          if (data.length == 0) {
            this.cheapestTrip = null
            this.quickestTrip =  null
            return
          }

          const durations = data.map((trip: TripProps) => parseInt(trip.duration.replace('h', '')))
          this.quickestTrip = data.filter((trip: TripProps) => trip.duration == `${Math.min(...durations)}h`)[0]

          const prices = data.map((trip: TripProps) => parseFloat(trip.price_econ.replace('R$ ', '')).toFixed(2))
          this.cheapestTrip = data.filter((trip: TripProps) => trip.price_econ == `R$ ${Math.min(...prices).toFixed(2)}`)[0]
        })
    }
  }
}
</script>

<template>
  <div class="calculate_trip">
    <Title title="Calcular Viagem"></Title>
    <div class="content">
      <div class="inputs">
        <div class="city">
          <select v-model="cityInput">
            <option disabled selected value="">Escolha a cidade</option>
            <option v-for="(city, key) in cities" :key="key">{{ city }}</option>
          </select>
        </div>
        <DateInput :setDate="setDate" />
        <button class="search" @click="search">Buscar</button>
      </div>
      <hr />
      <div class="trips">
        <h1 v-if="!cheapestTrip && !quickestTrip" style="font-weight: 600">{{ message }}</h1>
        <div class="trip" v-if="cheapestTrip">
          <h1 class="title">Mais Barata</h1>
          <p class="company">{{cheapestTrip?.name || "Sem Nome"}}</p>
          <div class="subinfos">
            <p class="prop">Leito</p>
            <p class="prop">Tempo Estimado</p>
            <p class="value">{{ cheapestTrip?.seat || "?" }}</p>
            <p class="value">{{ cheapestTrip?.duration || "?" }}</p>
          </div>
          <p class="prop">Preço</p>
          <p class="value">{{ cheapestTrip?.price_econ || "???" }}</p>

        </div>
        <div class="trip" v-if="quickestTrip">
          <h1 class="title">Mais Rápida</h1>
          <p class="company">{{quickestTrip?.name || "Sem Nome"}}</p>
          <div class="subinfos">
            <p class="prop">Leito</p>
            <p class="prop">Tempo Estimado</p>
            <p class="value">{{ quickestTrip?.seat || "?" }}</p>
            <p class="value">{{ quickestTrip?.duration || "?" }}</p>
          </div>
          <p class="prop">Preço</p>
          <p class="value">{{ quickestTrip?.price_econ || "???" }}</p>

        </div>
      </div>
    </div>
  </div>

  <transition name="custom-animation">
    <Modal :close="close" title="Preencha os Formulários" :no_header="true" v-if="modal"><template #content>
        <div class="fill_forms">
          <AlertIcon class="icon" />

          <p class="message">Informe cidade e data para pesquisar</p>
          <button class="close" @click="close">Fechar</button>
        </div>
      </template></Modal>
  </transition>
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

  margin-bottom: 1rem;
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
.inputs .date {
  display: flex;
  align-items: stretch;
}

.inputs .city,
.inputs .search {
  flex: 1 1 25%;
  justify-content: start;
}

.inputs .date {
  flex: 1 1 50%;
}

/*Inputs -> City*/
.inputs .city select {
  flex: 1;

  padding: 0 2.2rem;

  border-radius: 2.2rem;
  border: none;
  appearance: none;

  background-image: url('../../assets/expand.svg');
  background-repeat: no-repeat;
  background-position: 0.8rem center;
  background-size: 1.1rem 1.1rem;
}

/** Search */
.search {
  background-color: #2a3041;
  padding-inline: 4rem;
  color: white;
  font-weight: bold;
  border-radius: 0.8rem;
  cursor: pointer;
  transition: background-color 0.4s;
}

.search:hover {
  background-color: #48516c;
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

.fill_forms .icon {
  max-width: 4rem;
  max-height: 4rem;
}

.fill_forms .message {
  text-align: center;
  width: 80%;
  font-size: 1.6rem;
  margin: 0 auto;
}

.fill_forms .close {
  font-size: 1.3rem;
  color: white;

  padding: 0.5rem 3rem;
  margin-top: 1rem;

  background-color: #03a8b4;

  border: solid 0.3px #048a93;
  border-radius: 3rem;

  transition: background-color 0.5s;
}

.fill_forms .close:hover {
  background-color: #05becb;
}

@keyframes fade-out {
  0% {
    opacity: 1;
  }

  100% {
    opacity: 0;
  }
}

/** Trips */
.trips {
  flex: 1;

  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 3rem;

  overflow-y: scroll;
  overflow-x: hidden;
}

.trips .subinfos {
  display: flex;
  text-align: center;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
}

.trips .subinfos * {
  flex: 1 1 40%;
}

.trips .trip {
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  flex-direction: column;
  gap: 0.6rem;

  padding-bottom: 1rem;

  color:#2a3041;
  background-color: white;
  border-radius: 1rem;

  animation: fadein 0.6s;
}

@keyframes fadein {
  0% {
    transform: translateY(3rem);
    opacity: 0;
  }

  80% {
    opacity: 1;
  }

  100% {
    transform: translateY(0rem);
  }
}

.trips .trip > * {
  min-width: 20rem;
}

.trips .trip .title {
  font-weight: bold;

  padding: 1rem 1rem 0.5rem 1rem;
  border-top-left-radius: 1rem;
  border-top-right-radius: 1rem;

  color: white;
  background-color: #2a3041;
}

.trips .trip .company {
  margin-top: 0.5rem;
  font-size: 1.4rem;
  font-weight: bold;
}

.trips .trip .prop {
  color: gray;
  font-weight: 500;
}

.trips .trip .value {
  font-weight: bold;
}

</style>
