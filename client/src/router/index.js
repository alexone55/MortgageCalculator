
import { createWebHistory, createRouter } from "vue-router";
import MortgageCalculator from '../components/MortgageCalculator.vue';
import ManageBanks from '../components/ManageBanks.vue';


const routes = [
  {
    path: '/',
    name: 'MortgageCalculator',
    component: MortgageCalculator,
  },
  {
      path: '/ManageBanks',
      name: 'ManageBanks',
      component: ManageBanks,
    },
];
const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;