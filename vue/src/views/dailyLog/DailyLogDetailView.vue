<template>
    <h2>Detail DailyLog</h2>

    <div class="card">
        <div class="card-header">
            <div class="d-flex justify-content-between">
                <h3>{{ dailyLog.title }}</h3>
            </div>
        </div>
        <div class="card-body">
            <pre>{{ dailyLog }}</pre>
            <div class="row">
                <div class="col-12">
                    <dl class="row gy-3 align-items-center">
                        <dt class="col-6">Popis:</dt>
                        <dd class="col-6">{{ dailyLog.description }}</dd>
                    </dl>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted,computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
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
</script>