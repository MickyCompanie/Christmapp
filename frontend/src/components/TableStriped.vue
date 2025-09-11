<template>
<div class="relative overflow-x-auto shadow-md sm:rounded-lg">
    <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
                <th v-for="head in tableHeads" :key="head" scope="col" class="px-6 py-3">
                    {{ head }}
                </th>
                <!-- <th scope="col" class="px-6 py-3">
                    Product name
                </th>
                <th scope="col" class="px-6 py-3">
                    Color
                </th>
                <th scope="col" class="px-6 py-3">
                    Category
                </th>
                <th scope="col" class="px-6 py-3">
                    Price
                </th>
                <th scope="col" class="px-6 py-3">
                    Action
                </th> -->
            </tr>
        </thead>
        <tbody>
            <tr v-for="data in tableData" class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 border-gray-200">
                <!-- <th v-for="attribute in attributes" scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    {{}}
                </th> -->
                <td v-for="attribute in attributes" class="px-6 py-4">
                    {{ data[attribute] }}
                </td>
                <td class="px-6 py-4">
                    <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</a>
                </td>
                <td class="px-6 py-4">
                    <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</a>
                </td>
            </tr>
        </tbody>
    </table>
</div>
</template>

<script setup>
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
                title: "Sample Wish 1",
                description: "This is a sample wish description.",
                created_at: "2023-10-01",
                updated_at: "2023-10-02"
            },
            {
                title: "Sample Wish 2",
                description: "This is another sample wish description.",
                wisher: "Jane Smith",
                created_at: "2023-10-03",
                updated_at: "2023-10-04"
            }
        ])
    },
    attributes: {
        type: Array,
        required: false,
        default: () => ["title", "description", "wisher", "createdAt", "updatedAt"]
    }
});

defineEmits([]);
</script>