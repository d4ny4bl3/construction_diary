<template>
    <div class="d-flex justify-content-center align-items-center">
        <div class="shadow p-4 w-100 ">
            <form @submit.prevent="login">
                <div class="mb-3">
                    <input type="text" v-model="username" id="username" class="form-control" placeholder="Jméno" required />
                </div>
                <div class="mb-3">
                    <input type="password" v-model="password" id="password" class="form-control" placeholder="Heslo" required />
                </div>

                <button type="submit" class="btn btn-primary w-100">Přihlásit se</button>
            </form>
        </div>
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    import { useUserStore } from '@/stores/user';

    const username = ref("")
    const password = ref("")
    const userStore = useUserStore()

    const login = async () => {
        try {
            await userStore.login({
                username: username.value,
                password: password.value
            })
        } catch (error) {
            console.error("Login error", error)
        }

    }
</script>

<!-- <script>
    import { useUserStore } from '@/stores/user';

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