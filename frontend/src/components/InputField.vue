<template>
    <div>
        <label 
            :for="id" 
            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >
            {{title}}
        </label>
        <input 
            :id="id" 
            :name="name" 
            :type="type" 
            :placeholder="placeholder" 
            class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" 
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)" 
            required=""
        >
    </div>
</template>

<script setup>
defineProps({
    title: String,
    modelValue: String,
    placeholder: String,
    type: {
        type: String,
        default: "text"
    },
    id: String,
    name: String,
})

defineEmits(["update:modelValue"]);
</script>