// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import MainComponent from '../components/Citytravel/mainComponent.vue'
import ExcursionPage from '../components/Citytravel/excursionPage.vue'
import TestComponent from '../components/TestComponent.vue';
import HomeView from '../components/CatsFactImage/HomeView.vue';
import ImageView from '../components/CatsFactImage/ImageView.vue';
import FactView from '../components/CatsFactImage/FactView.vue';
import MainComponent2 from '../components/my-to-fo-list/mainComponent.vue'



const routes = [
  { path: '/excursion', component: MainComponent },
  { path: '/excursion/excursions/:id', component: ExcursionPage, name: 'excursion' },

  { path: '/test', component: TestComponent },

  { path: '/Cats', component: HomeView},
  { path: '/Cats/Fact', component: FactView},
  { path: '/Cats/Image', component: ImageView},

  { path: '/My-To-Do-List', component: MainComponent2},


]

const router = createRouter({
    history: createWebHistory(),
    routes
  });

export default router