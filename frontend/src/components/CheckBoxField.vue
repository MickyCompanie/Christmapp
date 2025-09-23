<template>
    <div class="flex items-center mb-4">
        <input 
            :id="id" 
            type="checkbox" 
            :checked="modelValue"
            @change="$emit('update:modelValue', !modelValue)" 
            class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
        >
        <label :for="id" class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">{{ title }}</label>
    </div>
</template>

<script setup>

defineProps({
    title: {
        type: String,
        required: true
    },
    modelValue: Boolean,
    id: String,
    name: String,
})

defineEmits(["update:modelValue"]);
</script>