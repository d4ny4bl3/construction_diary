<template>
    <div class="d-flex justify-content-between">
        <h2>Daily Log Edit</h2>
        <RouterLink
            class="btn btn-primary"
            :to="{ name: 'DailyLogDetailView', params: { id: id } }"
        >
            {{ t("utils.back") }}
        </RouterLink>
    </div>
    <DailyLogForm :dailyLog="store.dailyLog" @submit="updateDailyLog" :submit-label="t('utils.saveChanges')" />
</template>

<script setup>
import DailyLogForm from '@/components/DailyLogForm.vue';
import { onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useDailyLogStore } from '@/stores/dailyLogStore';
import { useI18n } from 'vue-i18n';

const route = useRoute()
const router = useRouter()
const store = useDailyLogStore()
const { t } = useI18n()
const id = route.params.id

onMounted(async () => {
    try {
        await store.fetchDailyLog(id)
    } catch (error) {
        console.error("Error loading daily log.", error)
    }
})

const updateDailyLog = async (data) => {
    try {
        await store.updateDailyLog(id, data)
        router.push({
            name: "DailyLogDetailView",
            params: {
                id: id,
            }
        })
    } catch (error) {
        console.error("Error updating daily log.", error)
    }
}

</script>