<template>
    <div class="flex flex-col h-screen">
        <NavBar />
        <Sidebar />
        <div class="bg-gray-900 flex-1 overflow-auto">
            <router-view />
        </div>
    </div>
</template>

<script setup>
import NavBar from '@/template/NavBar.vue';
import Sidebar from './Sidebar.vue';
</script>