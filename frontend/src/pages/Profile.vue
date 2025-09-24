<template>
    <Page>
        <Card>
            <div class="select-none">
                <h5 class="mb-2 text-2xl font-semibold tracking-tight text-gray-900 dark:text-white">Votre Profil</h5>
                <p v-if="person" class="mb-3 font-extralight text-gray-500 dark:text-gray-400">vous etes parmis nous depuis le {{ new Date(person.created_at).toLocaleDateString('fr-FR') }}</p>
            </div>
            <PersonForm 
                v-if="person"
                :person="person"
                :buttonTitle="'Update Profile'"
                @submit="updateButtonCall()"
            />

        </Card>
    </Page>
</template>

<script setup>
import { ref, onMounted, onBeforeMount } from 'vue';
import { useAuthStore } from '../stores/auth';
import Page from '@/template/Page.vue'
import Card from '@/template/Card.vue'
import PersonForm from '@/components/forms/PersonForm.vue'

const authStore = useAuthStore()
const person = ref(null)

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