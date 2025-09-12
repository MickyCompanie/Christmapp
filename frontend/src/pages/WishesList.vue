<template>
    <Page>
        <Card>
           <div class="select-none flex flex-col sm:flex-row sm:justify-between sm:items-center">
                <div class="flex gap-x-4 ">
                    <SparklesIcon class="w-8 h-8 text-blue-400text-gray-500 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"/>
                    <h5 class="mb-2 text-2xl font-semibold tracking-tight text-gray-900 dark:text-white">
                        Wishes
                    </h5>
                </div>
                <div>
                    <ButtonCustom title="Make A Wish" :icon="PlusIcon" @click="onAddWish()" />
                </div>
            </div>

            <div class="overflow-x-auto relative shadow-md sm:rounded-lg mt-4">
                <TableStriped 
                    :table-heads="wishesStore.getTableHeads" 
                    :attributes="wishesStore.getAttributes"
                    @click:row="onRowClick"                
                    @click:edit="onEdit"
                    @click:delete="onDelete"
                />
            </div>
        </Card>
    </Page>
</template>

<script setup>
import { SparklesIcon, PlusIcon } from '@heroicons/vue/24/solid';

import { useWishStore } from '@/stores/wish';
import { onMounted, ref } from 'vue';

import Page from '../template/Page.vue';
import Card from '../template/Card.vue';
import TableStriped from '../components/TableStriped.vue';
import ButtonCustom from '../components/ButtonCustom.vue';

const wishesStore = useWishStore();

function onAddWish() {
  console.log("Navigate to add wish page")
  showModal();
}

function onRowClick(uid) {
  console.log("Navigate to wish with UID:", uid)
}

function onEdit(uid) {
  console.log("Edit wish with UID:", uid)
}

function onDelete(uid) {
  console.log("Delete wish with UID:", uid)
  wishesStore.deleteWishAction(uid);
}

onMounted(() => {
    wishesStore.getAllWishesAction();
});

</script>