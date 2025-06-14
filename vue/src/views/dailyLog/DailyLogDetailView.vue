<template>
    <div class="card">
        <div class="card-header">
            <div class="d-flex justify-content-between">
                <h3>Detail zaznamu</h3>
                <div class="d-flex gap-2">
                    <RouterLink
                        :to="{ name: 'DailyLogEditView', params: { id: id } }"
                        class="btn btn-secondary"
                    >
                        {{ t("utils.edit") }}
                    </RouterLink>
                    <button
                        class="btn btn-danger"
                        @click="deleteDailyLog"
                    >
                        {{ t("utils.delete") }}
                    </button>
                </div>
            </div>
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-6">
                    <dl class="row gy-3 align-items-center">
                        <dt class="col-6">Nazev:</dt>
                        <dd class="col-6">{{ dailyLog.title }}</dd>

                        <dt class="col-6">Popis:</dt>
                        <dd class="col-6">{{ dailyLog.description }}</dd>

                        <dt class="col-6">Datum:</dt>
                        <dd class="col-6">{{ dailyLog.date ? d(new Date(dailyLog.date), "dateOnly") : "--" }}</dd>
                    </dl>
                </div>
                <div class="col-6">
                    <dl class="row gy-3 align-items-center">
                        <dt class="col-6">Od:</dt>
                        <dd class="col-6">{{ dailyLog.start_time }}</dd>

                        <dt class="col-6">Do:</dt>
                        <dd class="col-6">{{ dailyLog.end_time }}</dd>

                        <dt class="col-6">Cas prace:</dt>
                        <dd class="col-6">{{ dailyLog.work_time }}</dd>
                    </dl>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted,computed } from 'vue';
import { RouterLink, useRoute, useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { useDailyLogStore } from '@/stores/dailyLogStore';

const route = useRoute()
const router = useRouter()
const dailyLogStore = useDailyLogStore()
const { t, d } = useI18n()

const id = route.params.id

const dailyLog = computed(() => dailyLogStore.dailyLog)

onMounted(async () => {
    try {
        await dailyLogStore.fetchDailyLog(id)
    } catch (error) {
        console.error("Error loading daily log.", error)
    }
})

const deleteDailyLog = async () => {
    const confirm = window.confirm("Opravdu chcete smazat denni zaznam?")
    if (!confirm) return

    try {
        await dailyLogStore.deleteDailyLog(id)
        router.push({ name: "DailyLogListView" })
    } catch (error) {
        console.error("Error deleting daily log.", error)
    }
}
</script>