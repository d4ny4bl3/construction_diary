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
                    <RouterLink to="/projects/add" class="nav-link text-white">Přidat projekt</RouterLink>
                </li>
            </ul>
            <ul class="nav flex-column">
                <li class="nav-item">
                    <RouterLink to="/projects/" class="nav-link text-white">Seznam projektů</RouterLink>
                </li>
            </ul>
        </div>
    </nav>
</template>