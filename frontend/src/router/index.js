import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@/stores/index.js';

import Signin from '@/pages/Signin.vue';
import Signup from '@/pages/Signup.vue';
import Template from '@/template/Template.vue';
import Home from '@/pages/Home.vue';
import User from '@/pages/User.vue';
import SignAll from '@/template/SignAll.vue';
import Profile from '@/pages/Profile.vue';
import GroceriesList from '@/pages/GroceriesList.vue';
import WishesList from '@/pages/WishesList.vue';
import WishEdit from '../pages/wish/WishEdit.vue';
import WishCreate from '@/pages/WishCreate.vue';
import Settings from '../template/Settings.vue';
import GiftsList from '@/pages/GiftsList.vue';
import GiftStatusList from '../pages/giftStatus/GiftStatusList.vue';
import GiftStatusCreate from '@/pages/giftStatus/GiftStatusCreate.vue'
import GiftStatusEdit from '../pages/giftStatus/GiftStatusEdit.vue';
import GroceriesStatusList from '../pages/groceriesStatus/GroceriesStatusList.vue';
import GroceriesStatusCreate from '../pages/groceriesStatus/GroceriesStatusCreate.vue';
import GroceriesStatusEdit from '../pages/groceriesStatus/GroceriesStatusEdit.vue';

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
                path: "groceries",
                name: "grocerieslist",
                component: GroceriesList,
            },
            {
                path: "user",
                name: "userlist",
                component: User,
            },
            {
                path: "user/:id",
                name: "userDetail",
                component: User,
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