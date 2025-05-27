import { defineStore } from "pinia";
import api from '@/api';

export const useDailyLogStore = defineStore("dailyLog", {
    state: () => ({
        dailyLogs: [],
        dailyLog: {},
    }),

    actions: {
        async createDailyLog(data) {
            const response = await api.post("/daily-logs/add/", data)
            this.dailyLogs.push(response.data)
            this.material = response.data
            return response.data
        }
    }
})