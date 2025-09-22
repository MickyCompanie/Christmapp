<template>
  <div
    v-if="authStore?.getUsers?.length > 0"  
    class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 justify-items-center"
  >
    <UserCard 
      v-for="user in authStore.getUsers"
      :key="user"
      :user="user"
      @upgrade="onUpgrade"
      @downgrade="onDowngrade"
    />
  </div>
</template>


<script setup>
import { useAuthStore } from '../../stores/auth';
import { onMounted, ref } from 'vue';
import UserCard from '@/components/UserCard.vue';

const authStore = useAuthStore()

function onUpgrade(uid){
  authStore.upgradeUserRoleAction(uid)
}

function onDowngrade(uid){
  authStore.downgradeUserRoleAction(uid)
}

onMounted(async () => {
    await authStore.getAllUsersAction()

})
</script>