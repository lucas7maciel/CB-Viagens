
/* Not using vuex anymore
import type { InjectionKey } from 'vue'
import { createStore, Store } from 'vuex'

import type { StateProps } from '@/types/state'

export const key: InjectionKey<Store<StateProps>> = Symbol()

export const store: any = createStore<StateProps>({
  state: {
    token: '',
    authenticated: false
  },
  mutations: {
    initializeStore(state: StateProps) {
      const token = localStorage.getItem('token')
      if (token) {
        state.token = token
        state.authenticated = true
      } else {
        state.token = ''
        state.authenticated = false
      }
    },
    setToken(state: StateProps, token: string | null) {
      state.token = token
      state.authenticated = true
    },
    removeToken(state: StateProps) {
      state.token = ''
      state.authenticated = false
    }
  },
  actions: {},
  modules: {}
})
*/
