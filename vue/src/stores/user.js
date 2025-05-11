import { defineStore } from "pinia";
import api from '@/api';

function getCsrfToken() {
    const match = document.cookie.match(/csrftoken=([^;]+)/)
    return match ? match[1] : null
  }

export const useUserStore = defineStore("user", {
    state: () => ({
        user: {},
        error: null,
        loading: true,
    }),

    getters: {
        isLoggedIn: (state) => Object.keys(state.user).length > 0
    },

    actions: {
        async fetchUser() {
            this.loading = true
            try {
                const response = await api.get("/accounts/me/")
                this.setUser(response.data)
            } catch (error) {
                if (error.response && error.response.status === 403) {
                    this.clearUser()
                } else {
                    console.error("Error loading user", error)
                }
            } finally {
                this.loading = false
            }
        },
        async login(credentials) {
            try {
                this.loading = true
                await api.post("/accounts/login/", credentials)
                await this.fetchUser()
            } catch (error) {
                this.setError("Invalid login", error)
            } finally {
                this.loading = false
            }
        },
        async logout() {
            await api.post("/accounts/logout/", null, {
                headers: {
                    "X-CSRFTOKEN": getCsrfToken()
                  }
            })
            this.clearUser()
        },
        setUser(userData) {
            this.user = userData
            this.error = null
        },
        clearUser() {
            this.user = {}
        },
        setError(message) {
            this.error = message
        },
        resetError() {
            this.error = null
        }
    }
})