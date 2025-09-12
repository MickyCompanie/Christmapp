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
            <tr v-for="data in tableData" class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 border-gray-200">
                <td v-for="attribute in attributes" @click="$emit('click:row', data.uid)" class="px-6 py-4 select-none cursor-pointer">
                    {{ data[attribute] }}
                </td>
                <td class="px-6 py-4">
                    <div v-if="data[ownerAttribute] === authStore.getPersonUid" @click="$emit('click:edit', data.uid)" class="font-medium text-blue-600 dark:text-blue-500 hover:underline cursor-pointer">
                        <pencil-icon class="w-5 h-5"/>
                    </div>
                </td>
                <td class="px-6 py-4">
                    <div v-if="data[ownerAttribute] === authStore.getPersonUid" @click="$emit('click:delete', data.uid)" class="font-medium text-blue-600 dark:text-blue-500 hover:underline cursor-pointer">
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
        default: () => ["Title", "Description", "Wisher", "Created At", "Updated At"]
    },
    tableData: {
        type: Array,
        required: false,
        default: () => ([
            {
                uid: 1,
                title: "Sample Wish 1",
                description: "This is a sample wish description.",
                created_at: "2023-10-01",
                updated_at: "2023-10-02"
            },
            {
                uid: 2,
                title: "Sample Wish 2",
                description: "This is another sample wish description.",
                wisher: "60235199-6bf2-43cc-a22a-a19f7ef46d35",
                created_at: "2023-10-03",
                updated_at: "2023-10-04"
            }
        ])
    },
    attributes: {
        type: Array,
        required: false,
        default: () => ["title", "description", "wisher", "createdAt", "updatedAt"]
    },
    ownerAttribute: {
        type: String,
        required: false,
        default: "wisher"
    }
});

defineEmits(["click:row", "click:edit", "click:delete"]);
</script>