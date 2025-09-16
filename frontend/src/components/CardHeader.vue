<template>
    <div v-if="showBackButton" class="mb-4">
        <ChevronLeftIcon @click="router.back()" class="w-8 h-8 cursor-pointer  text-gray-500  dark:text-gray-400"/>
    </div>
    
    <div v-if="title" class="select-none">
        <h5 class="mb-2 text-2xl font-semibold tracking-tight text-gray-900 dark:text-white">{{ title }}</h5>
    </div>
</template>

<script setup>
import { ChevronLeftIcon } from '@heroicons/vue/24/solid';
import { useRouter } from 'vue-router';
const router = useRouter();

defineProps({
    title: {
        type: String,
        required: false
    },
    showBackButton: {
        type: Boolean,
        default: false,
        required: false
    }
});
</script>