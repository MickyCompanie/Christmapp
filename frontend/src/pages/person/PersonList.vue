<template>
    <Page>
        <Card>
            <div class="select-none flex flex-col sm:flex-row sm:justify-between sm:items-center">
                <div class="flex gap-x-4 ">
                    <UserGroupIcon class="w-8 h-8 text-blue-400text-gray-500 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"/>
                    <h5 class="mb-2 text-2xl font-semibold tracking-tight text-gray-900 dark:text-white">
                        People
                    </h5>
                </div>
                <div>
                    <ButtonCustom title="Add A Person" :icon="PlusIcon" @click="onAddPerson()" />
                </div>

            </div>
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
import { UserGroupIcon, PlusIcon } from '@heroicons/vue/24/solid';
import { onMounted, ref } from 'vue';
import { usePersonStore } from '../../stores/person';
import { useRouter } from 'vue-router';

import Page from '@/template/Page.vue'
import Card from '@/template/Card.vue'
import ButtonCustom from '@/components/ButtonCustom.vue'
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