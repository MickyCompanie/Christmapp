<template>
    <Page>
        <Card>
            <ListCardTitle 
                :icon="ShoppingCartIcon"
                title="Groceries"
                button-text="add an item"
                @add="onAddGrocerie()"
            />

            <div class="overflow-x-auto relative shadow-md sm:rounded-lg mt-4">
                <TableStriped 
                    v-if="groceriesStore.getGroceries.length > 0"
                    :table-heads="groceriesStore.getTableHeads" 
                    :table-data="groceriesStore.getGroceries"
                    :attributes="groceriesStore.getAttributes"
                    ownerAttribute=""
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
            <GrocerieDetail 
                :grocerie-uid="selectedGrocerieUid"
            />
        </ModalWrapper>
    </Page>
</template>

<script setup>
import { ShoppingCartIcon } from '@heroicons/vue/24/solid';
import { useGroceriesStore } from '@/stores/groceries'
import { useRouter } from 'vue-router'
import { onMounted, ref } from 'vue';

import Page from '@/template/Page.vue';
import Card from '@/template/Card.vue';
import ListCardTitle from '@/components/ListCardTitle.vue'
import TableStriped from '@/components/TableStriped.vue'
import ModalWrapper from '@/components/ModalWrapper.vue'
import GrocerieDetail from '@/pages/groceries/GrocerieDetail.vue'

const router = useRouter()
const groceriesStore = useGroceriesStore()
const isModalOpen = ref(false)
const selectedGrocerieUid = ref(null)

function onAddGrocerie(){
    router.push({name: 'groceriesCreate'})
}

function onRowClick(uid){
    selectedGrocerieUid.value = uid
    isModalOpen.value = true
}

function onModalClose(){
    isModalOpen.value = false
    selectedGrocerieUid.value = null
    groceriesStore.resetGrocerieAction()

}

function onEdit(uid){
    router.push({name: 'groceriesEdit', params: { uid: uid } })
}

function onDelete(uid){
    groceriesStore.deleteGrocerieAction(uid)
}

onMounted(async () => {
    await groceriesStore.getAllGroceriesAction()
})

</script>