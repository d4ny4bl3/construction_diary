<template>
    <div class="d-flex justify-content-between align-items-center bg-dark px-3 py-3 text-white">
        <span class="navbar-brand">Stavební deník</span>
        <div v-if="userStore.isLoggedIn" class="text-white">
            Přihlášen: {{ userStore.user.username }}
            <button @click="logout" class="btn btn-sm btn-outline-light ms-3">Odhlásit</button>
        </div>
  </div>
</template>

<script setup>
    import { useRouter } from 'vue-router';
    import { useUserStore } from '@/stores/user'

    const userStore = useUserStore()
    const router = useRouter()

    const logout = async () => {
        await userStore.logout()
        router.push({name: "Login"})
    }
</script>