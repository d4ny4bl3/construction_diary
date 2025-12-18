<template>
    <RouterLink
        :to="{ name: 'DailyLogAddView' }"
        class="btn btn-primary mb-3"
    >
        {{ t("dailyLog.buttonNew") }}
    </RouterLink>

    <div class="card">
        <div class="card-header">
            <h3>{{ t("dailyLog.list") }}</h3>
        </div>
        <div class="card-body">
            <table class="table table-striped table-hover table-responsive-md text-center">
                <thead>
                    <tr>
                        <th>{{ t("dailyLog.project") }}</th>
                        <th>{{ t("dailyLog.description") }}</th>
                        <th>{{ t("dailyLog.date") }}</th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                        v-for="dailyLog in store.dailyLogs"
                        :key="dailyLog.id"
                        class="clickable-row"
                        @click="goToDailyLog(dailyLog)"
                        style="cursor: pointer;"
                    >
                        <td>{{ dailyLog.project_name }}</td>
                        <td>{{ dailyLog.title }}</td>
                        <td>{{ dailyLog.date ? d(new Date(dailyLog.date), "dateOnly") : "--" }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useDailyLogStore } from '@/stores/dailyLogStore';
import { useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';

const router = useRouter()
const store = useDailyLogStore()
const { t, d } = useI18n()

onMounted(() => {
    store.fetchDailyLogs()
})

function goToDailyLog(dailyLog) {
    router.push({
        name: "DailyLogDetailView",
        params: {
            id: dailyLog.id
        }
    })
}
</script>