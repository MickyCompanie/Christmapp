<template>
    <li :key="item.routeName">
        <router-link 
            :to="{name: item.routeName}" 
            :class="['flex items-center p-2 group rounded-lg', route.name === item.routeName || item?.routeChildren?.includes(route.name) ? 'bg-gray-100 dark:bg-gray-700 text-white' : 'text-gray-900  dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700']"
        >
            <component
                :is="item.icon"
                :class="['shrink-0 w-5 h-5 transition duration-75', route.name === item.routeName || item?.routeChildren?.includes(route.name) ? ' group:text-blue-900 dark:group:text-white' : 'text-gray-500  group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white']"
            />
            <span class="flex-1 ms-3 whitespace-nowrap">{{ item.title }}</span>
        </router-link>
    </li>
</template>

<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();

defineProps({
    item: Object
})
</script>