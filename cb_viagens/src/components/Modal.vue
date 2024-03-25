<script lang="ts">
//Icons
import CloseIcon from '@/components/icons/IconClose.vue'
//

export default {
  components: {
    CloseIcon
  },
  props: ['title', 'close', 'content', 'no_header']
}
</script>

<template>
  <div>
    <div class="shadow" @click="close"></div>
    <div class="modal">
      <div class="header" v-if="!no_header">
        <h3 class="title">{{ title }}</h3>
        <CloseIcon class="close" @click="close" />
      </div>
      <hr v-if="!no_header" />
      <slot name="content"></slot>
    </div>
  </div>
</template>

<style scoped>
/*Content (vou mudar)*/
.content {
  flex: 1;
}

.content .infos {
  display: flex;
  flex-wrap: wrap;

  margin-top: 1.5rem;
}

.content .infos .row {
  flex: 1;
  align-items: center;
  justify-content: center;
}

.content .infos .prop {
  font-weight: bold;
  color: gray;
}

.content .infos .value {
  font-weight: bold;
}

.content .infos .prop,
.content .infos .value {
  flex: 1 1 49%;

  font-size: 1.2rem;
}

.message {
  font-weight: bold;
  justify-self: center;
  text-align: center;

  padding-inline: 10%;

  margin-top: 1.5rem;
}

.add {
  font-weight: bold;
  font-size: 1.3rem;
  color: white;

  padding: 0.5rem 1rem;
  margin-top: 0.6rem;
  margin-bottom: 1rem;

  border-radius: 3rem;
  border: none;
  background-color: black;

  cursor: pointer;
  transition: background-color 0.3s;
}

.add:hover {
  background-color: lightgray;
}

/**/
.shadow,
.modal {
  position: fixed;
  z-index: 999;
}

/*Shadow*/
.shadow {
  width: 100%;
  height: 100%;

  top: 0;
  left: 0;

  background-color: rgba(0, 0, 0, 0.2);
  animation: show_shadow 0.4s;
}

@keyframes show_shadow {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
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

  font-weight: bold;
}

.modal .header .close {
  max-width: 1.3em;
  max-height: 1.3em;

  cursor: pointer;
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
</style>
