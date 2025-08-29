<template>
<main class="bg-gray-50 dark:bg-gray-900">
  <div class="flex flex-col items-center justify-center px-6 pt-8 mx-auto md:h-screen pt:mt-0 dark:bg-gray-900">
    <a  class="flex items-center justify-center mb-8 text-2xl font-semibold lg:mb-10 dark:text-white select-none">
        <img src="../assets/christmapp_logo.png" class="mr-4 h-11" alt="Christmapp Logo">
        <span>Christmapp</span>  
    </a>
    <div class="w-full max-w-xl p-6 space-y-8 sm:p-8 bg-white rounded-lg shadow dark:bg-gray-800">
        <slot/>
    </div>
</div>
</main>
</template>

<script setup>
</script>