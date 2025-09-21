<template>
    <div class="select-none flex flex-col sm:flex-row sm:justify-between sm:items-center">
            <div class="flex gap-x-4 ">
                
            </div>
            <div>
                <ButtonCustom title="Create A Status" :icon="PlusIcon" @click="onAddGroceriesStatus()" />
            </div>
        </div>

        <div class="overflow-x-auto relative shadow-md sm:rounded-lg mt-4">
            <TableStriped 
                v-if="groceriesStatusStore.getGroceriesStatuses?.length > 0"
                :table-heads="groceriesStatusStore.getTableHeads" 
                :table-data="groceriesStatusStore.getGroceriesStatuses"
                :attributes="groceriesStatusStore.getAttributes"
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
                :status="groceriesStatusStore.getGroceriesStatus"
            />
        </ModalWrapper>
</template>

<script setup>
import { PlusIcon } from '@heroicons/vue/24/solid';
import { useGroceriesStatusesStore } from '@/stores/groceriesStatus';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

import ButtonCustom from '@/components/ButtonCustom.vue';
import TableStriped from '@/components/TableStriped.vue';
import ModalWrapper from '@/components/ModalWrapper.vue';
import StatusDetail from '@/pages/StatusDetail.vue';

const groceriesStatusStore = useGroceriesStatusesStore();
const router = useRouter();

const groceriesStatuses = ref(null);
const isModalOpen = ref(false);


function onAddGroceriesStatus() {
    router.push({ name: 'groceriesStatusCreate' });
}

async function onRowClick(uid) {
    await groceriesStatusStore.getSpecificGroceriesStatusAction(uid)
    isModalOpen.value = true;
}

function onModalClose() {
    isModalOpen.value = false
    groceriesStatusStore.resetGroceriesStatusAction()
}

function onEdit(uid) {
    router.push({ name: 'groceriesStatusEdit', params: { uid: uid } });
}

function onDelete(uid) {
  groceriesStatusStore.deleteGroceriesStatusAction(uid);
}

onMounted(async () => {
    groceriesStatusStore.resetGroceriesStatusAction();
    await groceriesStatusStore.getAllGroceriesStatusesAction();
    groceriesStatuses.value = groceriesStatusStore.getGroceriesStatuses;
});
</script>