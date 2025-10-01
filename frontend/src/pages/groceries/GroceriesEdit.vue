<template>
    <Page>
        <Card>
            <CardHeader :showBackButton="true" />
            <GrocerieForm
                v-if="grocerie"
                :grocerie="grocerie"
                :persons="groceriesStore.getPersons"
                :statuses="groceriesStore.getStatuses"
                buttonTitle="Update Item"
                @submit="onSubmit()"
            />
        </Card>
    </Page>
</template>

<script setup>
import { useGroceriesStore } from '@/stores/groceries';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

import Page from '@/template/Page.vue'
import Card from '@/template/Card.vue'
import CardHeader from '@/components/CardHeader.vue'
import GrocerieForm from '@/components/forms/GrocerieForm.vue';

const groceriesStore = useGroceriesStore()
const route = useRoute()

let grocerie = ref(null)

function onSubmit(){
    groceriesStore.updateGrocerieAction(grocerie.value)
}

onMounted(async () => {
    await groceriesStore.getSpecificGrocerieAction(route.params.uid)
    grocerie.value = groceriesStore.getGrocerie

})
</script>