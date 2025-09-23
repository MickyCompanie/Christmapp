<template>
    <Page>
        <Card>
            <CardHeader :showBackButton="true" />
            <PersonForm 
                v-if="person"
                :person="person"
                :buttonTitle="'Update Person'"
                @submit="onPersonUpdate()"
            />
        </Card>
    </Page>
</template>

<script setup>
import { usePersonStore } from '@/stores/person';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

import Page from '@/template/Page.vue';
import Card from '@/template/Card.vue';
import CardHeader from '@/components/CardHeader.vue';
import PersonForm from '@/components/forms/PersonForm.vue';

const personStore = usePersonStore();

let person = ref(null);
let route = useRoute();

function onPersonUpdate() {
    personStore.updatePersonAction(person.value);  
}

onMounted(async () => {
    await personStore.getSpecificPersonAction(route.params.uid);
    person.value = personStore.getPerson
});
</script>