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
                    v-for="project in projectStore.projects"
                    :key="project.id"
                    :value="project.id"
                >
                    {{ project.name }}
                </option>
            </select>
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
    </form>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue';
import { useI18n } from 'vue-i18n';
import { useProjectStore } from '@/stores/projectStore';

const props = defineProps({
    dailyLog: {
        type: Object,
        default: null,
    },
    submitLabel: {
        type: String,
        default: "",
    },
})

const emit = defineEmits(["submit"])
const projectStore = useProjectStore()
const { t } = useI18n()

onMounted(async () => {
    try {
        await projectStore.fetchProjects()
    } catch (error) {
        console.error("Error loading projects.", error)
    }
})

const title = ref("")
const project = ref("")
const date = ref("")
const startTime = ref("")
const endTime = ref("")

watch(() => props.dailyLog,
    (newVal) => {
        if (newVal) {
            title.value = newVal.title || ""
            project.value = newVal.project || null
            date.value = newVal.date || ""
            startTime.value = newVal.startTime || ""
            endTime.value = newVal.endTime || ""
        }
    }
)
</script>