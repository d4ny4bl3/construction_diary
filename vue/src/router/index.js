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
import PurchaseListView from "@/views/material/PurchaseListView.vue";
import DailyLogAddView from "@/views/dailyLog/DailyLogAddView.vue";
import DailyLogDetailView from "@/views/dailyLog/DailyLogDetailView.vue";

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
        meta: {
            title: "titles.projectEdit"
        }
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
        meta: {
            title: "titles.materialAdd"
        }
    },
    {
        path: "/materials/:id/edit",
        name: "MaterialEditView",
        component: MaterialEditView,
        meta: {
            title: "titles.materialEdit"
        }
    },
    {
        path: "/materials",
        name: "MaterialListView",
        component: MaterialListView,
        meta: {
            title: "titles.materials"
        }
    },

    {
        path: "/purchases/add",
        name: "PurchaseAddView",
        component: PurchaseAddView,
        meta: {
            title: "titles.purchaseAdd"
        }
    },
    {
        path: "/purchases/:id/edit",
        name: "PurchaseEditView",
        component: PurchaseEditView,
        meta: {
            title: "titles.purchaseEdit"
        }
    },
    {
        path: "/purchases/:id",
        name: "PurchaseDetailView",
        component: PurchaseDetailView,
        meta: {
            title: "titles.purchaseDetail"
        }
    },
    {
        path: "/purchases",
        name: "PurchaseListView",
        component: PurchaseListView,
        meta: {
            title: "titles.purchases"
        }
    },

    {
        path: "/daily-logs/add",
        name: "DailyLogAddView",
        component: DailyLogAddView,
    },
    {
        path: "/daily-logs/:id",
        name: "DailyLogDetailView",
        component: DailyLogDetailView,
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