<script lang="ts">
// Functions
import { getId, getHeaders } from '@/utils/authData'

export default {
  props: ['trip', 'add', 'cancel'],
  data() {
    return {
      message: 'Informações do voo selecionado' as string
    }
  },
  methods: {
    async bookTrip() {
      this.message = 'Reservando voo...'

      try {
        const id = await getId()

        if (!id) {
          this.message = 'Falha ao obter dados do usuário\n(Verifique está logado)'
          return
        }

        const res = await fetch(
          `${import.meta.env.VITE_API_URL}/trips/book/${this.trip.id}/${id}/`,
          getHeaders()
        )

        if (!res.ok) {
          this.message = 'Falha ao agendar viagem'
          return
        }

        if (res.status === 401) {
          this.message = 'Usuário não autorizado'
          return
        }

        const data = await res.json()

        this.message = 'success' in data ? data.success : data.message
      } catch (error) {
        this.message = 'Falha ao reservar viagem'

        console.error(error)
      }
    },
    async cancelTrip() {
      this.message = 'Cancelando voo...'

      try {
        const res = await fetch(
          `${import.meta.env.VITE_API_URL}/trips/cancel/${this.trip.id}/`,
          getHeaders()
        )

        if (res.status === 401) {
          this.message = 'Usuário não autorizado'
          return
        }

        if (!res.ok) {
          this.message = 'Falha ao cancelar viagem'
          return
        }

        const data = await res.json()

        this.message = 'success' in data ? data.success : data.message
      } catch (error) {
        this.message = 'Falha ao cancelar viagem'

        console.error(error)
      }
    },
    handleKeyboard(e: KeyboardEvent) {
      if (e.key !== 'Enter' && e.key !== ' ') {
        return
      }

      if (this.add) {
        this.bookTrip()
      } else if (this.cancel) {
        this.cancelTrip()
      }
    }
  },
  mounted() {
    document.addEventListener('keydown', this.handleKeyboard)
  },
  beforeUnmount() {
    document.addEventListener('keydown', this.handleKeyboard)
  }
}
</script>

<template>
  <div class="add_trip">
    <!-- Trip data -->
    <div class="infos">
      <span class="prop">Compania</span><span class="value">{{ trip.name }}</span>
      <span class="prop">Cidade</span><span class="value">{{ trip.city }}</span>
      <span class="prop">Duração</span><span class="value">{{ trip.duration }}</span>
      <span class="prop">Leito</span><span class="value">{{ trip.seat }}</span>
      <span class="prop">Preço</span><span class="value">{{ trip.price_confort }}</span>
    </div>

    <!-- Book | Cancel section -->
    <p v-if="cancel || add" class="message">{{ message }}</p>

    <div v-if="cancel || add" class="buttons">
      <button v-if="cancel" class="cancel" @click="cancelTrip">Cancelar</button>
      <button v-if="add" class="add" @click="bookTrip">Adicionar</button>
    </div>
  </div>
</template>

<style scoped>
.add_trip {
  flex: 1;
}

.add_trip .infos {
  display: flex;
  flex-wrap: wrap;

  margin-top: 1.5rem;
  margin-bottom: 1rem;
}

.add_trip .infos .row {
  flex: 1;
  align-items: center;
  justify-content: center;
}

.add_trip .infos .prop {
  font-weight: bold;
  color: gray;
}

.add_trip .infos .value {
  font-weight: bold;
}

.add_trip .infos .prop,
.add_trip .infos .value {
  flex: 1 1 49%;

  font-size: 1.2rem;
}

.message {
  font-weight: bold;
  justify-self: center;
  text-align: center;

  padding-inline: 10%;
  user-select: none;
}

/** Buttons */
.buttons {
  display: flex;
  justify-content: center;
  align-items: center;

  gap: 1rem;

  user-select: none;
}

button {
  font-weight: bold;
  font-size: 1.3rem;
  color: white;

  padding: 0.5rem 2rem;
  margin-top: 0.8rem;
  margin-bottom: 1rem;

  border-radius: 3rem;
  border: none;
  background-color: black;

  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: lightgray;
}

/** */
@media (orientation: portrait) {
  .add_trip .infos {
    flex-direction: column;
  }

  .add_trip .infos .value {
    font-size: 1.4rem;
    margin-bottom: 0.3rem;
  }
}
</style>
