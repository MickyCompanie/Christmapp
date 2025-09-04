<template>
    <Page>
        <Card>
            <div class="select-none">
                <h5 class="mb-2 text-2xl font-semibold tracking-tight text-gray-900 dark:text-white">Votre Profil</h5>
                <p v-if="person" class="mb-3 font-extralight text-gray-500 dark:text-gray-400">vous etes parmis nous depuis le {{ new Date(person.created_at).toLocaleDateString('fr-FR') }}</p>
            </div>
            <div v-if="person" class="w-full py-4 grid grid-cols-1 md:grid-cols-2 gap-4 rounded-md">
                <InputField 
                   v-model="person.first_name"
                   title="prenom"
                   id="first_name"
                   name="first name"
                   placeholder=""
               />
                <InputField 
                   v-model="person.last_name"
                   title="nom"
                   id="first_name"
                   name="first name"
                   placeholder=""
               />
                <InputField 
                   v-model="person.phone_number"
                   title="numero de telephone"
                   id="phone_number"
                   name="phone_number"
                   placeholder=""
               />
                <InputField 
                   v-model="person.street_address"
                   title="adresse"
                   id="street_address"
                   name="street_address"
                   placeholder=""
               />
                <InputField 
                   v-model="person.city"
                   title="ville"
                   id="city"
                   name="city"
                   placeholder=""
               />
                <InputField 
                   v-model="person.post_code"
                   title="code postal"
                   id="post_code"
                   name="post_code"
                   placeholder=""
               />
            </div>
            <div v-if="person && hasPersonChanged(person, authStore.user.person)" class="flex w-full justify-end py-2">
                 <button @click="updateButtonCall()" type="button" class="text-white bg-blue-700 cursor-pointer hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">Update</button>
            </div>
        </Card>
    </Page>
</template>

<script setup>
import { ref, onMounted, onBeforeMount } from 'vue';
import { useAuthStore } from '../stores/auth';
import Card from '../template/Card.vue';
import Page from '../template/Page.vue';
import InputField from "@/components/InputField.vue";

const authStore = useAuthStore()
const person = ref(null)

function hasPersonChanged(person, originalPerson) {
  return JSON.stringify(person) !== JSON.stringify(originalPerson);
}

function updateButtonCall(){
    authStore.proceedToUpdatePerson(person.value)
}

onMounted(async () => {
  await authStore.getCurrentUser()
  if (authStore.user?.person) {
    person.value = { ...authStore.user.person }
  }
})

</script>