<template>
    <h2>DailyLog Add view</h2>

    <DailyLogForm />

    <div class="my-4">
            <button type="submit" class="btn btn-primary w-100 py-3 fw-bold fs-5 text-white">{{ t("utils.create") }}</button>
        </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n';
import DailyLogForm from '@/components/DailyLogForm.vue';

const { t } = useI18n()
</script>