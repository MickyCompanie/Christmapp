<template>
    <form @submit.prevent="$emit('submit')">
        <div v-if="person" class="w-full py-4 grid grid-cols-1 md:grid-cols-2 gap-4 rounded-md">
            <InputField 
            v-model="person.first_name"
            title="first name"
            id="first_name"
            name="first name"
            placeholder="first name"
            />
            <InputField 
            v-model="person.last_name"
            title="last name"
            id="last_name"
            name="last name"
            placeholder="last name"
            />
            <InputField 
            v-model="person.phone_number"
            title="phone number"
            id="phone_number"
            name="phone_number"
            placeholder="ex: 0400 00 00 00"
            />
            <InputField 
                v-model="person.street_address"
                title="address"
                id="street_address"
                name="street_address"
                placeholder="street, nbr"
            />
            <InputField 
                v-model="person.city"
                title="city"
                id="city"
                name="city"
                placeholder="city"
            />
            <InputField 
                v-model="person.post_code"
                title="zip code"
                id="post_code"
                name="post_code"
                placeholder="zip code"
            />
            
            <CheckBoxField 
                v-model="person.is_pro"
                title="professional"
                id="ispro"
            />
            <InputField 
                v-if="person.is_pro === true"
                v-model="person.vat_number"
                title="vat number"
                id="vat_number"
                name="vat_number"
                placeholder="vat number"
            />
        </div>
        <div class="w-full flex justify-end px-4 pt-8 md:px-8">
            <ButtonCustom 
                :title="buttonTitle"
                type="submit"
                @click="$emit('submit')" 
            />
        </div>
    </form>
</template>

<script setup>
import InputField from '@/components/InputField.vue';
import CheckBoxField from '@/components/CheckBoxField.vue';
import ButtonCustom from '@/components/ButtonCustom.vue';

defineProps({
    person: {
        type: Object,
        required: true
    },
    buttonTitle: {
        type: String,
        required: true,
    }
});

defineEmits(['submit']);
</script>