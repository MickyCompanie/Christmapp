<template>
    <div class="flex flex-col h-screen">
        <NavBar />
        <Sidebar />
        <div class="bg-gray-900 flex-1 overflow-auto">
            <router-view />
        </div>
        <Toast />
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useAuthStore } from '@/stores/auth';

import NavBar from '@/template/NavBar.vue';
import Sidebar from './Sidebar.vue';
import Toast from '@/components/Toast.vue';

onMounted(() => {
    const authStore = useAuthStore();
    authStore.getCurrentUser();
});
</script>