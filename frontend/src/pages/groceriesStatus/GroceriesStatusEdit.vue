<template>
    <CardHeader :showBackButton="true" />
    <StatusForm 
        :status="groceriesStatus"
        buttonTitle="Update Status"
        @submit="onSubmit"
    />
</template>

<script setup>
import { useGroceriesStatusesStore } from '@/stores/groceriesStatus';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

import CardHeader from '@/components/CardHeader.vue'
import StatusForm from '@/components/forms/StatusForm.vue';

const groceriesStatusStore = useGroceriesStatusesStore()
const route = useRoute()

let groceriesStatus = ref(null)

function onSubmit(){
    groceriesStatusStore.updateGroceriesStatusAction(groceriesStatus.value)
}

onMounted(async () => {
    await groceriesStatusStore.getSpecificGroceriesStatusAction(route.params.uid)
    groceriesStatus.value = groceriesStatusStore.getGroceriesStatus

})
</script>