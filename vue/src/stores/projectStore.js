import { defineStore } from 'pinia'
import api from '@/api'

function getCsrfToken() {
    const match = document.cookie.match(/csrftoken=([^;]+)/)
    return match ? match[1] : null
}

export const useProjectStore = defineStore("project", {
    state: () => ({
        projects: [],
        project: {},
        statuses: []
    }),

    getters: {
        getProjectBySlug: (state) => (slug) =>
            state.projects.find(p => p.slug === slug)
    },

    actions: {
        async fetchProjects() {
            const response = await api.get("/projects/")
            this.projects = response.data
        },

        async fetchProject(slug) {
            const response = await api.get(`/projects/${slug}`)
            this.project = response.data
        },

        async createProject(data) {
            const response = await api.post("/projects/", data)
            this.projects.push(response.data)
        },

        async updateProject(slug, data) {
            const response = await api.patch(`/projects/${slug}/`, data)
            this.project = response.data
        },

        async deleteProject(slug) {
            const response = await api.delete(`/projects/${slug}`)
            this.projects = this.projects.filter(p => p.slug != slug)
        },

        async fetchStatuses() {
            const response = await api.get(`/projects/statuses`)
            this.statuses = response.data
        }
    }
})