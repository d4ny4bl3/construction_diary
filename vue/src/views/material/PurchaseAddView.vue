<template>
    <h2>{{ t("headers.purchaseAdd") }}</h2>

    <PurchaseForm @submit="createPurchase" :submit-label="t('utils.create')"/>
</template>

<script setup>
import { useMaterialStore } from '@/stores/materialStore';
import { useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import PurchaseForm from '@/components/PurchaseForm.vue';

const store = useMaterialStore()
const router = useRouter()
const { t } = useI18n()

const createPurchase = async (data) => {
    try {
        const created = await store.createPurchase(data)
        router.push({
                name: "PurchaseDetailView",
                params: {
                    id: created.id,
                }
            })
    } catch (error) {
        console.error("Error adding purchase.", error)
    }
}
</script>