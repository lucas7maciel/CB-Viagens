<script lang="ts">
export default {
  props: ['trip', 'add', 'cancel'],
  methods: {
    //verificar se ta com permissao antes
    bookTrip() {
      fetch(`${import.meta.env.VITE_API_URL}/trips/book/${this.trip.id}/${14}/`) // Pegar parametros corretamente
        .then((res) => res.json())
        .then(console.log)
        .catch(console.log)
    },
    cancelTrip() {
      fetch(`${import.meta.env.VITE_API_URL}/trips/cancel/${this.trip.id}/`) // Pegar parametros corretamente
        .then((res) => res.json())
        .then(console.log)
        .catch(console.log)
    }
  }
}
</script>

<template>
  <div class="add_trip">
    <div class="infos">
      <span class="prop">Compania</span>|<span class="value">{{ trip.name }}</span>
      <span class="prop">Cidade</span>|<span class="value">{{ trip.city }}</span>
      <span class="prop">Duração</span>|<span class="value">{{ trip.duration }}</span>
      <span class="prop">Leito</span>|<span class="value">{{ trip.seat }}</span>
      <span class="prop">Preço</span>|<span class="value">{{ trip.price_confort }}</span>
    </div>

    <p v-if="cancel || add" class="message">O voo adicionado poderá ser visto em Minhas Viagens</p>
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
}

/** Buttons */
.buttons {
  display: flex;
  justify-content: center;
  align-items: center;

  gap: 1rem;
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
</style>
