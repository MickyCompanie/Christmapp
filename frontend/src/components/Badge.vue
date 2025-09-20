<template>
    <span :class="`*:bg-${color}-100 text-${color}-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-${color}-900 dark:text-${color}-300`">{{ title }}</span>
</template>

<script setup>
    defineProps({
        title: {
            type: String,
            required: true,
        },
        color: {
            type: String,
            required: false,
            default: "blue"
        }
    });
</script>