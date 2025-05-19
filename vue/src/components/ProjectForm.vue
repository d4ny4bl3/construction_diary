<template>
    <form class="row g-3 p-3" ref="form" @submit.prevent="submit">
        <div class="col-12">
            <label for="name" class="form-label fw-bold">Jmeno projektu</label>
            <input type="text" class="form-control" id="name" v-model="name" required>
        </div>
        <div class="col-12">
            <label for="location" class="form-label fw-bold">Lokace</label>
            <input type="text" class="form-control" id="location" v-model="location" required>
        </div>
        <div class="col-6">
            <label for="StartDate" class="form-label fw-bold">Začátek projektu</label>
            <input type="date" class="form-control" id="StartDate" v-model="StartDate" required>
        </div>
        <div class="col-6">
            <label for="EndDate" class="form-label fw-bold">Konec projektu</label>
            <input
                type="date"
                class="form-control"
                id="EndDate"
                v-model="EndDate"
                :min="StartDate"
            >
        </div>
        <div class="col-6">
            <label for="status" class="form-label fw-bold">Status</label>
            <select class="form-select" v-model="status">
                <option
                    v-for="status in store.statuses"
                    :key="status.id"
                    :value="status.id"
                >
                    {{ status.name }}
                </option>
            </select>
        </div>

        <div class="my-4">
            <button type="submit" class="btn btn-primary w-100 py-3 fw-bold fs-5 text-white">{{ label }}</button>
        </div>
    </form>
</template>

<script setup>
    import { ref, watch, computed, onMounted } from 'vue';
    import { useProjectStore } from '@/stores/projectStore';
    import { useI18n } from 'vue-i18n';

    const store = useProjectStore()
    const { t } = useI18n()

    const props = defineProps({
        project: {
            type: Object,
            default: null,
        },
        submitLabel: {
            type: String,
            default: "",
        },
    })

    onMounted(async () => {
        try {
            await store.fetchStatuses()
        } catch (error) {
            console.error("Error loading statuses", error)
        }
    })

    const label = computed(() =>
        props.submitLabel || t("utils.create")
    )

    const emit = defineEmits(["submit"])

    const name = ref("")
    const location = ref("")
    const StartDate = ref("")
    const EndDate = ref("")
    const status = ref("")

    watch(
        () => props.project,
        (newProject) => {
            if (newProject) {
                name.value = newProject.name || ""
                location.value = newProject.location || ""
                StartDate.value = newProject.start_date || ""
                EndDate.value = newProject.end_date || ""
                status.value = newProject.status || null
            }
        },
        { immediate: true }
    )

    const submit = () => {
        emit("submit", {
            name: name.value,
            location: location.value,
            start_date: StartDate.value,
            end_date: EndDate.value || null,
            status: status.value,
        })
    }

</script>