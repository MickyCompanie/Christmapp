<template>
    <Page>
        <Card>
           <ListCardTitle 
                :icon="SparklesIcon"
                title="Wishes"
                button-text="Make A Wish"
                @add="onAddWish()"
            />

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
import { SparklesIcon } from '@heroicons/vue/24/solid';

import { useWishStore } from '@/stores/wish';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

import Page from '@/template/Page.vue';
import Card from '@/template/Card.vue';
import ModalWrapper from '@/components/ModalWrapper.vue';
import WishDetail from '@/pages/wish/WishDetail.vue';
import TableStriped from '@/components/TableStriped.vue';
import ListCardTitle from '@/components/ListCardTitle.vue';

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