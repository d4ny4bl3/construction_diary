<template>
    <h1>Project Add View</h1>

    <ProjectForm @submit="createProject" :submit-label="t('utils.create')"/>

</template>

<script setup>
    import ProjectForm from '@/components/ProjectForm.vue';
    import { useI18n } from 'vue-i18n';
    import { useProjectStore } from '@/stores/projectStore';

    const { t } = useI18n()
    const store = useProjectStore()

    const createProject = async (data) => {
        try {
            await store.createProject(data)
            router.push({name: "Dashboard"})
        } catch (error) {
            console.error("Error adding project", error)
        }
    }
</script>