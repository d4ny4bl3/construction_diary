<template>
    <h1>Material Edit View</h1>

    <MaterialForm @submit="updateMaterial" :material="store.material" :unit="store.units" :submit-label="t('utils.saveChanges')" />
</template>

<script setup>
import { onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { useMaterialStore } from '@/stores/materialStore';
import MaterialForm from '@/components/MaterialForm.vue';

const store = useMaterialStore()
const route = useRoute()
const router = useRouter()
const { t } = useI18n()

const id = route.params.id

onMounted(async () => {
    try {
        await Promise.all([
            store.fetchMaterial(id),
            store.fetchUnits()
        ])
    } catch (error) {
        console.error("Error loading material or units.", error)
    }
})

const updateMaterial = async (data) => {
    try {
        await store.updateMaterial(id, data)
        router.push({ name: "MaterialListView" })
    } catch (error) {
        console.error("Error updating material.", error)
    }
}
</script>