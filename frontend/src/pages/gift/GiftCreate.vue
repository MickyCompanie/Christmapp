<template>
    <Page>
        <Card>
            <CardHeader :showBackButton="true" />
            <GiftForm
                v-if="gift"
                :gift="gift"
                :persons="giftStore.getPersons"
                :statuses="giftStore.getStatuses"
                buttonTitle="Create A Gift"
                @submit="onGiftCreate()"
            />
        </Card>
    </Page>
</template>

<script setup>
import { useGiftStore } from '@/stores/gift'
import { onMounted, ref } from 'vue'

import Page from '@/template/Page.vue'
import Card from '@/template/Card.vue'
import CardHeader from '@/components/CardHeader.vue'
import GiftForm from '@/components/forms/GiftForm.vue'

const giftStore = useGiftStore();

let gift = ref(null);

function onGiftCreate() {
    giftStore.createGiftAction(gift.value);  
}

onMounted(async () => {
    await giftStore.getEmptyGiftAction();
    gift.value = { ...giftStore.getGift }
});
</script>
