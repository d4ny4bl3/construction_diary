<template>
    <h2>DailyLog Add view</h2>

    <DailyLogForm @submit="createDailyLog" :submit-label="t('utils.create')" />
</template>

<script setup>
import { useI18n } from 'vue-i18n';
import { useRouter } from 'vue-router';
import { useDailyLogStore } from '@/stores/dailyLogStore';
import DailyLogForm from '@/components/DailyLogForm.vue';

const store = useDailyLogStore()
const router = useRouter()
const { t } = useI18n()

const createDailyLog = async (data) => {
    try {
        const created = await store.createDailyLog(data)
        router.push({
            name: "DailyLogDetailView",
            params: {
                id: created.id,
            }
        })
    } catch (error) {
        console.error("Error adding daily log.", error)
    }
}
</script>