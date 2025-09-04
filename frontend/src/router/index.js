import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@/stores/index.js';

import Signin from '@/pages/Signin.vue';
import Signup from '@/pages/Signup.vue';
import Template from '@/template/Template.vue';
import Home from '@/pages/Home.vue';
import User from '@/pages/User.vue';
import SignAll from '@/template/SignAll.vue';
import Profile from '@/pages/Profile.vue';

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
                path: "user",
                name: "userlist",
                component: User,
            },
            {
                path: "user/:id",
                name: "userDetail",
                component: User,
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