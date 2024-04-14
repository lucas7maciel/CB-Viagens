<script lang="ts">
// Components
import Modal from '@/components/Modal.vue'
import ProfileInfos from '@/components/dashboardBar/ProfileInfos.vue'
// Icons
import ProfileIcon from '../icons/IconProfile.vue'
import type { Ref } from 'vue'

export default {
  components: {
    ProfileIcon,
    Modal,
    ProfileInfos
  },
  data() {
    return {
      options: false as boolean,
      modal: false as boolean
    }
  },
  methods: {
    getName() {
      const token : string | null = localStorage.getItem("token")

      const headers: Headers = new Headers()
      headers.append('Authorization', `Token ${token}`)

      const options: Object = {
        method: 'GET',
        headers
      } 

      fetch(`${import.meta.env.VITE_API_URL}/auth/users/me/`, options)
        .then(res => res.json())
        .then(console.log)
        .catch(console.log)
    },
    // Modal
    openModal() {
      this.modal = true
    },
    closeModal() {
      this.modal = false
    },
    // Options
    handleOptions() {
      this.options = !this.options
    },
    handleClickOutside(event: any /** Ver isso */) {
      const profileRef = this.$refs.profileRef as Ref<HTMLDivElement>;
      if (this.options && !profileRef.value.contains(event.target)) {
        console.log('Clicou fora, fechando')
        this.options = false
      }
    },
    logout() {
      localStorage.setItem('token', '')
      this.$router.push('signin')
    }
  },
  mounted() {
    //otimizar isso
    document.addEventListener('click', this.handleClickOutside)
    this.getName()
  },
  beforeUnmount() {
    document.removeEventListener('click', this.handleClickOutside)
  },
}
</script>

<template>
  <div class="profile" ref="profileRef" @click="handleOptions">
    <div class="pic"><ProfileIcon class="svg" /></div>
    <p class="name">Lucas Maciel</p>

    <div v-if="options" class="options" ref="options">
      <p @click="openModal">Ver Perfil</p>
      <p @click="logout">Logout</p>
    </div>
    
    <Modal :close="closeModal" title="Seu Perfil" v-if="modal"
      ><template #content><ProfileInfos /></template></Modal
  >
  </div>
</template>

<style scoped>
.profile {
  position: relative;

  display: flex;
  align-items: center;
  gap: 1rem;

  max-height: 2rem;

  margin: 1rem 0;
  padding-inline: 1.2rem;

  cursor: pointer;
}

.profile .pic {
  position: relative;

  width: 2rem;
  height: 2rem;

  border-radius: 50%;
  border: solid white 2.5px;

  overflow: hidden;
}

.profile .pic .svg {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  max-width: 100%;
  max-height: 100%;

  object-fit: contain;
}

.profile .name {
  flex: 1;
  font-weight: bold;
}

/* options */
.profile .options {
  position: absolute;
  bottom: 130%;
  left: 1.2rem;

  min-width: calc(100% - 2.4rem);

  padding: 0.5rem;

  background-color: gray;
  border-radius: 1rem;

  animation: show_options 0.3s;
}

.profile .options p {
  width: 100%;

  padding: 0.3rem 0.4rem;
  margin: 0.1rem 0.2rem;

  border-radius: 1rem;

  transition: background-color 0.5s;
}

.profile .options p:hover {
  background-color: rgba(255, 255, 255, 0.5);
}

@keyframes show_options {
  0% {
    opacity: 0;
    transform: translateY(1rem);
  }

  80% {
    opacity: 1;
  }

  100% {
    transform: translateY(0rem);
  }
}

/** */
@media (max-width: 55rem) {
  .profile {
    display: none;
  }
}
</style>
