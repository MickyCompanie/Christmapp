<template>
  <div v-if="status" class="space-y-6 p-4">
    
    <div class="flex items-center gap-3">
      <h2 class="text-3xl font-bold text-gray-900 dark:text-white">
        status
      </h2>
    </div>

    
    <div>
      <p class="text-base leading-relaxed text-gray-600 dark:text-gray-400">
        a {{ status.color }} badge displaying the status: "{{ status.name }}"
      </p>
    </div>
  </div>
</template>


<script setup>
const props = defineProps({
    status: Object,
})
</script>