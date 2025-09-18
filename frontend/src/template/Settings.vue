<template>
    <Page>
        <Card>
            <div class="border-b border-gray-200 dark:border-gray-700">
                <ul class="flex flex-wrap -mb-px text-sm font-medium text-center text-gray-500 dark:text-gray-400">
                    <SettingsTabs 
                        v-for="tabs in settingsBar"
                        :route-name="tabs.routeName"
                        :title="tabs.title"
                        :icon="tabs.icon"
                    />
                </ul>
            </div>
            
            <div class="p-8">
                <RouterView />
            </div>
        </Card>
    </Page>
</template>

<script setup>
import { settingsBar } from '@/enums/settingsBar'

import Card from './Card.vue';
import Page from './Page.vue';
import SettingsTabs from '../components/SettingsTabs.vue';


</script>