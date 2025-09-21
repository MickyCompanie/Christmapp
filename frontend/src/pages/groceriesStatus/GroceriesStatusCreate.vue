<template>
    <CardHeader :showBackButton="true" />
    <StatusForm 
        :status="groceriesStatus"
        buttonTitle="Create Status"
        @submit="onSubmit"
    />
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useGroceriesStatusesStore } from '@/stores/groceriesStatus';
import CardHeader from '@/components/CardHeader.vue';
import StatusForm from '@/components/forms/StatusForm.vue';

const groceriesStatusStore = useGroceriesStatusesStore();

const groceriesStatus = ref(null);

function onSubmit() {
    groceriesStatusStore.createGroceriesStatusAction(groceriesStatus.value);
}

onMounted(async () => {
    await groceriesStatusStore.getEmptyGroceriesStatusAction();
    groceriesStatus.value = groceriesStatusStore.groceriesStatus;
});
</script>