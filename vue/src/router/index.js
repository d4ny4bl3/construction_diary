import { createRouter, createWebHistory } from "vue-router";
import { useUserStore } from '@/stores/userStore';
import { watch } from "vue";

import Login from "@/views/Login.vue";
import Dashboard from "@/views/Dashboard.vue";
import ProjectAddView from "@/views/project/ProjectAddView.vue";
import ProjectEditView from "@/views/project/ProjectEditView.vue";
import ProjectListView from "@/views/project/ProjectListView.vue";
import ProjectDetailView from "@/views/project/ProjectDetailView.vue";
import MaterialAddView from "@/views/material/MaterialAddView.vue";
import MaterialEditView from "@/views/material/MaterialEditView.vue";
import MaterialListView from "@/views/material/MaterialListView.vue";
import PurchaseAddView from "@/views/material/PurchaseAddView.vue";
import PurchaseEditView from "@/views/material/PurchaseEditView.vue";
import PurchaseDetailView from "@/views/material/PurchaseDetailView.vue";

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
        meta: {
            title: "titles.projectAdd"
        }
    },
    {
        path: "/projects/:id/:slug/edit",
        name: "ProjectEditView",
        component: ProjectEditView,
    },
    {
        path:"/projects",
        name: "ProjectListView",
        component: ProjectListView,
        meta: {
            title: "titles.projects"
        }
    },
    {
        path:"/projects/:id/:slug",
        name: "ProjectDetailView",
        component: ProjectDetailView,
        meta: {
            title: "titles.projectDetail"
        }
    },

    {
        path: "/materials/add",
        name: "MaterialAddView",
        component: MaterialAddView,
    },
    {
        path: "/materials/:id/edit",
        name: "MaterialEditView",
        component: MaterialEditView
    },
    {
        path: "/materials",
        name: "MaterialListView",
        component: MaterialListView,
    },

    {
        path: "/purchases/add",
        name: "PurchaseAddView",
        component: PurchaseAddView,
    },
    {
        path: "/purchases/:id/edit",
        name: "PurchaseEditView",
        component: PurchaseEditView,
    },
    {
        path: "/purchases/:id",
        name: "PurchaseDetailView",
        component: PurchaseDetailView,
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