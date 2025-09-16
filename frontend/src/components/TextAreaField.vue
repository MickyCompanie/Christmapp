<template>
    <div>
        <label for="message" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{ title }}</label>
        <textarea 
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"
            :id="id" 
            rows="4" 
            :placeholder="placeholder"
            class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        />
    </div>
</template>

<script setup>
defineProps({
    title: String,
    modelValue: String,
    placeholder: String,
    id: String,
    name: String,
})

defineEmits(["update:modelValue"]);
</script>