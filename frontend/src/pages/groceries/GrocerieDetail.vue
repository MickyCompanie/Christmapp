<template>
  <div v-if="groceriesStore.getGrocerie" class="space-y-6 p-4">
    
    <div v-if="groceriesStore.getGrocerie.title" class="flex items-center gap-3">
        <h2 class="text-3xl font-bold text-gray-900 dark:text-white">
            {{ groceriesStore.getGrocerie.title }}
        </h2>
    </div>

    <div v-if="groceriesStore.getGrocerie.description">
        <h3 class="font-bold text-gray-900 dark:text-white mb-2"> Status </h3>
        <Badge  
            :title="groceriesStore.getGrocerie.status.name"
            :color="groceriesStore.getGrocerie.status.color" 
        />
    </div>
 
    
    <div v-if="groceriesStore.getGrocerie.description">
        <h3 class="font-bold text-gray-900 dark:text-white"> Description </h3>
        <p class="text-base leading-relaxed text-gray-600 dark:text-gray-400">
            {{ groceriesStore.getGrocerie.description }}
        </p>
    </div>

    <div>
        <h3 class="font-bold text-gray-900 dark:text-white"> Assigned Person </h3>
      <p 
        v-if="groceriesStore.getGrocerie.assigned_person" 
        class="text-base leading-relaxed text-gray-600 dark:text-gray-400"
      >
        {{ `${groceriesStore.getGrocerie.assigned_person.first_name} ${groceriesStore.getGrocerie.assigned_person.last_name}` }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { useGroceriesStore } from '@/stores/groceries'
import { onMounted } from 'vue';

import Badge from '@/components/Badge.vue'

const groceriesStore = useGroceriesStore()

const props = defineProps({
    grocerieUid: {
        type: String,
        required: true
    }
})

onMounted(async () => {
    await groceriesStore.getSpecificGrocerieAction(props.grocerieUid);
});

</script>