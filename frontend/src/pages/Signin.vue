<template>
<SignAll>
    <h2 class="text-2xl font-bold text-gray-900 dark:text-white select-none">
            Sign in to platform 
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
        

        <div class="flex items-start">
            <div class="flex items-center h-5">
                <input id="remember" aria-describedby="remember" name="remember" type="checkbox" class="w-4 h-4 border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-600" required="">
            </div>
            <div class="ml-3 text-sm">
            <label for="remember" class="font-medium text-gray-900 dark:text-white">Remember me</label>
            </div>
            <a href="#" class="ml-auto text-sm text-primary-700 hover:underline dark:text-primary-500">Lost Password?</a>
        </div>
        <button @click="proceedToLogin()" type="button" class="text-white bg-blue-700 cursor-pointer hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">Sign In</button>
        <div class="text-sm font-medium text-gray-500 dark:text-gray-400">
            Not registered? <a class="text-primary-700 hover:underline dark:text-primary-500">Create account</a>
        </div>
    </form>
</SignAll>
  

</template>


<script setup>
import { ref } from "vue"
import InputField from "@/components/InputField.vue"
import SignAll from "@/template/SignAll.vue";
import { useAuthStore } from "@/stores/auth/index.js";

const email = ref("")
const password = ref("")

const store = useAuthStore();

function proceedToLogin(creds) {
  store.login({email: email.value, password: password.value});
}
</script>