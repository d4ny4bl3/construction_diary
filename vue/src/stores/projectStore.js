import { defineStore } from 'pinia'
import api from '@/api'

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

        async fetchProject(id, slug) {
            const response = await api.get(`/projects/${id}/${slug}/`)
            this.project = response.data
        },

        async createProject(data) {
            const response = await api.post("/projects/add/", data)
            this.projects.push(response.data)
        },

        async updateProject(id, slug, data) {
            const response = await api.patch(`/projects/${id}/${slug}/edit/`, data)
            this.project = response.data
        },

        async deleteProject(slug) {
            const response = await api.delete(`/projects/${slug}/`)
            this.projects = this.projects.filter(p => p.slug != slug)
        },

        async fetchStatuses() {
            const response = await api.get(`/projects/statuses/`)
            this.statuses = response.data
        }
    }
})