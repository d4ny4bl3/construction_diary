<template>
    <h2>{{ t("headers.materialAdd") }}</h2>

    <MaterialForm @submit="createMaterial" :submit-label="t('utils.create')"/>
</template>

<script setup>
import MaterialForm from '@/components/MaterialForm.vue';
import { useMaterialStore } from '@/stores/materialStore';
import { useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';

const store = useMaterialStore()
const router = useRouter()
const { t } = useI18n()

const createMaterial = async (data) => {
    try {
        await store.createMaterial(data)
        router.push({ name: "MaterialListView" })
    } catch (error) {
        console.error("Error adding material.", error)
    }
}
</script>