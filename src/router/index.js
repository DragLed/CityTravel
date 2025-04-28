// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import MainComponent from '../components/mainComponent.vue'
import ExcursionPage from '../components/excursionPage.vue'



const routes = [
  { path: '/', component: MainComponent },
  { path: '/excursion/:id', component: ExcursionPage, name: 'excursion' }
]

const router = createRouter({
    history: createWebHistory(),
    routes
  });

export default router