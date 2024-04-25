<script lang="ts">
// Components
import Modal from '@/components/Modal.vue'
import ProfileInfos from '@/components/dashboardBar/ProfileInfos.vue'
// Icons
import ProfileIcon from '../icons/IconProfile.vue'
// Types
import type { ModalProps } from '@/types/modal'
import type {UserProps} from '@/types/user'
// Functions
import { getHeaders, logout } from '@/utils/authData'

export default {
  components: {
    ProfileIcon,
    Modal,
    ProfileInfos
  },
  data() {
    return {
      options: false as boolean,
      user: null as UserProps | null
    }
  },
  methods: {
    async getName() {
      try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/auth/users/me`, getHeaders());

        if (res.status === 401) {
          throw new Error('Unauthorized request');
        }

        if (!res.ok) {
            throw new Error('Falha no servidor');
        }

        const user = await res.json();

        if (!user) {
            throw new Error('Falha ao identificar usuário');
        }

        this.user = user.data
    } catch (error) {
        console.error('Error:', error);
    }
    },
    // Modal
    openModal() {
      const modal = this.$refs.modal as ModalProps | null
      modal?.open()
    },
    closeModal() {
      const modal = this.$refs.modal as ModalProps | null
      modal?.close()
    },
    // Options
    handleOptions() {
      this.options = !this.options
    },
    handleClickOutside(event: MouseEvent) {
      const profileRef = this.$refs.profileRef as HTMLDivElement

      if (this.options && !profileRef.contains(event.target as Node)) {
        this.options = false
      }
    },
    //
    logout() {
      logout(this.$router)
    }
  },
  mounted() {
    this.getName()

    document.addEventListener('click', this.handleClickOutside)
  },
  beforeUnmount() {
    document.removeEventListener('click', this.handleClickOutside)
  }
}
</script>

<template>
  <div class="profile" ref="profileRef" @click="handleOptions">
    <div class="pic">
      <ProfileIcon class="svg" />
    </div>
    <p class="name">
      {{ user ? user.first_name ? `${user.first_name} ${user.last_name}` : "(Sem Nome)" : "Carregando..." }}
    </p>

    <!-- Options Modal -->
    <div v-if="options" class="options" ref="options">
      <p @click="openModal">Ver Perfil</p>
      <p @click="logout">Logout</p>
    </div>

    <!-- User information modal -->
    <Modal ref="modal" title="Seu Perfil">
      <ProfileInfos :user="user" />
    </Modal>
  </div>
</template>

<style scoped>
/** Container */
.profile {
  position: relative;

  display: flex;
  align-items: center;
  gap: 1rem;

  max-height: 2rem;

  margin: 1rem 0;
  padding-inline: 1.2rem;

  white-space: nowrap;
  text-overflow: ellipsis;
  cursor: pointer;
}

/** Picture */
.pic {
  position: relative;

  width: 2rem;
  height: 2rem;

  background: var(--secondary-color);
  border-radius: 50%;
  border: solid white 2.5px;

  overflow: hidden;
}

.pic .svg {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  max-width: 100%;
  max-height: 100%;

  object-fit: contain;
}

/** Name */
.profile .name {
  flex: 1;

  font-weight: bold;
  text-overflow: ellipsis;
}

/* Options Modal */
.options {
  position: absolute;
  bottom: 130%;
  left: 1.2rem;
  z-index: 5;

  min-width: calc(100% - 2.4rem);

  padding: 0.5rem;

  background-color: var(--secondary-color);
  border-radius: 1rem;

  animation: show_options 0.3s;
}

.options p {
  width: 100%;

  padding: 0.3rem 0.8rem;
  margin: 0.1rem 0.2rem;

  border-radius: 1rem;

  transition: background-color 0.4s;
}

.options p:hover {
  background-color: rgba(255, 255, 255, 0.5);
}

/** Media queries */
@media (max-width: 900px) {
  /** Container */
  .profile {
    margin: 0;
    padding-inline: 0;
  }

  /** Name */
  .name {
    display: none;
  }

  /** Options Modal */
  .options {
    bottom: initial;
    left: initial;

    top: 130%;
    right: 0rem;
  }
}
</style>
