<template>
    <h2>Purchases Edit View</h2>

    <PurchaseForm @submit="updatePurchase" :purchase="store.purchase" :submit-label="t('utils.saveChanges')" />
</template>

<script setup>
import { onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { useMaterialStore } from '@/stores/materialStore';
import PurchaseForm from '@/components/PurchaseForm.vue';

const store = useMaterialStore()
const route = useRoute()
const router = useRouter()
const { t } = useI18n()

const id = route.params.id

onMounted(async () => {
    try {
        await store.fetchPurchase(id)
    } catch (error) {
        console.error("Error loading purchase.", error)
    }
})

const updatePurchase = async (data) => {
    try {
        await store.updatePurchase(id, data)
        router.push({
            name: "PurchaseDetailView",
            params: {
                id: id
            }
        })
    } catch (error) {
        console.error("Error updating purchase.", error)
    }
}

</script>