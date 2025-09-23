<template>
  <div v-if="personStore.getPerson" class="space-y-6 p-4">
    
    <div v-if="personStore.getPerson.first_name && personStore.getPerson.last_name" class="flex items-center gap-3">
      <h2 class="text-3xl font-bold text-gray-900 dark:text-white">
        {{ `${personStore.getPerson.first_name} ${personStore.getPerson.last_name}` }}
      </h2>
    </div>

    
    <div>
        <h3 class="font-bold text-gray-900 dark:text-white">
        phone number
        </h3>
        <p class="text-base leading-relaxed text-gray-600 dark:text-gray-400">
            {{ personStore.getPerson.phone_number || "this person has not registered it's phone number yet" }}
        </p>
    </div>

    <div>
        <h3 class="font-bold text-gray-900 dark:text-white">
        address
        </h3>
      <p 
        v-if="personStore.getPerson.street_address && personStore.getPerson.post_code && personStore.getPerson.city" 
        class="text-base leading-relaxed text-gray-600 dark:text-gray-400"
      >
        {{ `${personStore.getPerson.street_address} ${personStore.getPerson.post_code} ${personStore.getPerson.city}` }}
      </p>
      <p v-else class="text-base leading-relaxed text-gray-600 dark:text-gray-400">
        this person has not registered a full address yet
      </p>
    </div>
  </div>
</template>


<script setup>
import { usePersonStore } from '@/stores/person';
import { onMounted } from 'vue';

const props = defineProps({
    personUid: {
        type: String,
        required: true
    }
})

const personStore = usePersonStore();


onMounted(async () => {
    await personStore.getSpecificPersonAction(props.personUid);
});

</script>