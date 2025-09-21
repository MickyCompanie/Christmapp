<template>
    <CardHeader :showBackButton="true" />
    <StatusForm 
        :status="giftStatus"
        buttonTitle="Create Status"
        @submit="onSubmit"
    />
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useGiftStatusStore } from '@/stores/giftStatus/index.js';
import CardHeader from '@/components/CardHeader.vue';
import StatusForm from '@/components/forms/StatusForm.vue';

const giftStatusStore = useGiftStatusStore();

const giftStatus = ref(null);

function onSubmit() {
    giftStatusStore.createGiftStatusAction(giftStatus.value);
}

onMounted(async () => {
    await giftStatusStore.getEmptyGiftStatusAction();
    giftStatus.value = giftStatusStore.giftStatus;
});

</script>