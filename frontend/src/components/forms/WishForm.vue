<template>
    <div class="w-full py-4 grid grid-cols-1 gap-4 rounded-md px-4 md:px-8">
        <InputField 
            v-model="wish.title"
            title="title"
            id="title"
            name="title"
            placeholder="what do you wish for?"
        />
        <TextAreaField 
            v-model="wish.description"
            title="description"
            id="description"
            name="description"
            placeholder="Tell us more about your wish..."
        />
    </div>

    <div class="w-full flex justify-end px-4 pt-8 md:px-8">
        <ButtonCustom title="Make A Wish" @click="$emit('submit')" />
     </div>

</template>

<script setup>

import InputField from '@/components/InputField.vue';
import ButtonCustom from '@/components/ButtonCustom.vue';
import TextAreaField from '@/components/TextAreaField.vue';


defineProps({
    wish: {
        type: Object,
        required: true
    }
});

defineEmits(['submit']);
</script>