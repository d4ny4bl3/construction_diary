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
            <input type="date" class="form-control" id="EndDate" v-model="EndDate" required>
        </div>

        <div class="my-4">
            <button type="submit" class="btn btn-primary w-100 py-3 fw-bold fs-5 text-white">{{ label }}</button>
        </div>
    </form>
</template>

<script setup>
    import { ref, watch, computed } from 'vue';
    import { useI18n } from 'vue-i18n';

    const { t } = useI18n()

    const props = defineProps({
        project: {
            type: Object,
            default: null,
        },
        submitLabel: {
            type: String,
            default: "",
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

    watch(
        () => props.project,
        (newProject) => {
            if (newProject) {
                name.value = newProject.name || ""
                location.value = newProject.location || ""
                StartDate.value = newProject.StartDate || ""
                EndDate.value = newProject.EndDate || ""
            }
        },
        { immediate: true }
    )

    const submit = () => {
        emit("submit", {
            name: name.value,
            location: location.value,
            start_date: StartDate.value,
            end_date: EndDate.value,
        })
    }

</script>