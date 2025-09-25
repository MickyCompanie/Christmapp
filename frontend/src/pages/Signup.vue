<template>
<div>
    <h2 class="text-2xl font-bold text-gray-900 dark:text-white select-none">
        Sign up to platform 
    </h2>
    <form class="mt-8 space-y-6" @submit.prevent="proceedToSignup()">
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
        
        <ButtonCustom title="Sign Up" @click="proceedToSignup()" />
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
import ButtonCustom from "@/components/ButtonCustom.vue"


const email = ref("")
const password = ref("")

const store = useAuthStore();

function proceedToSignup() {
  store.signUp({email: email.value, password: password.value});
}
</script>