<template>
    <RouterLink
        :to="{ name: 'PurchaseAddView' }"
        class="btn btn-primary mb-3"
    >
        {{ t("purchase.buttonNew") }}
    </RouterLink>
    <div class="card">
        <div class="card-header">
            <h3>{{ t("headers.purchases") }}</h3>
        </div>
        <div class="card-body">
            <table class="table table-striped table-hover table-responsive-md">
                <thead>
                    <tr>
                        <th>{{ t("purchase.date") }}</th>
                        <th>{{ t("purchase.material") }}</th>
                        <th>{{ t("purchase.quantity") }}</th>
                        <th>{{ t("purchase.price") }}</th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                        v-for="purchase in store.purchases"
                        :key="purchase.id"
                        @click="goToProject(purchase.id)"
                        class="clickable-row"
                        style="cursor: pointer;"
                    >
                        <td>{{ purchase.buy_at ? d(new Date(purchase.buy_at), "dateOnly") : "" }}</td>
                        <td>{{ purchase.material_name }}</td>
                        <td>{{ purchase.quantity }} {{ purchase.material_unit }}</td>
                        <td>{{ purchase.price }} Kč</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { useMaterialStore } from '@/stores/materialStore';

const router = useRouter()
const store = useMaterialStore()
const { t, d } = useI18n()

onMounted(() => {
    store.fetchPurchases()
})

function goToProject(purchaseId) {
    router.push({
        name: "PurchaseDetailView",
        params: {
            id: purchaseId
        }
    })
}
</script>