<template>
    <form class="row g-4 p-3" ref="form" @submit.prevent="submit">
        <div class="col-7">
            <label for="title" class="form-label fw-bold">Nazev</label>
            <input type="text" id="title" class="form-control" v-model="title">
        </div>
        <div class="col-5">
            <label for="project" class="form-label fw-bold">Projekt</label>
            <select class="form-select" v-model="project" required>
                <option
                    v-for="project in store.projects"
                    :key="project.id"
                    :value="project.id"
                >
                    {{ project.name }}
                </option>
            </select>
        </div>
        <div class="col-12">
            <label for="description" class="form-label fw-bold">Popis</label>
            <textarea id="description" name="description" class="form-control" rows="3" v-model="description"></textarea>
        </div>
        <div class="col-4">
            <label for="date" class="form-label fw-bold">Datum</label>
            <input type="date" id="date" class="form-control" v-model="date">
        </div>
        <div class="col-4">
            <label for="start_time" class="form-label fw-bold">Od</label>
            <input type="time" id="start_time" class="form-control" v-model="startTime">
        </div>
        <div class="col-4">
            <label for="end_time" class="form-label fw-bold">Do</label>
            <input type="time" id="end_time" class="form-control" v-model="endTime" :min="startTime">
        </div>

        <div class="my-4">
            <button type="submit" class="btn btn-primary w-100 py-3 fw-bold fs-5 text-white">{{ label }}</button>
        </div>
    </form>
</template>

<script setup>
import { ref, watch, onMounted, computed } from 'vue';
import { useI18n } from 'vue-i18n';
import { useProjectStore } from '@/stores/projectStore';

const props = defineProps({
    dailyLog: {
        type: Object,
        default: null,
    },
    submitLabel: {
        type: String,
        default: ""
    }
})

const emit = defineEmits(["submit"])
const store = useProjectStore()
const { t } = useI18n()

onMounted(async () => {
    try {
        await store.fetchProjects()
    } catch (error) {
        console.error("Error loading projects.", error)
    }
})

const title = ref("")
const project = ref("")
const description = ref("")
const date = ref("")
const startTime = ref("")
const endTime = ref("")
const label = computed(() =>
    props.submitLabel || t("utils.create")
)

watch(() => props.dailyLog,
    (newVal) => {
        if (newVal) {
            title.value = newVal.title || ""
            project.value = newVal.project || null
            description.value = newVal.description || ""
            date.value = newVal.date || ""
            startTime.value = newVal.start_time || ""
            endTime.value = newVal.end_time || ""
        }
    }
)

const submit = () => {
    emit("submit", {
        title: title.value,
        project: project.value,
        description: description.value,
        date: date.value,
        startTime: startTime.value ? startTime.value + ":00" : null,
        endTime: endTime.value ? endTime.value + ":00" : null,
    })
}
</script>