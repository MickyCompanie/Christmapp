<template>
<Page>
        <Card>
            <CardHeader :showBackButton="true" />
            <WishForm 
                v-if="wish"
                :wish="wish"
                :buttonTitle="'Update Wish'"
                @submit="onWishUpdate()"
            />
        </Card>
    </Page>
</template>

<script setup>
import { useWishStore } from '@/stores/wish';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

import Page from '../template/Page.vue';
import Card from '../template/Card.vue';
import CardHeader from '../components/CardHeader.vue';
import WishForm from '../components/forms/WishForm.vue';

const wishesStore = useWishStore();

let wish = ref(null);
let route = useRoute();

function onWishUpdate() {
    wishesStore.updateWishAction(wish.value);  
}

onMounted(async () => {
    await wishesStore.getSpecificWishAction(route.params.uid);
    if (wishesStore.wish) {
        wish.value = { ...wishesStore.wish }
    }
});

</script>