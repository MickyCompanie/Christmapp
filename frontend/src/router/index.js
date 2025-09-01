import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '../stores/auth';

import Signin from '../pages/Signin.vue';
import Signup from '../pages/Signup.vue';
import Template from '../template/Template.vue';
import Home from '../pages/Home.vue';
import User from '../pages/User.vue';

const routes = [
    {
        path: "/signin",
        name: "signin",
        component: Signin,
    },
    {
        path: "/signup",
        name: "signup",
        component: Signup,
    },
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
                path: "/user/:id",
                name: "user",
                component: User,
            },
        ]
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});


router.beforeEach((to, from, next) => {
    const store = useAuthStore();

    if(to.meta.requiresAuth && !store.isAuthenticated) {
        next({ name: 'signin' });
    } else if(to.name === 'signin' && store.isAuthenticated) {
        next({ name: 'home' });
    } else {
        next();
    }
});

export default router;