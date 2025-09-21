<template>
  <div v-if="giftStatusStore.getGiftStatus" class="space-y-6 p-4">
    
    <div class="flex items-center gap-3">
      <h2 class="text-3xl font-bold text-gray-900 dark:text-white">
        status
      </h2>
    </div>

    
    <div>
      <p class="text-base leading-relaxed text-gray-600 dark:text-gray-400">
        a {{ giftStatusStore.getGiftStatus.color }} badge displaying the status: "{{ giftStatusStore.getGiftStatus.name }}"
      </p>
    </div>
  </div>
</template>


<script setup>

import { useGiftStatusStore } from '@/stores/giftStatus';
import { onMounted } from 'vue';

const props = defineProps({
    giftStatusUid: {
        type: String,
        required: true
    }
})

const giftStatusStore = useGiftStatusStore();


onMounted(async () => {
    await giftStatusStore.getSpecificGiftStatusAction(props.giftStatusUid);
});

</script>