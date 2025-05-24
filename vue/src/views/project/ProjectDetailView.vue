<template>
    <h2 class="mb-3">{{ t("headers.projectDetail") }}</h2>
    <div class="card mb-3">
        <div class="card-header">
            <div class="d-flex justify-content-between">
                <h3>{{ store.project.name }}</h3>
                <div class="d-flex gap-2">
                    <RouterLink
                        :to="{ name: 'ProjectEditView', params: { id: id, slug: slug } }"
                        class="btn btn-secondary"
                    >
                        {{ t("utils.edit") }}
                    </RouterLink>
                    <button
                        class="btn btn-danger"
                        @click="deleteProject"
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
                        <dt class="col-4">{{ t("project.start_date") }}:</dt>
                        <dd class="col-8">{{ project.start_date ? d(new Date(project.start_date), "dateOnly") : "--" }}</dd>

                        <dt class="col-4">{{ t("project.end_date") }}:</dt>
                        <dd class="col-8">{{ project.end_date ? d(new Date(project.end_date), "dateOnly") : "--" }}</dd>
                    </dl>
                </div>
                <div class="col-6">
                    <dl class="row gy-3">
                        <dt class="col-4">{{ t("project.location") }}:</dt>
                        <dd class="col-8">{{ project.location }}</dd>

                        <dt class="col-4">{{ t("project.status") }}:</dt>
                        <dd class="col-8">{{ project.status_name }}</dd>
                    </dl>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, computed } from 'vue';
import { useProjectStore } from '@/stores/projectStore';
import { useRoute, useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';

const store = useProjectStore()
const route = useRoute()
const router = useRouter()
const { t, d } = useI18n()

const id = route.params.id
const slug = route.params.slug

const project = computed(() => store.project)

onMounted(async () => {
    try {
        await Promise.all([
            store.fetchProject(id, slug),
            store.fetchStatuses()
        ])
    } catch (error) {
        console.error("Error loading project or statuses", error)
    }
})

const deleteProject = async () => {
    const confirm = window.confirm(t("confirm.deleteProject"))
    if (!confirm) return

    try {
        await store.deleteProject(id, slug)
        router.push({ name: "ProjectListView" })
    } catch (error) {
        console.error("Error deleting project.", error)
    }
}
</script>