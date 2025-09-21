<template>
    <CardHeader :showBackButton="true" />
    <StatusForm 
        :status="giftStatus"
        buttonTitle="Update Status"
        @submit="onSubmit"
    />
</template>

<script setup>
import { useGiftStatusStore } from '@/stores/giftStatus';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

import CardHeader from '@/components/CardHeader.vue'
import StatusForm from '@/components/forms/StatusForm.vue';

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