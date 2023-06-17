import  { createRouter, createWebHistory } from 'vue-router';

import Dashboard from './pages/Dashboard.vue';
import Home from './pages/Home.vue';
import Registration from './pages/Registration.vue';
import Requests from './pages/Requests.vue';
import Admin from './pages/Admin.vue';
import NotFound from './pages/NotFound.vue';

export default  createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', redirect: '/home'},
        { path: '/home', component: Home},
        { path: '/register', component: Registration},
        { path: '/dashboard', component: Dashboard},
        { path: '/admin', component: Admin },
        { path: '/requests', component: Requests},
        { path: '/:notFound(.*)', component: NotFound},
    ]
})