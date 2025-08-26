import { createRouter, createWebHistory } from 'vue-router';

import Signin from '../src/pages/Signin.vue';
import Signup from '../src/pages/Signup.vue';
import SideBar from '../src/template/Sidebar.vue';
import Home from '../src/pages/Home.vue';
import User from '../src/pages/User.vue';

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
        component: SideBar,
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