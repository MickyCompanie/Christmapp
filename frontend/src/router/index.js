import { createRouter, createWebHistory } from 'vue-router';

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

export default router;