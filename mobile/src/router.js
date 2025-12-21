import { createRouter, createWebHistory } from '@ionic/vue-router'
import TabsLayout from '@/views/TabsLayout.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      component: TabsLayout,
      children: [
        { path: "/", redirect: "/tab1"},
        {
          path: "tab1",
          component: () => import("@/views/TabOne.vue")
        },
        {
          path: "tab2",
          component: () => import("@/views/TabTwo.vue")
        },
      ]
    },

    {
      path: "/a",
      component: () => import("@/views/Ham1.vue")
    },
    {
      path: "/b",
      component: () => import("@/views/Ham2.vue")
    },
  ],
})

export default router
