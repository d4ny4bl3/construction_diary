<template>
    <RouterLink
        :to="{ name: 'MaterialAddView' }"
        class="btn btn-primary mb-3"
    >
        Pridat material
    </RouterLink>

    <div class="card">
        <div class="card-header">
            <h3>Seznam materialu</h3>
        </div>
        <div class="card-body">
            <table class="table table-striped table-hover table-responsive-md">
                <thead>
                    <tr>
                        <th>Nazev</th>
                        <th>Jednotka</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                        v-for="material in store.materials"
                        :key="material.id"
                    >
                        <td>{{ material.name }}</td>
                        <td>{{ material.unit.name }}</td>
                        <td>
                            <button
                                class="btn btn-outline-secondary"
                                @click="goToEdit(material)"
                            >
                                Upravit
                            </button>
                        </td>
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

const { t, d } = useI18n()
const store = useMaterialStore()
const router = useRouter()

onMounted(() => {
    try {
        store.fetchMaterials()
    } catch (error) {
        console.error("Error loading materials.", error)
    }
})

function goToEdit(material) {
    router.push({
        name: "MaterialEditView",
        params: {
            id: material.id,
        }
    })
}
</script>