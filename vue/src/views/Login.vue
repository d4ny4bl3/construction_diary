<template>
    <div class="row justify-content-center align-items-center vh-100 w-50 mx-auto m-0">
        <div class="shadow p-5">
            <form @submit.prevent="login">
                <div class="mb-3">
                    <input type="text" v-model="username" id="username" class="form-control" :placeholder="t('login.username')" required />
                </div>
                <div class="mb-3">
                    <input type="password" v-model="password" id="password" class="form-control" :placeholder="t('login.password')" required />
                </div>

                <button type="submit" class="btn btn-primary w-100">{{t("login.button")}}</button>
            </form>
        </div>
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    import { useUserStore } from '@/stores/userStore';
    import { useRoute, useRouter } from 'vue-router';
    import { useI18n } from 'vue-i18n';

    const { t } = useI18n()

    const router = useRouter()
    const route = useRoute()

    const username = ref("")
    const password = ref("")
    const userStore = useUserStore()

    const login = async () => {
        try {
            await userStore.login({
                username: username.value,
                password: password.value
            })

            if (userStore.isLoggedIn) {
                const redirectTo = route.query.path || "/dashboard"
                await router.push(redirectTo)
            }
        } catch (error) {
            console.error("Login error", error)
        }
    }
</script>

<!-- <script>
    import { useUserStore } from '@/stores/userStore';

    export default {
        data() {
            return {
                username: "",
                password: "",
            }
        },
        methods: {
            login() {
                const store = useUserStore()

                store.login({
                    username: this.username,
                    password: this.password
                })
                .then(() => {
                    console.log("Login successful");
                })
                .catch(error => {
                    console.error("Login error", error);
                });
            },

            async login() {
                const store = useUserStore()
                await store.login({
                    username: this.username,
                    password: this.password
                })
            }
        }
    }
</script> -->

<style scoped>

</style>