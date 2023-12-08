<template>
  <MDBNavbar class="navbar-container" container>
    <router-link to="/" style="font-size: x-large; color:black;padding-left:50px">
      J M A C
    </router-link>
  </MDBNavbar>

<section class="vh-100">
  <aside class="container py-5 h-100">
    <aside class="row d-flex justify-content-center align-items-center h-100">
      <h2 class="fw-bold mb-2 text-uppercase">Patient Information Ticket</h2>
      <hr class="solid">
        <div class="print-area">
          <p>{{ PatientInfo.name }}</p>
          <p>wswswsws</p>
        </div>
        <div class="col-12 col-md-8 col-lg-6 col-xl-12">
            <button id="print" @click="printPage" class="btn form-floating btn-lg px-5" type="button">Print</button>
        </div>
      <aside class="float-container">
        <div class="float-child">
        <div class="col-12 col-md-8 col-lg-6 col-xl-12">
            <button @click="goToVisualization" class="btn form-floating btn-lg px-5" type="navigate">View Visualization Report</button>
        </div>
        </div>
        <div class="col-12 col-md-8 col-lg-6 col-xl-12">
        <div class="float-child">
            <button @click="startOver" class="btn form-floating btn-lg px-5" type="navigate">+ New Patient</button>
        </div>
        </div>
      </aside>
    </aside>
  </aside>
</section> 
</template>

<script>
  //import { ref, onMounted } from "vue";
  import { MDBNavbar } from 'mdb-vue-ui-kit';
  //import { useRouter } from 'vue-router';

  export default {
    components: {
      MDBNavbar
    },
    data() {
      return {
        PatientInfo: {
          name: '',
          number: ''
        }
      }
    },
    methods: {
      startOver() {
        this.$router.push("/");
        },
      printPage() {
        window.print();
        },
      goToVisualization() {
        this.$router.push("/VisualizationReport")
        }
      },
      mounted() {
          this.PatientInfo = JSON.parse(localStorage.getItem('PatientInfo'))
        }
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
    padding: 20px;
}  
.navbar-container {
  height: 15vh;
  background: linear-gradient(to bottom, #8a8a8a,#b8b8b8,#d3d3d3,#ececec,#ffffff);
  font-weight:bolder;
  font-family:system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  box-shadow: none;
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
@media print{
  body * {
    display:none;
  }
  .print-area, .print-area * {
    display:block;
  }
}
</style>