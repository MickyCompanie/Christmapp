<template>
    <NavBar />
    <Sidebar />
    <router-view />
</template>

<script setup>
import NavBar from '@/template/NavBar.vue';
import Sidebar from './Sidebar.vue';
</script>