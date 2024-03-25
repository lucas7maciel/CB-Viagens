import { ComponentCustomProperties } from 'vue'
import { Store } from 'vuex'

declare module '@vue/runtime-core' {
  // declare seus próprios estados do store
  interface State {
    token: string | null
    authenticated: boolean
  }

  // fornece tipagem para `this.$store`
  interface ComponentCustomProperties {
    $store: Store<State>
  }
}
