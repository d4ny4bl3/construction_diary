<template>
    <div>
        <Header />
        <div class="d-flex">
            <NavBar />
            <main class="container">
                <slot />
            </main>
        </div>
    </div>
</template>

<script setup>
    import Header from '@/views/layout/Header.vue';
    import NavBar from '@/views/layout/NavBar.vue';
</script>