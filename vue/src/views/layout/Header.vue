<template>
    <div class="d-flex justify-content-between align-items-center bg-dark px-3 py-3 text-white">
        <span class="navbar-brand">{{ t("navbar.brand") }}</span>
        <div v-if="userStore.isLoggedIn" class="text-white">
            {{ t("navbar.loggedInAs") }}: {{ userStore.user.username }}
            <button @click="logout" class="btn btn-sm btn-outline-light ms-3">{{ t("navbar.logout") }}</button>
        </div>
  </div>
</template>

<script setup>
    import { useRouter } from 'vue-router';
    import { useUserStore } from '@/stores/userStore'
    import { useI18n } from 'vue-i18n';

    const { t } = useI18n()
    const userStore = useUserStore()
    const router = useRouter()

    const logout = async () => {
        await userStore.logout()
        router.push({name: "Login"})
    }
</script>