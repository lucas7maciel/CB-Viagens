<script lang="ts">
// Components
import VueDatePicker from '@vuepic/vue-datepicker'
// Styling
import '@vuepic/vue-datepicker/dist/main.css'
// Functions
import { formatDate } from '@/utils/formatDate'
// Icons
import ExpandIcon from '@/components/icons/IconExpand.vue'

export default {
  props: ['setDate'],
  components: {
    VueDatePicker,
    ExpandIcon
  },
  data() {
    return {
      dateOutput: 'Selecione uma Data' as string
    }
  },
  methods: {
    // This function its gonna format the date selected in date picker
    format(date: Date) {
      if (!date) {
        return ''
      }

      this.setDate(date)
      this.dateOutput = formatDate(date) // @/utils/formatDate

      return this.dateOutput
    },
    // Opens date picker modal
    openPicker() {
      const datePicker = this.$refs.datepicker as any
      datePicker?.openMenu()
    }
  }
}
</script>

<template>
  <div class="date">
    <div class="container" @click="openPicker">
      <!-- Original component -->
      <VueDatePicker
        class="datepicker"
        ref="datepicker"
        :format="format"
        :enable-time-picker="false"
        :min-date="new Date()"
      />

      <!-- This div is gonna cover original's component appearence, so i cant edit it in my way -->
      <!-- Only its original modal it's gonna be used -->
      <div class="hider"></div>

      <!-- My own stylying -->
      <span>{{ dateOutput }}</span>
      <ExpandIcon class="expand" />
    </div>
  </div>
</template>

<style scoped>
.date .container {
  position: relative;

  /*font-size: 1.2rem;*/
  font-size: 0.9rem;
  user-select: none;
  color: gray;

  padding: 0 /*.4rem*/ 1.5rem;

  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;

  border-radius: 1.5rem;

  cursor: pointer;
}

.date .container span {
  white-space: nowrap;
}

.date .container .expand {
  max-width: 1rem;
  max-height: 1rem;
}

/*Esconder o input do date picker*/
.date .container .datepicker {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);

  z-index: 1;
}

.date .container .hider {
  position: absolute;
  top: -0.3rem;
  left: -0.1rem;

  width: calc(100% + 0.2rem);
  height: calc(100% + 0.6rem);

  background-color: #f3f3f3;

  z-index: 2;
}

.date .container span,
.date .container .expand {
  position: relative;
  z-index: 3;
}

/** */
@media (max-width: 950px) {
  .date .container .hider {
    /** Based on new header measures (comfTrips, myTrips) */
    top: -0.5rem;
    height: calc(100% + 1.2rem);
  }
}
</style>
