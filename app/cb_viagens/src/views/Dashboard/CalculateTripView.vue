<script lang="ts">
// Components
import Modal from '@/components/Modal.vue'
import SectionHeader from '@/components/SectionHeader.vue'
import DateInput from '@/components/DateInput.vue'
import CalculatedTrip from '@/components/CalculatedTrip.vue'
// Icons
import AlertIcon from '@/components/icons/IconAlert.vue'
// Functions
import { getHeaders } from '@/utils/authData'
// Types
import type { TripProps } from '@/types/trip'
import type { ModalProps } from '@/types/modal'

export default {
  components: {
    Modal,
    SectionHeader,
    DateInput,
    CalculatedTrip,
    AlertIcon
  },
  data() {
    return {
      cityInput: '' as string,
      dateInput: null as Date | null,
      cities: [] as string[],
      cheapestTrip: null as TripProps | null,
      quickestTrip: null as TripProps | null,
      message: 'Digite os dados para encontrar a viagem ideal' as string
    }
  },
  methods: {
    // Lists cities with available trips for select element
    async getCities() {
      try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/trips/cities`)

        if (!res.ok) {
          this.message = "Falha ao pesquisar cidades"
          return
        }

        this.cities = await res.json()
      
      } catch(error) {
        this.message = "Exceção ao pesquisar cidades"

        console.error(error)
      }
    },
    // Searchs quickest and cheapest trips available in selected date and city
    async getTrips() {
      if (!this.cityInput || !this.dateInput) {
        this.open()
        return
      }

      this.message = 'Pesquisando...'

      try {
        const url : string = `${import.meta.env.VITE_API_URL}/trips/calculate?city=${this.cityInput}`
        const res = await fetch(url, getHeaders())

        if (!res.ok) {
          this.cheapestTrip = null
          this.quickestTrip = null
          this.message = res.status === 401 ? "Usuário não autorizado" : "Falha ao pesquisar viagens"

          throw new Error(res.status === 401 ? "Unauthorized user" : "")
        }

        const data = await res.json()

        this.cheapestTrip = data.cheapest
        this.quickestTrip = data.quickest

        if (data.message === 'Pesquisando...') { // And (cheapest | quickest) trips are null
          this.message = `Nenhuma viagem encontrada para ${this.cityInput} no dia selecionado`
        }
      } catch(error) {
        this.cheapestTrip = null
        this.quickestTrip = null
        this.message = "Falha ao pesquisar viagens"

        console.error(error)
      }
    },
    // Modal
    open() {
      const modal = this.$refs.modal as ModalProps | null
      modal?.open()
    },
    close() {
      const modal = this.$refs.modal as ModalProps | null
      modal?.close()
    },
    // Date Input
    setDate(value: Date) {
      this.dateInput = value
    },
    // Event listeners
    handleKeyboard(e: KeyboardEvent) {
      const modal = this.$refs.modal as ModalProps | null

      if (e.key === 'Enter' || e.key === ' ') {
        document.activeElement?.blur()

        if (modal?.opened) {
          this.close()
        } else if (!this.cityInput) {
          const citySelect = this.$refs.city as HTMLSelectElement
          citySelect?.focus()
        } else if (!this.dateInput) {
          const dateRef = this.$refs.date as {openPicker: () => void}
          dateRef?.openPicker()
        } else {
          this.getTrips()
        }
      }
    }
  },
  watch: {
    cityInput() {
      // After user selects city, focus from select element is removed, so user
      // can activate date picker using keyboard
      const cityRef = this.$refs.city as HTMLSelectElement;
      cityRef?.blur()
    }
  },
  mounted() {
    this.getCities()

    document.addEventListener("keydown", this.handleKeyboard)
  },
  beforeUnmount() {
    document.removeEventListener("keydown", this.handleKeyboard)
  }
}
</script>

<template>
  <div class="calculate_trip">
    <SectionHeader title="Calcular Viagem"></SectionHeader>
    <div class="content">
      <!-- Inputs (city, date and search button) -->
      <div class="inputs">
        <div class="city">
          <select ref="city" v-model="cityInput">
            <option disabled selected value="">Escolha a cidade</option>
            <option v-for="(city, key) in cities" :key="key">{{ city }}</option>
          </select>
        </div>
        <DateInput ref="date" :setDate="setDate" />
        <button class="search" @click="getTrips">Buscar</button>
      </div>
      <hr />

      <!-- Trips container -->
      <div class="trips">
        <h1 v-if="!cheapestTrip && !quickestTrip" style="font-weight: 600">{{ message }}</h1>

        <CalculatedTrip title="Mais Barata" :trip="cheapestTrip" />
        <CalculatedTrip title="Mais Rápida" :trip="quickestTrip" />
      </div>
    </div>
  </div>

  <!-- 'Fill city and date' message -->
  <Modal ref="modal" :no_header="true">
    <div class="fill_forms">
      <AlertIcon class="icon" />

      <p class="message">Informe cidade e data para pesquisar</p>
      <button class="close" @click="close">Fechar</button>
    </div>
  </Modal>
</template>

<style scoped>
.calculate_trip {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  text-align: center;

  height: calc(100vh - 1rem);
}

.content {
  flex: 1;

  display: flex;
  flex-direction: column;
  align-items: stretch;

  background-color: #f3f3f3;
  border-radius: 1rem;
  padding: 1rem 1rem;

  scrollbar-width: thin;
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
  background-color: var(--primary-color);
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
  align-self: stretch;
  gap: 1rem;

  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;

  text-align: center;

  padding-inline: 5%;

  overflow-y: auto;
}

h1, button {
  user-select: none;
}

/** */
@media (max-width: 900px) {
  .inputs {
    flex-wrap: wrap;
    gap: 0.7rem;

    height: auto;
  }

  .inputs .city,
  .inputs .date {
    flex: 1 1 45%;
    justify-content: center;
  }

  .inputs .city,
  .inputs .search {
    height: 2rem; /** Ajeitar isso */
  }
}
</style>
