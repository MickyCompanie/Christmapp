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
                    v-if="wishesStore.getWishes.length > 0"
                    :table-heads="wishesStore.getTableHeads" 
                    :table-data="wishesStore.getWishes"
                    :attributes="wishesStore.getAttributes"
                    ownerAttribute="wisher_uid"
                    @click:row="onRowClick"                
                    @click:edit="onEdit"
                    @click:delete="onDelete"
                />
            </div>
        </Card>
        <ModalWrapper
            :is-modal-open="isModalOpen"
            :footer="true"
            @modal-close="onModalClose"
        >
            <WishDetail 
                :wish-uid="selectedWishUid"
            />
        </ModalWrapper>
    </Page>
</template>

<script setup>
import { SparklesIcon, PlusIcon } from '@heroicons/vue/24/solid';

import { useWishStore } from '@/stores/wish';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

import Page from '../template/Page.vue';
import Card from '../template/Card.vue';
import ModalWrapper from '../components/ModalWrapper.vue';
import WishDetail from './WishDetail.vue';
import TableStriped from '../components/TableStriped.vue';
import ButtonCustom from '../components/ButtonCustom.vue';

const wishesStore = useWishStore();
const router = useRouter();

const isModalOpen = ref(false);
const selectedWishUid = ref(null);


function onAddWish() {
    router.push({ name: 'wishCreate' });
}

function onRowClick(uid) {
  selectedWishUid.value = uid;
  isModalOpen.value = true;
}

function onModalClose() {
    isModalOpen.value = false;
    wishesStore.resetWish()
}

function onEdit(uid) {
    router.push({ name: 'wishEdit', params: { uid: uid } });
}

function onDelete(uid) {
  wishesStore.deleteWishAction(uid);
}

onMounted(() => {
    wishesStore.getAllWishesAction();
    wishesStore.resetWish();
});

</script>