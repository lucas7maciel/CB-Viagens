import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import  {store, key} from './store'
import axios from 'axios'

//axios.defaults.baseURL = 'localhost:3000/'

const app = createApp(App)
app.use(createPinia())
app.use(store, key)
app.use(router)

app.config.globalProperties.$axios = axios

app.mount('#app')
