<template>
    <div class="card">
        <div class="card-header">
            <h3>Seznam projektů</h3>
        </div>
        <div class="card-body">
            <table class="table table-striped table-hover table-responsive-md">
                <thead>
                    <tr>
                        <th>Název projektu</th>
                        <th>Lokace</th>
                        <th>Začátek projektu</th>
                        <th>Konec projektu</th>
                        <th>Stav</th>
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
                        <td>{{ d(new Date(project.start_date), "dateOnly") }}</td>
                        <td>{{ d(new Date(project.end_date), "dateOnly") }}</td>
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

    const { d } = useI18n()
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