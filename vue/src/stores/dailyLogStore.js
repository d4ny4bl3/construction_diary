import { defineStore } from "pinia";
import api from '@/api';

export const useDailyLogStore = defineStore("dailyLog", {
    state: () => ({
        dailyLogs: [],
        dailyLog: {},
        materialUsages: [],
        materialUsage: {},
    }),

    actions: {
        async fetchDailyLogs() {
            const response = await api.get("/daily-logs/")
            this.dailyLogs = response.data
        },
        async fetchDailyLog(id) {
            const response = await api.get(`/daily-logs/${id}`)
            this.dailyLog = response.data
        },
        async createDailyLog(data) {
            const response = await api.post("/daily-logs/add/", data)
            this.dailyLogs.push(response.data)
            this.dailyLog = response.data
            return response.data
        },
        async updateDailyLog(id, data) {
            const response = await api.patch(`/daily-logs/${id}/edit/`, data)
            this.material = response.data
        },
        async deleteDailyLog(id) {
            await api.delete(`/daily-logs/${id}/delete/`)
            this.dailyLogs = this.dailyLogs.filter(d => d.id != id)
        },

        async fetchMaterialUsages(dailyLogId) {
            try {
                const response = await api.get(`/daily-logs/${dailyLogId}/usages/`)
                this.materialUsages = response.data
            } catch (error) {
                console.error("Error loading material usages", error)
            }
        },
        async fetchMaterialUsage(dailyLogId, usageId) {
            try {
                const response = await api.get(`/daily-logs/${dailyLogId}/usages/${usageId}`)
                this.materialUsage = response.data
            } catch (error) {
                console.error("Error loading material usage", error)
            }
        },
        async createMaterialUsage(dailyLogId, data) {
            try {
                const response = await api.post(`/daily-logs/${dailyLogId}/usages/add/`, data)
                this.materialUsages.push(response.data)
                this.materialUsage = response.data
                return response.data
            } catch (error) {
                console.error("Error creating material usage.", error)
            }
        },
        async deleteMaterialUsage(dailyLogId, usageId) {
            try {
                await api.delete(`/daily-logs/${dailyLogId}/usages/${usageId}/delete/`)
                this.materialUsages = this.materialUsages.filter(m => m.id != usageId)
            } catch (error) {
                console.error("Error deleting material usage.", error)
            }
        }
    }
})