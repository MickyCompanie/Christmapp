<template>
  <div v-if="wishesStore.getWish" class="space-y-6 p-4">
    
    <div class="flex items-center gap-3">
      <h2 class="text-3xl font-bold text-gray-900 dark:text-white">
        {{ wishesStore.getWish.title }}
      </h2>
    </div>

    
    <div>
      <p class="text-base leading-relaxed text-gray-600 dark:text-gray-400">
        {{ wishesStore.getWish.description }}
      </p>
    </div>

    <!--
    <div>
      <p class="text-base text-gray-600 dark:text-gray-400">
        {{ wishesStore.getWish.someOtherField }}
      </p>
    </div>
    -->
  </div>
</template>


<script setup>

import { useWishStore } from '@/stores/wish';
import { onMounted } from 'vue';

const props = defineProps({
    wishUid: {
        type: String,
        required: true
    }
})

const wishesStore = useWishStore();


onMounted(async () => {
    await wishesStore.getSpecificWishAction(props.wishUid);
});

</script>