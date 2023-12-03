<template>
  <MDBNavbar class="navbar-container" container>
    <router-link to="/" style="font-size: x-large; color:black;padding-left:50px">
      J M A C
    </router-link>
  </MDBNavbar>

  <section class="vh-100 gradient-custom">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <h2 class="fw-bold mb-2 text-uppercase">Preliminary Information</h2>
      <hr class="solid">
      <h5 class="fw-regular mb-2">Enter the required information.</h5>
      <div class="float-container">
        <div class="float-child">
        <div class="col-12 col-md-8 col-lg-6 col-xl-12">
                <div class="form-floating mb-3">
                  <input type="age" class="form-control" id="ageFloatingInput" placeholder="e.g. 29" v-model="age">
                  <label for="floatingInput">Age</label>
                </div>
                <div class="form-floating mb-3">
                  <input type="gender" class="form-control" id="genderFloatingInput" placeholder="Male or Female" v-model="gender">
                  <label for="floatingInput">Sex (M or F)</label>
                </div>
                <div class="form-floating mb-3">
                  <input type="trestbps" class="form-control" id="trestbpsFloatingInput" placeholder="e.g. 145" v-model="trestbps">
                  <label for="floatingInput">Resting Heart Rate in mm Hg</label>
                </div>
        </div>        
        </div>
        <div class="float-child">
        <div class="col-12 col-md-8 col-lg-6 col-xl-12">
                <div class="form-floating mb-3">
                  <input type="has_history" class="form-control" id="histFfloatingInput" placeholder="Yes or No" v-model="has_history">
                  <label for="floatingInput">Has History of Heart Attack (Yes or No)</label>
                </div>
                <div class="form-floating mb-3">
                  <input type="cp" class="form-control" id="cpFloatingInput" placeholder="e.g. 2" v-model="cp">
                  <label for="floatingInput">Chest Pain Type</label>
                </div>
                <button @click="handleSubmit" class="btn btn-lg px-5" type="submit">Next</button>
        </div>
      </div>
      </div>
    </div>
    <div class="modal" v-if="data">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Modal title</h5>
            <button type="button" class="btn-close" @click="closeModal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p>Logreg: {{ data['logreg_predictions'] }}</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary" @click="Above35">Save changes</button>
          </div>
        </div>
      </div>
      </div>
    </div>
</section> 
</template>
<script>
import { MDBNavbar } from 'mdb-vue-ui-kit';
import axios from 'axios';

export default {
  name: 'OutputModal',
  props: {
    visible: Boolean,
    data: Object
  },
  components: {
    MDBNavbar
  },
  data() {
    return {
      modalVisible: false,
      responseData: null,
      age: '',
      gender: '',
      trestbps: '',
      has_history: '',
      cp: ''
    };
  },
  methods: {
    Above35() {
      this.$router.push("/AdditionalInfo1");
    },
      closeModal() {
        this.$emit('update:visible',false);
      },
      openModal() {
        this.modalVisible = true;
      },
    async handleSubmit() {
      try {
        this.modalVisible = true;
        const url = 'http://127.0.0.1:5000/Preliminary';
        const response = await axios.post(url, {
          age: this.age,
          gender: this.gender,
          trestbps: this.trestbps,
          has_history: this.has_history,
          cp: this.cp,
        });

        if (response.status === 200) {
          console.log('Request successful', response.data)
          this.responseData = response.data;
        } else {
          console.error('Request failed:', response.data);
          alert('Request failed:' + response.data.message);
        }
      } catch (error) {
        console.error('Request failed:', error.message);
      }
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
</style>