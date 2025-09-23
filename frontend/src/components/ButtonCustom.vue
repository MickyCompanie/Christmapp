<template>
    <button 
    @click="$emit('click')" 
    :type="type" 
    class="flex items-center gap-2 text-white bg-blue-700 cursor-pointer hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
    >
        <component v-if="icon"  :is="icon" class="w-5 h-5" />
        <span>
            {{ title }}
        </span>
    </button>
</template>

<script setup>

defineProps({
    title: {
        type: String,
        required: true
    },
    icon: {
    type: {
        type: String,
        required: false,
        default: "button"
    }, 
    required: false,
    default: null
  }

});
defineEmits(['click']);
</script>