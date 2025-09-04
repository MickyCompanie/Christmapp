<template>
    <li :key="key">
        <router-link :to="{name: routeName}" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
            <svg class="shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 18">
                <path :d="svgPath"/>
            </svg>
            <span class="flex-1 ms-3 whitespace-nowrap">{{ title }}</span>
        </router-link>
    </li>
</template>

<script setup>

defineProps({
    title: String,
    routeName: String,
    svgPath: String,
    key: String,
})
</script>