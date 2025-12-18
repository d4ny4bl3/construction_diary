<template>
    <RouterLink
        :to="{ name: 'MaterialAddView' }"
        class="btn btn-primary mb-3"
    >
        {{ t("material.buttonNew") }}
    </RouterLink>

    <div class="card">
        <div class="card-header">
            <h3>{{ t("headers.materials") }}</h3>
        </div>
        <div class="card-body">
            <table class="table table-striped table-hover table-responsive-md text-center">
                <thead>
                    <tr>
                        <th>{{ t("material.name") }}</th>
                        <th>{{ t("material.stock") }}</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                        v-for="material in store.materials"
                        :key="material.id"
                    >
                        <td class="col-5">{{ material.name }}</td>
                        <td class="col-2">{{ material.stock }} {{ material.unit.name }}</td>
                        <td class="col-5">
                            <div class="d-flex gap-4 justify-content-center">
                                <button
                                    class="btn btn-outline-secondary"
                                    @click="goToEdit(material.id)"
                                >
                                    {{ t("utils.edit") }}
                                </button>
                                <button
                                    class="btn btn-outline-danger"
                                    @click="deleteMaterial(material)"
                                >
                                    {{ t("utils.delete") }}
                                </button>
                            </div>
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

const { t } = useI18n()
const store = useMaterialStore()
const router = useRouter()

onMounted(() => {
    try {
        store.fetchMaterials()
    } catch (error) {
        console.error("Error loading materials.", error)
    }
})

const goToEdit = (materialId) => {
    router.push({
        name: "MaterialEditView",
        params: {
            id: materialId,
        }
    })
}

const deleteMaterial = async (material) => {
    const confirm = window.confirm(`${t("confirm.deleteMaterial")} "${material.name}"?`)
    if (!confirm) return

    try {
        await store.deleteMaterial(material.id)
        await store.fetchMaterials()
    } catch (error) {
        console.error("Error deleting material.", error)
    }
}
</script>