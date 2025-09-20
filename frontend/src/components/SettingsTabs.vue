<template>
     <li v-if="item" class="me-2">
        <router-link 
            :to="{name: item.routeName}" 
            :class="['inline-flex items-center justify-center p-4 border-b-2 rounded-t-lg', route.name === item.routeName || item.childrenRoutes?.includes(route.name) ? 'active text-blue-600 border-blue-600  dark:text-blue-500 dark:border-blue-500 group' : ' hover:text-gray-600 border-transparent  hover:border-gray-300 dark:hover:text-gray-300 group'
            ]"

        >
            <component
                :is="item.icon"
                :class="['w-4 h-4 me-2', route.name === item.routeName || item.childrenRoutes?.includes(route.name) ? 'text-blue-600 dark:text-blue-500' : 'text-gray-400 dark:text-gray-500 group-hover:text-gray-500 dark:group-hover:text-gray-300']"
            /> 
            {{ item.title }}
        </router-link>
    </li>
    {{  }}
</template>

<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();

defineProps({
    item: Object,
})
</script>