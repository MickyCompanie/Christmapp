<template>
    <Page>
        <Card>
            <CardHeader :showBackButton="true" />
            <WishForm 
                v-if="wish"
                :wish="wish"
                @submit="onWishCreate()"
            />
        </Card>
    </Page>
</template>

<script setup>
import { useWishStore } from '@/stores/wish';
import { onMounted, ref } from 'vue';

import Page from '../template/Page.vue';
import Card from '../template/Card.vue';
import CardHeader from '../components/CardHeader.vue';
import WishForm from '../components/forms/WishForm.vue';

const wishesStore = useWishStore();

let wish = ref(null);

function onWishCreate() {
    wishesStore.createWishAction(wish.value);  
}

onMounted(async () => {
    await wishesStore.getEmptyWishAction();
    wish.value = { ...wishesStore.wish }
});

</script>