import { createRouter, createWebHistory } from '@ionic/vue-router'
import MainLayout from '@/views/layouts/MainLayout.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      component: MainLayout,
      children: [
        {
          path: "",
          component: () => import("@/views/layouts/TabsLayout.vue"),
          children: [
            { path: "/", redirect: { name: "Dashboard" }},
            {
              path: "dashboard",
              name: "Dashboard",
              component: () => import("@/views/Dashboard.vue")
            },
            {
              path: "projects",
              name: "ProjectList",
              component: () => import("@/views/projects/ProjectListView.vue")
            },
            {
              path: "materials",
              name: "MaterialList",
              component: () => import("@/views/materials/MaterialListView.vue")
            },
            {
              path: "settings",
              name: "Settings",
              component: () => import("@/views/SettingsView.vue")
            },
          ]
        },
      ]
    },
  ],
})

export default router
