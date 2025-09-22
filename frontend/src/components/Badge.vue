<template>
    <span :class="badgeClass">{{ title }}</span>
</template>

<script setup>

let props = defineProps({
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

    const colorMap = {
        blue: 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-300',
        red: 'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-300',
        green: 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300',
        yellow: 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-300',
    };

    const badgeClass = `${colorMap[props.color] || colorMap.blue} text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm`;

</script>