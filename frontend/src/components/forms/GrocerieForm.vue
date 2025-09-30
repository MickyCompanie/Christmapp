<template>
    <form @submit.prevent="$emit('submit')">
        <div class="w-full py-4 grid grid-cols-1 gap-4 rounded-md px-4 md:px-8">
            <InputField 
                v-model="grocerie.title"
                title="title"
                id="title"
                name="title"
                placeholder="what are you about to buy?"
            />
            <TextAreaField 
                v-model="grocerie.description"
                title="description"
                id="description"
                name="description"
                placeholder="Tell us more about your item ..."
            />
            <SelectPersonField 
                v-model="grocerie.assigned_person_uid"
                title="recipient"
                id="recipient_uid"
                name="recipient_uid"
                :persons="persons" 
            />
            <SelectStatusField 
                v-model="grocerie.status_uid"
                title="status"
                id="status"
                name="status"
                :statuses="statuses" 
            />
        </div>

        <div class="w-full flex justify-end px-4 pt-8 md:px-8">
            <ButtonCustom :title="buttonTitle" @click="$emit('submit')" />
        </div>
    </form>
</template>

<script setup>
import InputField from '@/components/InputField.vue';
import ButtonCustom from '@/components/ButtonCustom.vue';
import TextAreaField from '@/components/TextAreaField.vue';
import SelectPersonField from '@/components/SelectPersonField.vue'
import SelectStatusField from '@/components/SelectStatusField.vue'

defineProps({
    grocerie: {
        type: Object,
        required: true
    },
    persons: {
        type: Array,
        required: true
    },
    statuses: {
        type: Array,
        required: true
    },
    buttonTitle: {
        type: String,
        required: true,
    }
});

defineEmits(['submit']);
</script>