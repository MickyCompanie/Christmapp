<template>
<div>
    <h2 class="text-2xl font-bold text-gray-900 dark:text-white select-none">
        Sign up to platform 
    </h2>
    <form class="mt-8 space-y-6" action="#">
        <InputField 
            v-model="email"
            title="Your email"
            id="email"
            name="email"
            placeholder="name@company.com"
            type="email"
        />


        <InputField
            v-model="password"
            title="Your password"
            id="password"
            name="password"
            placeholder=""
            type="password"
        />
        
        <button @click="proceedToSignup()" type="button" class="text-white bg-blue-700 cursor-pointer hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">Sign up</button>
        <div class="text-sm font-medium text-gray-500 dark:text-gray-400">
            Already Have An Account ? <router-link to="signin" class="text-primary-700 hover:underline dark:text-primary-500">Sign In</router-link>.
        </div>
    </form>
</div>
</template>


<script setup>
import { ref } from "vue"
import { useAuthStore, useNotificationsStore } from '@/stores';
import InputField from "@/components/InputField.vue"


const email = ref("")
const password = ref("")

const store = useAuthStore();

function proceedToSignup() {
  store.signUp({email: email.value, password: password.value});
}
</script>