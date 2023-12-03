// router.js
import { createRouter, createWebHistory } from 'vue-router';
import PreliminaryPage from './components/PreliminaryPage.vue';
import Above35InputsPage from './components/Above35InputsPage.vue';

const routes = [
  { path: '/', component: PreliminaryPage },
  { path: '/above35inputs', component: Above35InputsPage }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
