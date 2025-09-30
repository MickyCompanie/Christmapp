<template>
    <Page>
        <Card>
            <CardHeader :showBackButton="true" />
            <GrocerieForm
                v-if="grocerie"
                :grocerie="grocerie"
                :persons="groceriesStore.getPersons"
                :statuses="groceriesStore.getStatuses"
                buttonTitle="Create An Item"
                @submit="onGrocerieCreate()"
            />
        </Card>
    </Page>
</template>

<script setup>
import { useGroceriesStore } from '@/stores/groceries'
import { onMounted, ref } from 'vue';

import Page from '@/template/Page.vue'
import Card from '@/template/Card.vue'
import CardHeader from '@/components/CardHeader.vue'
import GrocerieForm from '@/components/forms/GrocerieForm.vue';

const groceriesStore = useGroceriesStore()
const grocerie = ref(null)

function onGrocerieCreate() {
    groceriesStore.createGrocerieAction(grocerie.value);  
}

onMounted(async () => {
    await groceriesStore.getEmptyGrocerieAction();
    grocerie.value = { ...groceriesStore.getGrocerie }
});
</script>