<template>
    <h2 class="mb-3">Detail nakupu</h2>
    <div class="card mb-3">
        <div class="card-header">
            <div class="d-flex justify-content-between">
                <h3>{{ material.name }} - {{ purchase.buy_at ? d(new Date(purchase.buy_at), "dateOnly") : "" }}</h3>
                <RouterLink
                    :to="{ name: 'PurchaseEditView', params: { id: id } }"
                    class="btn btn-primary"
                >
                    {{ t("utils.edit") }}
                </RouterLink>
            </div>
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-12">
                    <dl class="row gy-3 align-items-center">
                        <dt class="col-6">Pouzity material:</dt>
                        <dd class="col-6">{{ material.name }}</dd>

                        <dt class="col-6">Množství</dt>
                        <dd class="col-6">{{ purchase.quantity }} {{ material.unit?.name }}</dd>

                        <dt class="col-6">Cena za jednotku:</dt>
                        <dd class="col-6">{{ purchase.price_per_unit }} Kč</dd>

                        <dt class="col-6">Zakoupeno:</dt>
                        <dd class="col-6">{{ purchase.buy_at ? d(new Date(purchase.buy_at), "dateOnly") : "" }}</dd>
                    </dl>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { useMaterialStore } from '@/stores/MaterialStore'

const route = useRoute()
const store = useMaterialStore()
const { t, d } = useI18n()

const id = route.params.id

const purchase = computed(() => store.purchase)
const material = computed(() => store.material)

onMounted(async () => {
    try {
        await store.fetchPurchase(id)

        const materialId = store.purchase?.material
        if (materialId) {
            await store.fetchMaterial(materialId)
        }
    } catch (error) {
        console.error("Error loading purchase.", error)
    }
})
</script>