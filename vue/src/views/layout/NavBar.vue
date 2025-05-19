<template>
    <nav class="bg-dark text-white p-3 vh-100">
        <div class="container-fluid">
            <ul class="nav flex-column">
                <li class="nav-item">
                    <RouterLink to="/dashboard" class="nav-link text-white">Dashboard</RouterLink>
                </li>
            </ul>
            <ul class="nav flex-column">
                <li class="nav-item">
                    <RouterLink :to="{ name: 'ProjectListView' }" class="nav-link text-white">Projekty</RouterLink>
                </li>
            </ul>
        </div>
    </nav>
</template>