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
        // router.push
    } catch (error) {
        console.error("Error loading purchase.", error)
    }
})

</script>