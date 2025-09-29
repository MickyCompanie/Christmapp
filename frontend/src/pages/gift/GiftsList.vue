<template>
    <Page>
        <Card>
            <div class="select-none flex flex-col sm:flex-row sm:justify-between sm:items-center">
                <div class="flex gap-x-4 ">
                    <GiftIcon class="w-8 h-8 text-blue-400text-gray-500 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"/>
                    <h5 class="mb-2 text-2xl font-semibold tracking-tight text-gray-900 dark:text-white">
                        Gifts
                    </h5>
                </div>
                <div>
                    <ButtonCustom title="Create A Gift" :icon="PlusIcon" @click="onAddGift()" />
                </div>
            </div>

            <div class="overflow-x-auto relative shadow-md sm:rounded-lg mt-4">
                <TableStriped 
                    v-if="giftStore.getGifts.length > 0"
                    :table-heads="giftStore.getTableHeads" 
                    :table-data="giftStore.getGifts"
                    :attributes="giftStore.getAttributes"
                    ownerAttribute="buyer_uid"
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
            <GiftDetail 
                :gift-uid="selectedGiftUid"
            />
        </ModalWrapper>
    </Page>
</template>

<script setup>
import { GiftIcon, PlusIcon } from '@heroicons/vue/24/solid';
import { useGiftStore } from '@/stores/gift'
import { useRouter } from 'vue-router';
import { onMounted, ref } from 'vue';

import Page from '@/template/Page.vue';
import Card from '@/template/Card.vue';
import ButtonCustom from '@/components/ButtonCustom.vue'
import TableStriped from '@/components/TableStriped.vue';
import ModalWrapper from '@/components/ModalWrapper.vue'
import GiftDetail from '@/pages/gift/GiftDetail.vue';

const giftStore = useGiftStore()
const router = useRouter()
const selectedGiftUid = ref(null)
const isModalOpen = ref(false)

function onAddGift(){
    router.push({name: 'giftCreate'})
}

function onRowClick(uid){
    selectedGiftUid.value = uid
    isModalOpen.value = true
}

function onModalClose(){
    isModalOpen.value = false
    selectedGiftUid.value = null
    giftStore.resetGiftAction()

}

function onEdit(uid){
    router.push({name: 'giftEdit', params: { uid: uid } })
}

function onDelete(uid){
    giftStore.deleteGiftAction(uid)
}

onMounted(async () => {
    await giftStore.getAllGiftsAction()
})

</script>