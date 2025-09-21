<template>
    <div class="select-none flex flex-col sm:flex-row sm:justify-between sm:items-center">
                <div class="flex gap-x-4 ">
                   
                </div>
                <div>
                    <ButtonCustom title="Create A Status" :icon="PlusIcon" @click="onAddGiftStatus()" />
                </div>
            </div>

            <div class="overflow-x-auto relative shadow-md sm:rounded-lg mt-4">
                <TableStriped 
                    v-if="giftStatusStore.getGiftStatuses.length > 0"
                    :table-heads="giftStatusStore.getTableHeads" 
                    :table-data="giftStatusStore.getGiftStatuses"
                    :attributes="giftStatusStore.getAttributes"
                    @click:row="onRowClick"                
                    @click:edit="onEdit"
                    @click:delete="onDelete"
                />
            </div>
            <ModalWrapper
                :is-modal-open="isModalOpen"
                :footer="true"
                @modal-close="onModalClose"
            >
                <StatusDetail 
                    :status="giftStatusStore.getGiftStatus"
                />
            </ModalWrapper>
</template>

<script setup>
import { PlusIcon } from '@heroicons/vue/24/solid';
import { useGiftStatusStore } from '@/stores/giftStatus';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

import ButtonCustom from '@/components/ButtonCustom.vue';
import TableStriped from '@/components/TableStriped.vue';
import ModalWrapper from '@/components/ModalWrapper.vue';
import StatusDetail from '@/pages/StatusDetail.vue';

const giftStatusStore = useGiftStatusStore();
const router = useRouter();

const giftStatuses = ref(null);
const isModalOpen = ref(false);


function onAddGiftStatus() {
    router.push({ name: 'giftStatusCreate' });
}

async function onRowClick(uid) {
    await giftStatusStore.getSpecificGiftStatusAction(uid)
    isModalOpen.value = true;
}

function onModalClose() {
    isModalOpen.value = false;
    giftStatusStore.resetGiftStatusAction();
}

function onEdit(uid) {
    router.push({ name: 'giftStatusEdit', params: { uid: uid } });
}

function onDelete(uid) {
  giftStatusStore.deleteGiftStatusAction(uid);
}

onMounted(async () => {
    giftStatusStore.resetGiftStatusAction();
    await giftStatusStore.getAllGiftStatusesAction();
    giftStatuses.value = giftStatusStore.giftStatuses;
});
</script>