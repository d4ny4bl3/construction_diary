import { createRouter, createWebHistory } from "vue-router";
import { useUserStore } from '@/stores/userStore';
import { watch } from "vue";

import Login from "@/views/Login.vue";
import Dashboard from "@/views/Dashboard.vue";
import ProjectAddView from "@/views/ProjectAddView.vue";
import ProjectEditView from "@/views/ProjectEditView.vue";

const routes = [
    {
        path: "/login",
        name: "Login",
        component: Login,
        meta: {
            title: "titles.login",
        }
    },
    {
        path: "/dashboard",
        name: "Dashboard",
        component: Dashboard,
        meta: {
            title: "titles.dashboard"
        }
    },
    {
        path: "/projects/add",
        name: "ProjectAddView",
        component: ProjectAddView,
    },
    {
        path: "/projects/:id/:slug/edit",
        name: "ProjectEditView",
        component: ProjectEditView,
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
      const redirectTo = to.query.path || '/dashboard'
      return next(redirectTo)
    }

    if (to.path !== '/login' && !userStore.isLoggedIn) {
      return next({ path: '/login', query: { path: to.fullPath } })
    }

    next()
})

export default router