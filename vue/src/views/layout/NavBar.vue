<template>
    <nav class="sidebar bg-dark text-white pt-3 vh-100">
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
                    <a
                        class="nav-link text-white d-flex justify-content-between align-items-center"
                        data-bs-toggle="collapse"
                        href="#storeSubmenu"
                        role="button"
                        aria-expanded="false"
                        aria-controls="storeSubmenu"
                    >
                        {{ t("navbar.store") }}
                        <span class="chevron">&#x25BA;</span>
                    </a>

                    <ul class="collapse ms-0" id="storeSubmenu">
                        <li class="nav-item">
                            <RouterLink :to="{ name: 'MaterialListView' }" class="nav-link text-white">
                                {{ t("navbar.materials") }}
                            </RouterLink>
                        </li>
                        <li class="nav-item">
                            <RouterLink :to="{ name: 'PurchaseListView' }" class="nav-link text-white">
                                {{ t("navbar.purchases") }}
                            </RouterLink>
                        </li>
                    </ul>
                </li>
            </ul>

            <ul class="nav flex-column">
                <li class="nav-item">
                    <RouterLink :to="{ name: 'DailyLogListView' }" class="nav-link text-white">Denni zaznamy</RouterLink>
                </li>
            </ul>
        </div>
    </nav>
</template>

<script setup>
import { useI18n } from 'vue-i18n';
const { t } = useI18n()
</script>

<style>
.sidebar {
    width: 200px;
    min-width: 200px;
    max-width: 200px;
    overflow-y: auto;
}

a[aria-expanded="true"] .chevron {
    transform: rotate(90deg);
    transition: transform 0.2s ease;
}
a[aria-expanded="false"] .chevron {
    transition: transform 0.2s ease;
}
nav ul li {
    list-style: none;
}

.sidebar .nav-link {
    border-radius: 3px;
    padding: 10px 20px;
    border-bottom: 2px solid rgb(255, 255, 255, 0.1);
}

.sidebar .nav-link:hover,
.sidebar .nav-link:focus {
    background-color: rgba(255, 255, 255, 0.1);
    text-decoration: none;
}

.sidebar .nav-link.active {
    background-color: rgba(255, 255, 255, 0.25);
    font-weight: bold;
}

</style>