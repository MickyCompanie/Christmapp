<template>
    <Page>
        <Card>
            <CardHeader :showBackButton="true" />
            <GiftForm
                v-if="gift"
                :gift="gift"
                :persons="giftStore.getPersons"
                :statuses="giftStore.getStatuses"
                buttonTitle="Update Gift"
                @submit="onSubmit()"
            />
        </Card>
    </Page>
</template>

<script setup>
import { useGiftStore } from '@/stores/gift';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

import Page from '@/template/Page.vue'
import Card from '@/template/Card.vue'
import CardHeader from '@/components/CardHeader.vue'
import GiftForm from '@/components/forms/GiftForm.vue';

const giftStore = useGiftStore()
const route = useRoute()

let gift = ref(null)

function onSubmit(){
    giftStore.updateGiftAction(gift.value)
}

onMounted(async () => {
    await giftStore.getSpecificGiftAction(route.params.uid)
    gift.value = giftStore.getGift

})
</script>