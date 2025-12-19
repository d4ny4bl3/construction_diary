<template>
  <MainLayout v-if="userStore.isLoggedIn">
    <router-view />
  </MainLayout>

  <router-view v-else />
</template>

<script setup>
  import { useUserStore } from '@/stores/userStore';
  import { useRoute } from 'vue-router';
  import MainLayout from '@/views/layout/MainLayout.vue';

  const userStore = useUserStore()
  const route = useRoute()

  if (route.name !== 'Login') {
    userStore.fetchUser()
  }
</script>

<style scoped>

</style>
