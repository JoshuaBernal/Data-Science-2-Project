import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.js";
import 'mdb-vue-ui-kit/css/mdb.min.css';
import 'bootstrap-icons/font/bootstrap-icons.css';

import PreliminaryInputs from './components/InputForms/PreliminaryInputs.vue'
import Above35Inputs from './components/InputForms/Above35Inputs'
import Below35Inputs from './components/InputForms/Below35Inputs'
import LandingPage from './components/LandingPage/LandingPage.vue'
import MainResultPositive from './components/ResultPages/MainResultPositive.vue'
import MainResultNegative from './components/ResultPages/MainResultNegative.vue'
import PrintableTicket from './components/ResultPages/PrintableTicket.vue'
import VisualizationReport from './components/ResultPages/VisualizationReport.vue'


const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/Landing',
    name: 'LandingPage', 
    component: LandingPage
    },
    { path: '/MainResult0',
    name: 'MainResultNegative', 
    component: MainResultNegative
    },
    { path: '/MainResult1',
    name: 'MainResultPositive', 
    component: MainResultPositive
    },
    { path: '/VisualizationReport',
    name: 'VisualizationReport', 
    component: VisualizationReport
    },
    { path: '/PrintableTicket',
    name: 'PrintableTicket', 
    component: PrintableTicket
    },
    { path: '/',
    name: 'PreliminaryInputs', 
    component: PreliminaryInputs
    },
    { path: '/AdditionalInfo1',
    name: 'Above35Inputs',
    component: Above35Inputs
    },
    { path: '/AdditionalInfo2',
    name: 'Below35Inputs',
    component: Below35Inputs
    }
  ]
});

const app = createApp(App);
app.use(router);
app.mount('#app');
