<template>
    <RouterLink
        :to="{ name: 'ProjectAddView' }"
        class="btn btn-primary mb-3"
    >
        {{ t("project.buttonNew") }}
    </RouterLink>
    <div class="card">
        <div class="card-header">
            <h3>{{ t("headers.projects") }}</h3>
        </div>
        <div class="card-body">
            <table class="table table-striped table-hover table-responsive-md">
                <thead>
                    <tr>
                        <th>{{ t("project.name") }}</th>
                        <th>{{ t("project.location") }}</th>
                        <th>{{ t("project.start_date") }}</th>
                        <th>{{ t("project.end_date") }}</th>
                        <th>{{ t("project.status") }}</th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                        v-for="project in store.projects"
                        :key="project.id"
                        class="clickable-row"
                        @click="goToProject(project)"
                        style="cursor: pointer;"
                    >
                        <td>{{ project.name }}</td>
                        <td>{{ project.location }}</td>
                        <td>{{ project.start_date ? d(new Date(project.start_date), "dateOnly") : "--" }}</td>
                        <td>{{ project.end_date ? d(new Date(project.end_date), "dateOnly") : "--" }}</td>
                        <td>{{ project.status ? project.status_name : "--" }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script setup>
    import { useI18n } from 'vue-i18n';
    import { onMounted } from 'vue';
    import { useProjectStore } from '@/stores/projectStore';
    import { useRouter } from 'vue-router';

    const { t, d } = useI18n()
    const router = useRouter()
    const store = useProjectStore()

    onMounted(() => {
        store.fetchProjects()
    })

    function goToProject(project) {
        router.push({
            name: "ProjectDetailView",
            params: {
                id: project.id,
                slug: project.slug,
            }
        })
    }
</script>