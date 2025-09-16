<template>
    <Page>
        <Card>
           <div class="select-none flex flex-col sm:flex-row sm:justify-between sm:items-center">
                <div class="flex gap-x-4 ">
                    <SparklesIcon class="w-8 h-8 text-blue-400text-gray-500 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"/>
                    <h5 class="mb-2 text-2xl font-semibold tracking-tight text-gray-900 dark:text-white">
                        Wish
                    </h5>
                </div>
                <div>
                    <ButtonCustom title="Make A Wish" @click="onAddWish()" />
                </div>
            </div>
        </Card>
    </Page>
</template>

<script setup>

import { useWishStore } from '@/stores/wish';
import { onMounted } from 'vue';

import Page from '../template/Page.vue';
import Card from '../template/Card.vue';
import ButtonCustom from '../components/ButtonCustom.vue';

const wishesStore = useWishStore();


onMounted(() => {
    wishesStore.getAllWishesAction();
});

</script>