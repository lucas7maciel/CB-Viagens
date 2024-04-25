<script lang="ts">
//Icons
import CloseIcon from '@/components/icons/IconClose.vue'

export default {
  props: ['title', 'content', 'no_header', 'on_close'],
  components: {
    CloseIcon
  },
  data() {
    return {
      opened: false as boolean
    }
  },
  methods: {
    open() {
      this.opened = true
    },
    close() {
      if (this.on_close) {
        this.on_close()
      }

      this.opened = false
    }
  }
}
</script>

<template>
  <transition name="custom-animation">
    <div v-if="opened">
      <!-- Decorative shadow -->
      <div class="shadow" @click="close"></div>

      <!-- Actual container -->
      <div class="modal">

        <!-- Modal header (optional) -->
        <div class="header" v-if="!no_header">
          <h3 class="title">{{ title }}</h3>
          <CloseIcon class="close" @click="close" />
        </div>

        <!-- Line that divides header (if active) from content -->
        <hr v-if="!no_header" />
        
        <!-- Modal's content -->
        <slot></slot>
      </div>
    </div>
  </transition>
</template>

<style scoped>
/* General */
.shadow,
.modal {
  position: fixed;
  z-index: 999;
}

/* Shadow */
.shadow {
  width: 100%;
  height: 100%;

  top: 0;
  left: 0;

  background-color: rgba(0, 0, 0, 0.2);
  animation: show_shadow 0.4s;
}

/** Closing transition */
.custom-animation-leave-active {
  animation: fade-out 0.2s;
}

/*Modal*/
.modal {
  left: 50%;
  top: 50%;

  transform: translate(-50%, -50%);

  min-width: 30%;
  max-width: 80%;

  text-align: center;

  padding: 0.7rem;

  background-color: white;
  border-radius: 1rem;

  animation: show_modal 0.3s;
}

.modal .header,
hr {
  margin-bottom: 0.3rem;
}

.modal .header {
  display: flex;
  align-items: center;
  text-align: start;
}

.modal .header .title {
  flex: 1;

  color: black;
  font-weight: bold;
  user-select: none;
}

.modal .header .close {
  max-width: 1.3em;
  max-height: 1.3em;

  cursor: pointer;
}

/** Animations */
@keyframes show_shadow {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes fade-out {
  0% {
    opacity: 1;
  }

  100% {
    opacity: 0;
  }
}

@keyframes show_modal {
  0% {
    opacity: 0;
    top: 60%;
  }

  90% {
    opacity: 1;
  }
}

/** Queries */
@media (orientation: portrait) {
  .modal {
    min-width: 75%;
  }
}
</style>
