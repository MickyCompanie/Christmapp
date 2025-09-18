<template>
    <div class="flex flex-col h-screen">
        <NavBar />
        <Sidebar 
            :user="authStore.getUser"
        />
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

const authStore = useAuthStore();

onMounted(() => {
    authStore.getCurrentUser();
});
</script>