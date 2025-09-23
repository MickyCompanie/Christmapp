<template>
    <Page>
        <Card>
            <CardHeader :showBackButton="true" />
            <PersonForm 
                v-if="person"
                :person="person"
                buttonTitle="Create A Person"
                @submit="onPersonCreate()"
            />
        </Card>
    </Page>
</template>

<script setup>
import { usePersonStore } from '@/stores/person';
import { onMounted, ref } from 'vue';

import Page from '@/template/Page.vue';
import Card from '@/template/Card.vue';
import CardHeader from '@/components/CardHeader.vue';
import PersonForm from '@/components/forms/PersonForm.vue';

const personStore = usePersonStore();

let person = ref(null);

function onPersonCreate() {
    personStore.createPersonAction(person.value);  
}

onMounted(async () => {
    await personStore.getEmptyPersonAction();
    person.value = { ...personStore.getPerson }
});
</script>