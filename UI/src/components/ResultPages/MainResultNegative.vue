<template>
  <MDBNavbar class="navbar-container" container>
    <router-link to="/" style="font-size: x-large; color:black;padding-left:50px">
      J M A C
    </router-link>
  </MDBNavbar>

  <section class="vh-100 gradient-custom">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <h2 class="fw-bold mb-0 text-uppercase">Readings</h2>
      <hr class="solid">
        <div class="col-12 col-md-8 col-lg-6 col-xl-12">
                <div class="form-floating mb-3">
                  <p class="fw-regular mb-3 text-uppercase">Findings</p>
                  <h4 class="fw-bold mb-5">The patient has a LOW chance of having a CVD.</h4>
                  <p class="fw-regular mb-3 text-uppercase">Recommendations</p>
                  <h4 class="fw-bold mb-5">Admit the patient to the emergency room for further investigation of symptoms.</h4>
                </div>
        </div>
      <div class="float-container">
        <div class="float-child">
        <div class="col-12 col-md-8 col-lg-6 col-xl-12">
            <button @click="goToVisualization" class="btn form-floating btn-lg px-5" type="navigate">View Visualization Report</button>
        </div>
        </div>
        <div class="col-12 col-md-8 col-lg-6 col-xl-12">
        <div class="float-child">
            <button @click="goToTicketPage" class="btn form-floating btn-lg px-5" type="navigate">View Detailed Report</button>
        </div>
      </div>
      </div>
    </div>
  </div>
</section> 
</template>
<script>
//import { ref } from "vue";
import { MDBNavbar } from 'mdb-vue-ui-kit';

export default {
  components: {
    MDBNavbar
  },
  methods: {
    goToVisualization() {
      this.$router.push("/VisualizationReport");
    },
    goToTicketPage() {
      this.$router.push("/PrintableTicket");
    }
  },
};
</script>


<style scoped>
.vh-100 {
  height: 80vh !important;
}
.float-container {
    padding: 20px;
}
.float-child {
    width: 50%;
    float: left;
    padding: 10px;
    margin-right: 0%;
}  
.navbar-container {
  height: 15vh;
  background: linear-gradient(to bottom, #8a8a8a,#b8b8b8,#d3d3d3,#ececec,#ffffff);
  font-weight:bolder;
  font-family:system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  box-shadow: none;
}
.gradient-custom {
  background: color(srgb rgb(255, 255, 255) rgb(255, 255, 255) rgb(255, 255, 255))
}
.btn {
  border-radius: 50px;
  background-color: #ffca7b;
  font-weight: bolder;
  margin-top: .5rem;
}
hr.solid {
  border-top: 3px solid #000000;
}
</style>