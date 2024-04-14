import { Store } from '@/config/store';

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $store: Store;
  }
}

declare module "vuex" {
  export * from "vuex/types/index.d.ts";
  export * from "vuex/types/helpers.d.ts";
  export * from "vuex/types/logger.d.ts";
  export * from "vuex/types/vue.d.ts";
}