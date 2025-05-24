import { defineStore } from "pinia";
import api from "@/api"

export const useMaterialStore = defineStore("material", {
    state: () => ({
        materials: [],
        material: {},
        units: [],
        purchases: [],
        purchase: {},
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
        async deleteMaterial(id) {
            await api.delete(`/materials/${id}/delete/`)
            this.materials = this.materials.filter(m => m.id != id)
        },

        async fetchUnits() {
            const response = await api.get("/units/")
            this.units = response.data
        },

        async fetchPurchases() {
            const response = await api.get("/purchases/")
            this.purchases = response.data
        },
        async fetchPurchase(id) {
            const response = await api.get(`/purchases/${id}/`)
            this.purchase = response.data
        },
        async createPurchase(data) {
            const response = await api.post("/purchases/add", data)
            this.purchases.push(response.data)
            this.purchase = response.data
            return response.data
        },
        async updatePurchase(id, data) {
            const response = await api.patch(`/purchases/${id}/edit/`, data)
            this.material = response.data
        },
        async deletePurchase(id) {
            await api.delete(`/purchases/${id}/delete/`)
            this.purchases = this.purchases.filter(p => p.id != id)
        },
    }
})