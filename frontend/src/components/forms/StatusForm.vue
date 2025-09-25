<template>
    <form @submit.prevent="$emit('submit')">
        <div v-if="status" class="w-full py-4 grid grid-cols-1 gap-4 rounded-md px-4 md:px-8">
            <InputField 
            v-model="status.name"
            title="name"
            id="name"
            name="name"
            placeholder="tag name..."
            />
            <SelectField 
            v-model="status.color"
            title="color"
            id="color"
            name="color"
            placeholder="select color..."
            :options="badgeColor" 
            />
        </div>
        
        <div class="w-full flex justify-end px-4 pt-8 md:px-8">
            <ButtonCustom :title="buttonTitle" @click="$emit('submit')" />
        </div>
    </form>
</template>

<script setup>
import { badgeColor } from '@/enums/badgeColor.js';

import InputField from '@/components/InputField.vue';
import SelectField from '@/components//SelectField.vue';
import ButtonCustom from '@/components/ButtonCustom.vue';

defineEmits(['submit']);

defineProps({
    status: {
        type: Object,
        required: true
    },
    buttonTitle: {
        type: String,
        required: false,
        default: "Make A Wish"
    }
});
</script>