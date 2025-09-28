import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@/stores/index.js';

import Signin from '@/pages/Signin.vue';
import Signup from '@/pages/Signup.vue';
import Template from '@/template/Template.vue';
import Home from '@/pages/Home.vue';
import SignAll from '@/template/SignAll.vue';
import Profile from '@/pages/Profile.vue';
import GroceriesList from '@/pages/groceries/GroceriesList.vue';
import WishesList from '@/pages/wish/WishesList.vue';
import WishEdit from '@/pages/wish/WishEdit.vue';
import WishCreate from '@/pages/wish/WishCreate.vue';
import Settings from '@/template/Settings.vue';
import GiftsList from '@/pages/gift/GiftsList.vue';
import GiftCreate from '@/pages/gift/GiftCreate.vue';
import GiftEdit from '@/pages/gift/GiftEdit.vue';
import GiftStatusList from '@/pages/giftStatus/GiftStatusList.vue';
import GiftStatusCreate from '@/pages/giftStatus/GiftStatusCreate.vue'
import GiftStatusEdit from '@/pages/giftStatus/GiftStatusEdit.vue';
import GroceriesStatusList from '@/pages/groceriesStatus/GroceriesStatusList.vue';
import GroceriesStatusCreate from '@/pages/groceriesStatus/GroceriesStatusCreate.vue';
import GroceriesStatusEdit from '@/pages/groceriesStatus/GroceriesStatusEdit.vue';
import UserList from '@/pages/user/UserList.vue';
import PersonList from '@/pages/person/PersonList.vue';
import PersonCreate from '@/pages/person/PersonCreate.vue';
import PersonEdit from '@/pages/person/PersonEdit.vue';

const routes = [
    {
        path: "/",
        component: Template,
        meta: { requiresAuth: true },
        children: [
            {
                path: "", 
                name: "home",
                component: Home,
            },
            {
                path: "profile",
                name: "profile",
                component: Profile
            },
            {
                path: "wishes",
                name: "wisheslist",
                component: WishesList,
            },
            {
                path: "wish/:uid",
                name: "wishEdit",
                component: WishEdit,
            },
            {
                path: "wish/create",
                name: "wishCreate",
                component: WishCreate,
            },
            {
                path: "gifts",
                name: "giftlist",
                component: GiftsList,
            },
            {
                path: "gifts",
                name: "giftCreate",
                component: GiftCreate,
            },
            {
                path: "gifts/:uid",
                name: "giftEdit",
                component: GiftEdit,
            },
            {
                path: "people",
                name: "personlist",
                component: PersonList,
            },
            {
                path: "people/:uid",
                name: "personEdit",
                component: PersonEdit,
            },
            {
                path: "person/create",
                name: "personCreate",
                component: PersonCreate,
            },
            {
                path: "groceries",
                name: "grocerieslist",
                component: GroceriesList,
            },
            {
                path: "settings",
                name: "settings",
                component: Settings,
                children: [
                    {
                        path: "gift_status",
                        name: "giftStatusList",
                        component: GiftStatusList,
                    },
                    {
                        path: "gift_status/create",
                        name: "giftStatusCreate",
                        component: GiftStatusCreate,
                    },
                    {
                        path: "gift_status/:uid",
                        name: "giftStatusEdit",
                        component: GiftStatusEdit,
                    },
                    {
                        path: "groceries_status",
                        name: "groceriesStatusList",
                        component: GroceriesStatusList,
                    },
                    {
                        path: "groceries_status/create",
                        name: "groceriesStatusCreate",
                        component: GroceriesStatusCreate,
                    },
                    {
                        path: "groceries_status/:uid",
                        name: "groceriesStatusEdit",
                        component: GroceriesStatusEdit,
                    },
                    {
                        path: "users",
                        name: "userList",
                        component: UserList
                    },
                    
                ]
            },
        ]
    },
    {
        path: "/auth",
        name: "auth",
        component: SignAll,
        children: [
            {
                path: "signin",
                name: "signin",
                component: Signin,
            },
            {
                path: "signup",
                name: "signup",
                component: Signup,
            },
        ]
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});


router.beforeEach((to, from, next) => {
    const store = useAuthStore()

    if(to.meta.requiresAuth && !store.isAuthenticated) {
        next({ name: 'signin' });
    } else if(to.name === 'signin' && store.isAuthenticated) {
        next({ name: 'home' });
    } else {
        next();
    }
});

export default router;