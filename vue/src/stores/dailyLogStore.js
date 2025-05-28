import { defineStore } from "pinia";
import api from '@/api';

export const useDailyLogStore = defineStore("dailyLog", {
    state: () => ({
        dailyLogs: [],
        dailyLog: {},
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
        }
    }
})