<template>
    <RouterLink
        :to="{ name: 'PurchaseAddView' }"
        class="btn btn-primary mb-3"
    >
        Novy nakup
    </RouterLink>
    <div class="card">
        <div class="card-header">
            <h3>Seznam nakupu</h3>
        </div>
        <div class="card-body">
            <table class="table table-striped table-hover table-responsive-md">
                <thead>
                    <tr>
                        <th>Datum</th>
                        <th>Material</th>
                        <th>Mnozstvi</th>
                        <th>Cena</th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                        v-for="purchase in store.purchases"
                        :key="purchase.id"
                        @click="goToProject(purchase)"
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

function goToProject(purchase) {
    router.push({
        name: "PurchaseDetailView",
        params: {
            id: purchase.id
        }
    })
}
</script>