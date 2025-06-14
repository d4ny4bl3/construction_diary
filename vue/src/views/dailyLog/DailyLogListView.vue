<template>
    <RouterLink
        :to="{ name: 'DailyLogAddView' }"
        class="btn btn-primary mb-3"
    >
        Novy zaznam
    </RouterLink>

    <div class="card">
        <div class="card-header">
            <h3>Seznam dennich zaznamu</h3>
        </div>
        <div class="card-body">
            <table class="table table-striped table-hover table-responsive-md">
                <thead>
                    <tr>
                        <th>Projekt</th>
                        <th>Popis</th>
                        <th>Datum</th>
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