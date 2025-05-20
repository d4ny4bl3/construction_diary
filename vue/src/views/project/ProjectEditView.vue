<template>
    <h1>{{ t("headers.projectEdit") }}</h1>

    <ProjectForm @submit="updateProject" :project="store.project" :submit-label="t('utils.saveChanges')" />
</template>

<script setup>
    import ProjectForm from '@/components/ProjectForm.vue';
    import { useI18n } from 'vue-i18n';
    import { onMounted } from 'vue';
    import { useRoute, useRouter } from 'vue-router';
    import { useProjectStore } from '@/stores/projectStore';

    const { t } = useI18n()
    const route = useRoute()
    const router = useRouter()
    const store = useProjectStore()
    const id = route.params.id
    const slug = route.params.slug

    onMounted(async () => {
        try {
            await store.fetchProject(id, slug)
        } catch (error) {
            console.error("Error loading project", error)
        }
    })

    const updateProject  = async (data) => {
        try {
            await store.updateProject(id, slug, data)
            router.push({
            name: "ProjectDetailView",
            params: {
                id: store.project.id,
                slug: store.project.slug,
            }
        })
        } catch (error) {
            console.error("Error updating project", error)
        }

    }
</script>