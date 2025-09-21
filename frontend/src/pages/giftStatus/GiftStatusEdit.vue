<template>
    <CardHeader :showBackButton="true" />
    <GiftStatusForm 
        :gift-status="giftStatus"
        buttonTitle="Update Status"
        @submit="onSubmit"
    />
</template>

<script setup>
import { useGiftStatusStore } from '@/stores/giftStatus';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

import CardHeader from '@/components/CardHeader.vue'
import GiftStatusForm from '@/components/forms/GiftStatusForm.vue';

const giftStatusStore = useGiftStatusStore()
const route = useRoute()

let giftStatus = ref(null)

function onSubmit(){
    giftStatusStore.updateGiftStatusAction(giftStatus.value)
}

onMounted(async () => {
    await giftStatusStore.getSpecificGiftStatusAction(route.params.uid)
    giftStatus.value = giftStatusStore.getGiftStatus

})
</script>