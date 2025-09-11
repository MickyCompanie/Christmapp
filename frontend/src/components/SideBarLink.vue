<template>
    <li :key="routeName">
        <router-link :to="{name: routeName}" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
            <component
                :is="icon"
                class="shrink-0 w-5 h-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
            />
            <span class="flex-1 ms-3 whitespace-nowrap">{{ title }}</span>
        </router-link>
    </li>
</template>

<script setup>

defineProps({
    title: String,
    routeName: String,
    icon: [ Object, Function ],
})
</script>