<template>
    <div class="card mb-4">
        <div class="card-header">
            <div class="d-flex justify-content-between">
                <h3>{{ t("dailyLog.detail") }}</h3>
                <div class="d-flex gap-2">
                    <RouterLink
                        :to="{ name: 'DailyLogEditView', params: { id: id } }"
                        class="btn btn-secondary"
                    >
                        {{ t("utils.edit") }}
                    </RouterLink>
                    <button
                        class="btn btn-danger"
                        @click="deleteDailyLog"
                    >
                        {{ t("utils.delete") }}
                    </button>
                </div>
            </div>
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-6">
                    <dl class="row gy-3 align-items-center">
                        <dt class="col-6">{{ t("dailyLog.title") }}:</dt>
                        <dd class="col-6">{{ dailyLog.title }}</dd>

                        <dt class="col-6">{{ t("dailyLog.description") }}:</dt>
                        <dd class="col-6">{{ dailyLog.description }}</dd>

                        <dt class="col-6">{{ t("dailyLog.project") }}:</dt>
                        <dd class="col-6">{{ dailyLog.project_name }}</dd>

                        <dt class="col-6">{{ t("dailyLog.date") }}:</dt>
                        <dd class="col-6">{{ dailyLog.date ? d(new Date(dailyLog.date), "dateOnly") : "--" }}</dd>
                    </dl>
                </div>
                <div class="col-6">
                    <dl class="row gy-3 align-items-center">
                        <dt class="col-6">{{ t("dailyLog.from") }}:</dt>
                        <dd class="col-6">{{ dailyLog.start_time }}</dd>

                        <dt class="col-6">{{ t("dailyLog.to") }}:</dt>
                        <dd class="col-6">{{ dailyLog.end_time }}</dd>

                        <dt class="col-6">{{ t("dailyLog.duration") }}:</dt>
                        <dd class="col-6">{{ dailyLog.work_time }}</dd>
                    </dl>
                </div>
            </div>
        </div>
    </div>

    <!-- Material Usage -->
    <div class="card">
        <div class="card-header d-flex justify-content-between align-items-center">
            <h3>{{ t("materialUsage.label") }}</h3>
            <button class="btn btn-success" @click="openUsageModal">{{ t("materialUsage.add") }}</button>
        </div>
        <div class="card-body">
            <table v-if="materialUsages.length" class="table table-striped table-hover table-responsive-md text-center">
                <thead>
                    <tr>
                        <th>{{ t("materialUsage.name") }}</th>
                        <th>{{ t("materialUsage.quantity") }}</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                        v-for="usage in materialUsages"
                        :key="usage.id"
                    >
                        <td>{{ usage.material_name}}</td>
                        <td>{{ usage.used_quantity }} {{ usage.unit }}</td>
                        <td>

                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- Modal for material usage -->
     <div
        v-if="showUsageModal"
        class="modal fade show d-block"
        tabindex="-1"
    >
        <div class="modal-dialog modal-lg modal-dialog-centered">
            <div class="modal-content">

                <div class="modal-header">
                    <h5 class="modal-title">{{ t("materialUsage.add") }}</h5>
                    <button type="button" class="btn-close" @click="closeUsageModal"></button>
                </div>

                <form @submit.prevent="submit">
                    <div class="modal-body">
                        <MaterialUsageForm
                            ref="materialForm"
                            :materials="materials"
                        />
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" @click="closeUsageModal">
                            {{ t("utils.close") }}
                        </button>
                        <button type="submit" class="btn btn-primary">
                            {{ t("utils.save") }}
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <div
        v-if="showUsageModal"
        class="modal-backdrop fade show"
    ></div>
</template>

<script setup>
import { onMounted,computed, ref } from 'vue';
import { RouterLink, useRoute, useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { useDailyLogStore } from '@/stores/dailyLogStore';
import { useMaterialStore } from '@/stores/materialStore';
import MaterialUsageForm from '@/components/MaterialUsageForm.vue';

const route = useRoute()
const router = useRouter()
const { t, d } = useI18n()

const dailyLogStore = useDailyLogStore()
const materialStore = useMaterialStore()

const id = route.params.id
const dailyLog = computed(() => dailyLogStore.dailyLog)
const materialUsages = computed(() => dailyLogStore.materialUsages)

const materialForm = ref([])
const materials = ref([])
const showUsageModal = ref(false)

onMounted(async () => {
    try {
        await dailyLogStore.fetchDailyLog(id)
        await materialStore.fetchMaterials()
        await dailyLogStore.fetchMaterialUsages(id)
        materials.value = materialStore.materials
    } catch (error) {
        console.error("Error loading daily log.", error)
    }
})

const openUsageModal = () => {
    showUsageModal.value = true
}

const closeUsageModal = () => {
    showUsageModal.value = false
}

const submit = async () => {
    try {
        const data = materialForm.value.getData()

        await dailyLogStore.createMaterialUsage(id, data)
        closeUsageModal()

        await dailyLogStore.fetchMaterialUsages(id)
    } catch (error) {
        console.error("Error adding material usage.", error)
    }
}

const deleteDailyLog = async () => {
    const confirm = window.confirm("Opravdu chcete smazat denni zaznam?")
    if (!confirm) return

    try {
        await dailyLogStore.deleteDailyLog(id)
        router.push({ name: "DailyLogListView" })
    } catch (error) {
        console.error("Error deleting daily log.", error)
    }
}
</script>