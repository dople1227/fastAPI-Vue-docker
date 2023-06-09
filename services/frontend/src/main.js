import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'


const app = createApp(App)
axios.defaults.withCredentials = true
axios.defaults.baseURL = 'http://localhost:5000/'

app.use(router)
app.mount("#app")
// createApp(App).use(router).mount('#app')
