<template>
  <div v-if="giftStore.getGift" class="space-y-6 p-4">
    
    <div v-if="giftStore.getGift.title" class="flex items-center gap-3">
        <h2 class="text-3xl font-bold text-gray-900 dark:text-white">
            {{ giftStore.getGift.title }}
        </h2>
    </div>

    <div v-if="giftStore.getGift.description">
        <h3 class="font-bold text-gray-900 dark:text-white mb-2"> Status </h3>
        <Badge  
            :title="giftStore.getGift.status.name"
            :color="giftStore.getGift.status.color" 
        />
    </div>
 
    
    <div v-if="giftStore.getGift.description">
        <h3 class="font-bold text-gray-900 dark:text-white"> Description </h3>
        <p class="text-base leading-relaxed text-gray-600 dark:text-gray-400">
            {{ giftStore.getGift.description }}
        </p>
    </div>

    <div>
        <h3 class="font-bold text-gray-900 dark:text-white"> Recipient </h3>
      <p 
        v-if="giftStore.getGift.recipient" 
        class="text-base leading-relaxed text-gray-600 dark:text-gray-400"
      >
        {{ `${giftStore.getGift.recipient.first_name} ${giftStore.getGift.recipient.last_name}` }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { useGiftStore } from '@/stores/gift'
import { onMounted } from 'vue';

import Badge from '@/components/Badge.vue'

const giftStore = useGiftStore()

const props = defineProps({
    giftUid: {
        type: String,
        required: true
    }
})

onMounted(async () => {
    await giftStore.getSpecificGiftAction(props.giftUid);
});

</script>