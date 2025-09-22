<template>
    <div v-if="user" class="w-full select-none cursor-default max-w-sm p-6 bg-white rounded-lg shadow-lg dark:bg-gray-900">
            <h5 class="break-words mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{{ user.email }}</h5>
        <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">verified: {{ user.verified || "no"}}</p>

        <div class="py-2 flex flex-row items-center gap-2">
            <p class="font-normal text-gray-700 dark:text-gray-400">role: </p>
            <Badge  
            :title="user.role"
            :color="user.role === 'user' ? 'gray' : 'yellow'" 
            />
        </div>

        <div class="mt-4 flex flex-row">
            <ButtonCustom 
            v-if="user.role === 'user'"
            title="upgrade"
            :icon="ArrowUpIcon"
            @click="$emit('upgrade', user.uid)"
            />
            <ButtonCustom 
            v-else
            title="downgrade"
            :icon="ArrowDownIcon"
            @click="$emit('downgrade', user.uid)"
            />
        </div>
    </div>
</template>

<script setup>
import { ArrowUpIcon, ArrowDownIcon } from '@heroicons/vue/24/solid'
import ButtonCustom from '@/components/ButtonCustom.vue'
import Badge from '@/components/Badge.vue'

defineProps({
    user: {
        type: Object,
        required: true
    }
});

defineEmits(['upgrade', 'downgrade'])
</script>