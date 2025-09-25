<template>
    <div>
        <label :for="id" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{{ title }}</label>
        <select 
            :id="id"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            :placeholder="placeholder"
            :value="modelValue"
            @change="$emit('update:modelValue', $event.target.value)"
        >
            <template v-if="statuses" v-for="status in statuses" :key="status.uid">
                <option :value="status.uid">
                    <Badge  
                        :title="status.name"
                        :color="status.color" 
                    />
                </option>
            </template>
        </select>
    </div>
    
</template>

<script setup>
import Badge from '@/components/Badge.vue'

defineProps({
    title: String,
    modelValue: String,
    type: {
        type: String,
        required: false,
        default: "text"
    },
    id: String,
    name: String,
    statuses: {
        type: Array,
        required: true,
    }
})

defineEmits(["update:modelValue"]);
</script>