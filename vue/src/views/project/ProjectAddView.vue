<template>
    <h2>{{ t("headers.projectAdd") }}</h2>

    <ProjectForm @submit="createProject" :submit-label="t('utils.create')"/>

</template>

<script setup>
    import ProjectForm from '@/components/ProjectForm.vue';
    import { useI18n } from 'vue-i18n';
    import { useProjectStore } from '@/stores/projectStore';
    import { useRouter } from 'vue-router';

    const { t } = useI18n()
    const store = useProjectStore()
    const router = useRouter()

    const createProject = async (data) => {
        try {
            const created = await store.createProject(data)
            router.push({
                name: "ProjectDetailView",
                params: {
                    id: created.id,
                    slug: created.slug,
                }
            })
        } catch (error) {
            console.error("Error adding project", error)
        }
    }
</script>