<template>
     <li class="me-2">
        <router-link 
            :to="{name: routeName}" 
            :class="['inline-flex items-center justify-center p-4 border-b-2 rounded-t-lg', route.name === routeName ? 'active text-blue-600 border-blue-600  dark:text-blue-500 dark:border-blue-500 group' : ' hover:text-gray-600 border-transparent  hover:border-gray-300 dark:hover:text-gray-300 group'
            ]"

        >
            <component
                :is="icon"
                :class="['w-4 h-4 me-2', route.name === routeName ? 'text-blue-600 dark:text-blue-500' : 'text-gray-400 dark:text-gray-500 group-hover:text-gray-500 dark:group-hover:text-gray-300']"
            /> 
            {{ title }}
        </router-link>
    </li>
</template>

<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();

defineProps({
    title: String,
    routeName: String,
    icon: [ Object, Function ],
})
</script>