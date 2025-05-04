// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import MainComponent from '../components/mainComponent.vue'
import ExcursionPage from '../components/excursionPage.vue'
import TestComponent from '../components/TestComponent.vue';



const routes = [
  { path: '/', component: MainComponent },
  { path: '/excursion/:id', component: ExcursionPage, name: 'excursion' },
  { path: '/test', component: TestComponent }
]

const router = createRouter({
    history: createWebHistory(),
    routes
  });

export default router