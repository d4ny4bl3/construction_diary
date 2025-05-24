<template>
    <nav class="bg-dark text-white p-3 vh-100">
        <div class="container-fluid">
            <ul class="nav flex-column">
                <li class="nav-item">
                    <RouterLink to="/dashboard" class="nav-link text-white">{{ t("navbar.dashboard") }}</RouterLink>
                </li>
            </ul>
            <ul class="nav flex-column">
                <li class="nav-item">
                    <RouterLink :to="{ name: 'ProjectListView' }" class="nav-link text-white">{{ t("navbar.projects") }}</RouterLink>
                </li>
            </ul>
            <ul class="nav flex-column">
                <li class="nav-item">
                    <RouterLink :to="{ name: 'MaterialListView' }" class="nav-link text-white">{{ t("navbar.materials") }}</RouterLink>
                </li>
            </ul>
            <ul class="nav flex-column">
                <li class="nav-item">
                    <RouterLink :to="{ name: 'PurchaseListView' }" class="nav-link text-white">{{ t("navbar.purchases") }}</RouterLink>
                </li>
            </ul>
        </div>
    </nav>
</template>

<script setup>
import { useI18n } from 'vue-i18n';
const { t } = useI18n()
</script>