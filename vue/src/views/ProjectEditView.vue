<template>
    <h1>Project Edit View</h1>

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

    onMounted(() => {
        store.fetchProject(route.params.slug)
    })

    const updateProject  = async (data) => {
        await store.updateProject(route.params.slug, data)
    }
</script>