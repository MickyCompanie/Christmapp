<template>
    <Page>
        <Card>
            <ListCardTitle 
                :icon="ShoppingCartIcon"
                title="Groceries"
                button-text="add an item"
                @add="onAdd()"
            />
        </Card>
    </Page>
</template>

<script setup>
import { ShoppingCartIcon } from '@heroicons/vue/24/solid';
import Page from '@/template/Page.vue';
import Card from '@/template/Card.vue';
import ListCardTitle from '@/components/ListCardTitle.vue'

function onAdd(){
    console.log('add')
}

</script>