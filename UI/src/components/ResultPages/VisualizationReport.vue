<template>
  <MDBNavbar class="navbar-container" container>
    <router-link to="/" style="font-size: x-large; color:black;padding-left:50px">
      J M A C
    </router-link>
  </MDBNavbar>

<section class="vh-100 gradient-custom">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <h2 class="fw-bold mb-2 text-uppercase">Visualization Report</h2>
      <hr class="solid">
      <div v-for="(url, index) in imageUrls" :key="index" class="crop">
        <img :src="url" alt="Image" class="img-fluid img-thumbnail rounded mx-auto d-block"/>
      </div>
      <div class="float-container">
        <div class="float-child">
          <div class="col-12 col-md-8 col-lg-6 col-xl-12">
            <button @click="goToTicket" class="btn form-floating btn-lg px-5" type="navigate">View Detailed Report</button>
          </div>
        </div>
        <div class="col-12 col-md-8 col-lg-6 col-xl-12">
          <div class="float-child">
              <button @click="startOver" class="btn form-floating btn-lg px-5" type="navigate">+ New Patient</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</section> 
</template>
<script>
  //import { ref, onMounted } from "vue";
  import axios from 'axios'
  import { MDBNavbar } from 'mdb-vue-ui-kit';
  //import { useRouter } from 'vue-router';

  export default {
    components: {
      MDBNavbar
    },
    data() {
      return {
        imageUrls: []
      }
    },
    methods: {
    startOver() {
      this.$router.push("/");
      localStorage.clear();
    },
    goToTicket() {
      this.$router.push("/PrintableTicket")
    }
  },
  mounted() {
    try {
    axios.get('http://127.0.0.1:5000/getImages')
      .then(response => {
        this.imageUrls = response.data.image_urls;
      })
      .catch(error => {
        console.error(error);
      });
  } catch (error) {
    console.error(error);
  }
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
.crop img {
  flex-shrink: 0;
  min-width: 100%;
  min-height: 100%;
}
</style>