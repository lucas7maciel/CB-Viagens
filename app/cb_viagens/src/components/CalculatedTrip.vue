<script lang="ts">
// Components
import Modal from '@/components/Modal.vue'
import TripInfos from '@/components/TripInfos.vue'
// Types
import type {ModalProps} from '@/types/modal'

export default {
  props: ['title', 'trip'],
  components: {
    Modal,
    TripInfos
  },
  methods: {
    // Modal
    open() {
      const modal = this.$refs.modal as ModalProps | null
      modal?.open()
    },
    close() {
      const modal = this.$refs.modal as ModalProps | null
      modal?.close()
    }
  }
}
</script>

<template>
  <!-- Trip infos -->
  <div v-if="trip" class="container">
    <div class="trip" @click="open">
      <h1 class="title">{{ title }}</h1>
      <p class="company">{{ trip?.name || 'Sem Nome' }}</p>

      <div class="subinfos">
        <!-- Props -->
        <p class="prop">Leito</p>
        <p class="prop">Preço</p>
        <p class="prop">Duração</p>
        
        <!-- Values -->
        <p class="value">{{ trip?.seat || '?' }}</p>
        <p class="value">R$ {{ trip?.price_econ || '???' }}</p>
        <p class="value">{{ trip?.duration || '? ' }}h</p>
      </div>
    </div>

    <!-- Trip infos modal / Booking page -->
    <Modal ref="modal" :title="title">
      <TripInfos :trip="trip" :add="true" />
    </Modal>
  </div>
</template>

<style scoped>
.container {
  flex: 1;

  display: flex;
  justify-content: center;
  align-items: center;
}

.trip {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 0.6rem;

  padding-bottom: 1rem;

  color: var(--primary-color);
  user-select: none;
  white-space: nowrap;
  text-align: center;
  text-overflow: ellipsis;
  cursor: pointer;

  box-shadow: 0 4px 2px rgba(0, 0, 0, 0.05);
  background-color: white;
  border-radius: 1rem;

  transition: transform 0.3s;
  animation: fadein 0.6s;
}

.trip:hover {
  transform: translateY(-1rem);
}

.trips .trip .title {
  font-weight: bold;

  width: 20rem;

  padding: 1rem 1rem 0.5rem 1rem;
  border-top-left-radius: 1rem;
  border-top-right-radius: 1rem;

  color: white;
  background-color: var(--primary-color);
}

.trips .trip .company {
  margin-top: 0.5rem;
  font-size: 1.4rem;
  font-weight: bold;
}

.trip .subinfos {
  display: flex;
  text-align: center;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
}

.trip .subinfos * {
  flex: 1 1 29%;
}

.trips .trip .prop {
  color: gray;
  font-weight: 500;
}

.trips .trip .value {
  font-weight: bold;
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

/** Modal */
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
</style>
