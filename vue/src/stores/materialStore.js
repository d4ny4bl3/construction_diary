import { defineStore } from "pinia";
import api from "@/api"

export const useMaterialStore = defineStore("material", {
    state: () => ({
        materials: [],
        material: {},
        units: []
    }),

    actions: {
        async fetchMaterials() {
            const response = await api.get("/materials/")
            this.materials = response.data
        },
        async fetchMaterial(id) {
            const response = await api.get(`/materials/${id}/`)
            this.material = response.data
        },
        async createMaterial(data) {
            const response = await api.post("/materials/add/", data)
            this.materials.push(response.data)
            this.material = response.data
            return response.data
        },
        async updateMaterial(id, data) {
            const response = await api.patch(`/materials/${id}/edit/`, data)
            this.material = response.data
        },

        async fetchUnits() {
            const response = await api.get("/units/")
            this.units = response.data
        },
    }
})