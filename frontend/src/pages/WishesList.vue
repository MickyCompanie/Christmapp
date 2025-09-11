<template>
    <Page>
        <Card>
           <div class="select-none flex flex-col sm:flex-row sm:justify-between sm:items-center">
                <h5 class="mb-2 text-2xl font-semibold tracking-tight text-gray-900 dark:text-white">
                    WishesList
                </h5>
                <div>
                    <button class="px-4 py-2 bg-blue-500 text-white rounded">Action</button>
                </div>
            </div>

            <div class="overflow-x-auto relative shadow-md sm:rounded-lg mt-4">
                <TableStriped :table-heads="wishesStore.getTableHeads" :attributes="wishesStore.getAttributes"/>
            </div>
        </Card>
    </Page>
</template>

<script setup>
import { useWishStore } from '@/stores/wish';
import { onMounted } from 'vue';

import Page from '../template/Page.vue';
import Card from '../template/Card.vue';
import TableStriped from '../components/TableStriped.vue';

const wishesStore = useWishStore();

onMounted(() => {
    wishesStore.getAllWishesAction();
});

</script>