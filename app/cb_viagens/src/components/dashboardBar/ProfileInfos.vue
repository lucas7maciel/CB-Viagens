<script lang="ts">
// Icons
import IconProfile from '@/components/icons/IconProfile.vue'
// Functions
import { formatDate } from '@/utils/formatDate'

export default {
  props: ['user'],
  components: {
    IconProfile
  },
  data() {
    return {
      name: `${this.user?.first_name} ${this.user?.last_name}` as string,
      joined: formatDate(new Date(this.user?.date_joined) || Date.now(), true)
    }
  }
}
</script>

<template>
  <div class="container">
    <div class="profile">
      <IconProfile class="pic" />
    </div>
    <hr />
    <p class="name">{{ user?.first_name ? name : '(Sem Nome)' }}</p>
    <p class="since">{{ user ? `Desde ${joined}` : 'Carregando...' }}</p>
  </div>
</template>

<style scoped>
/** Container */
.container {
  text-align: center;

  padding: 1rem 0;
}

/** General */
hr {
  width: 50%;

  margin: 1.5rem auto 0.4rem auto;
}

/** Picture */
.profile {
  max-height: 8rem;
  max-width: 8rem;
  aspect-ratio: 1;

  margin: 0 auto 0.5rem auto;

  border-radius: 50%;
  border: solid 3px white;
  box-shadow: 0 0 3px rgba(0, 0, 0, 0.2);

  background-color: var(--secondary-color);

  overflow: hidden;
}

.profile .pic {
  max-width: 100%;
  max-height: 100%;

  object-fit: contain;
}

/** Name */
.name {
  color: black;
  font-weight: bold;
  font-size: 2.3rem;

  margin-bottom: 0.2rem;
}

/** Since */
.since {
  font-weight: 600;
  font-size: 1rem;

  color: rgb(59, 59, 59);
}
</style>
