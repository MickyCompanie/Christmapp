<template>
    <Page>
        <Card>
            <ListCardTitle 
                :icon="UserGroupIcon"
                title="People"
                button-text="Add A Person"
                @add="onAddPerson()"
            />

            <div class="overflow-x-auto relative shadow-md sm:rounded-lg mt-4">
                
            <PersonTable
                v-if="personStore?.getPersons?.length > 0"
                :table-heads="personStore.getTableHeads" 
                :persons="personStore.getPersons"
                :attributes="personStore.getAttributes"
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
            <PersonDetail 
                :person-uid="selectedPersonUid"
            />
        </ModalWrapper>
    </Page>
</template>

<script setup>
import { UserGroupIcon } from '@heroicons/vue/24/solid';
import { onMounted, ref } from 'vue';
import { usePersonStore } from '../../stores/person';
import { useRouter } from 'vue-router';

import Page from '@/template/Page.vue'
import Card from '@/template/Card.vue'
import ListCardTitle from '@/components/ListCardTitle.vue';
import PersonTable from '@/components/PersonTable.vue';
import ModalWrapper from '@/components/ModalWrapper.vue'
import PersonDetail from '@/pages/person/PersonDetail.vue';

const personStore = usePersonStore()
const router = useRouter()

const isModalOpen = ref(false);
const selectedPersonUid = ref(null);

function onAddPerson(){
    router.push({ name: 'personCreate' });
}

function onEdit(uid){
    router.push({ name: 'personEdit', params: { uid: uid } });
}

function onRowClick(uid){
  selectedPersonUid.value = uid;
  isModalOpen.value = true;
}

function onModalClose() {
    isModalOpen.value = false;
    personStore.resetPersonAction()
}

function onDelete(uid){
    personStore.deletePersonAction(uid)
}

onMounted(async () => {
    await personStore.getAllPersonAction()
})

</script>