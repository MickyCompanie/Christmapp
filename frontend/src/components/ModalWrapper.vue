<template>
    <div 
        v-if="isModalOpen"
        class="fixed top-0 right-0 left-0 z-50 flex justify-center items-center w-full h-screen bg-black bg-opacity-50"
    >
    <div class="relative p-4 w-full max-w-2xl max-h-full">
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
        <!-- Modal header -->
        <div
            v-if="title"
            class="flex items-center justify-between p-4 border-b rounded-t dark:border-gray-600"
        >
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
            {{ title }}
            </h3>
            <button 
                @click="onModalClose()"
                class="text-gray-400 hover:text-gray-900 dark:hover:text-white"
            >
            ✕
            </button>
        </div>
        <!-- Modal body -->
        <div class="p-4 space-y-4">
            <slot />
            <!-- Tu peux afficher ici les détails du souhait -->
        </div>
        <!-- Modal footer -->
        <div 
            v-if="footer"
            class="flex justify-end p-4 border-t dark:border-gray-600"
        >
            <button @click="onModalClose()"
                    class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
            Fermer
            </button>
        </div>
        </div>
    </div>
    </div>
</template>

<script setup>

const emit = defineEmits(['modalClose'])

function onModalClose(){
    emit('modalClose')
}

defineProps({
    isModalOpen: {
        type: Boolean,
        required: true
    },
    title: {
        type: String,
        required: false
    },
    footer: {
        type: Boolean,
        required: false,
        default: false
    }
})
</script>