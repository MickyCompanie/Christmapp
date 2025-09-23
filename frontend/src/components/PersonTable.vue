<template>
    <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
    <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
                <th v-for="head in tableHeads" :key="head" scope="col" class="px-6 py-3 select-none">
                    {{ head }}
                </th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="person in persons" class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 border-gray-200">
                <td v-for="attribute in attributes" @click="$emit('click:row', person.uid)" class="px-6 py-4 select-none cursor-pointer">
                    {{ person[attribute] || '-'}}
                </td>
                <td class="px-6 py-4">
                    <div v-if="authStore?.user?.role === 'admin' || !person['user']" @click="$emit('click:edit', person.uid)" class="font-medium text-blue-600 dark:text-blue-500 hover:underline cursor-pointer">
                        <pencil-icon class="w-5 h-5"/>
                    </div>
                </td>
                <td class="px-6 py-4">
                    <div v-if="authStore?.user?.role === 'admin' || !person['user']" @click="$emit('click:delete', person.uid)" class="font-medium text-blue-600 dark:text-blue-500 hover:underline cursor-pointer">
                        <trash-icon class="w-5 h-5"/>
                    </div>
                </td>
            </tr>
        </tbody>
    </table>
</div>
</template>

<script setup>
import { useAuthStore } from '../stores/auth';
import { PencilIcon, TrashIcon } from '@heroicons/vue/24/solid';

const authStore = useAuthStore();

defineProps({
    tableHeads: {
        type: Array,
        required: false,
        default: () => ["Title", "Created At", "Updated At", "Edit", "Delete"]
    },
    persons: {
        type: Array,
        required: true,
    },
    attributes: {
        type: Array,
        required: false,
        default: () => ["title", "description", "createdAt", "updatedAt"]
    },
})

defineEmits(['click:edit', 'click:delete', 'click:row'])
</script>