import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.js'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './style.css'
import App from './App.vue'
import router from './router'
import i18n from '@/locales'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(i18n)

router.beforeEach((to, from, next) => {
    const defaultTitle = "Stavební deník"
    const translated = to.meta?.title ? i18n.global.t(to.meta.title) : null
    document.title = translated ? `${defaultTitle} - ${translated}` : defaultTitle
    next()
})

app.mount('#app')
