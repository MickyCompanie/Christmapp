<template>
    <div class="select-none flex flex-col sm:flex-row sm:justify-between sm:items-center">
        <div class="flex gap-x-4 ">
            <component
                :is="icon"
                class="w-8 h-8 text-gray-500 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
            />
            <h5 class="mb-2 text-2xl font-semibold tracking-tight text-gray-900 dark:text-white">
                {{ title }}
            </h5>
        </div>
        <div>
            <ButtonCustom :title="buttonText" :icon="PlusIcon" @click="$emit('add')" />
        </div>
    </div>
</template>

<script setup>
import { PlusIcon } from '@heroicons/vue/24/solid';

import ButtonCustom from '@/components/ButtonCustom.vue'

defineProps({
    title: {
        type: String,
        required: true
    },
    buttonText: {
        type: String,
        required: false,
        default: 'add'
    },
    icon: {
        type: [Object, Function]
    }
})

defineEmits(['add'])
</script>