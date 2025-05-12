<template>
  <MainLayout v-if="userStore.isLoggedIn">
    <router-view />
  </MainLayout>

  <router-view v-else />
</template>

<script setup>
  import { useUserStore } from '@/stores/user';
  import MainLayout from '@/views/layout/MainLayout.vue';

  const userStore = useUserStore()
  userStore.fetchUser()
</script>

<style scoped>

</style>
