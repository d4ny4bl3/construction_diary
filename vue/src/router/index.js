import { createRouter, createWebHistory } from "vue-router";
import { useUserStore } from '@/stores/user';
import { watch } from "vue";

import Login from "@/views/Login.vue";
import Dashboard from "@/views/Dashboard.vue";

const routes = [
    {
        path: "/login",
        name: "Login",
        component: Login,
    },
    {
        path: "/dashboard",
        name: "Dashboard",
        component: Dashboard,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach(async (to, from, next) => {
    const userStore = useUserStore()

    if (userStore.loading) {
        await new Promise(resolve => {
            const stop = watch(
                () => userStore.loading,
                (loading) => {
                    if (!loading) {
                        stop()
                        resolve()
                    }
                }
            )
        })
    }

    if (to.path === '/login' && userStore.isLoggedIn) {
        return next('/dashboard')
    }

    if (to.path !== '/login' && !userStore.isLoggedIn) {
      return next('/login')
    }

    next()
})

export default router