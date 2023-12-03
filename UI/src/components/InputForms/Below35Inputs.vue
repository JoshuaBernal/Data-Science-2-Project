<template>
  <div>
    <MDBNavbar class="navbar-container" container>
      <router-link to="/" style="font-size: x-large; color:black;padding-left:50px">
        J M A C
      </router-link>
    </MDBNavbar>

    <section class="vh-100 gradient-custom">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <h2 class="fw-bold mb-2 text-uppercase">Probability Test for CVD</h2>
      <hr class="solid">
      <h5 class="fw-regular mb-2">Based on the patient's preliminary information, please enter the required additional information.</h5>
        <div class="col-12 col-md-8 col-lg-6 col-xl-7">
                <div class="form-floating mb-3">
                  <input type="chol" class="form-control" id="cholFloatingInput" placeholder="e.g. 21" v-model="chol">
                  <label for="floatingInput">Cholesterol Level in mg/dl</label>
                </div>
                <div class="form-floating mb-3">
                  <input type="fbs" class="form-control" id="fbsFloatingInput" placeholder="Male or Female" v-model="fbs">
                  <label for="floatingInput">Fasting Blood Sugar in mg/dl</label>
                </div>
                <div class="form-floating mb-3">
                  <input type="restcg" class="form-control" id="restecgFloatingInput" placeholder="e.g. 145" v-model="restecg">
                  <label for="floatingInput">Resting Electrocardiographic Results</label>
                </div>
        </div>
      <div>
                <button @click="handleSubmit" class="btn btn-lg px-5" type="submit">Submit</button>
      </div>
    </div>
  </div>
</section> 
  </div>
</template>
<script>
  import { ref, onMounted } from "vue";
  import { MDBNavbar } from 'mdb-vue-ui-kit';
  import { useRouter } from 'vue-router';

  export default {
    components: {
      MDBNavbar
    },
    setup() {
      const email = ref('');
      const password = ref('');
      const checkbox2 = ref(false);
      const router = useRouter();

      onMounted(() => {
        const rememberMePreference = localStorage.getItem('rememberMe');

        if (rememberMePreference === 'true') {
          checkbox2.value = true;
        }
      });

      const handleSubmit = async () => {
        try {
          const url = 'http://localhost:8081/auth/login'; // Update the API endpoint here
          const response = await fetch(url, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              email: email.value,
              password: password.value,
            }),
          });
          const data = await response.json();
          if (response.ok) {
            console.log('Login successful:', data);
            document.cookie = `token=${data.token}; expires=${new Date(data.expiresIn)}`;
      
            // Redirect to appropriate component based on role
            if (data.role === 'seniorCitizen') {
              router.push({ name: 'SeniorDashboard'});
            } else if (data.role === 'guardian') {
              router.push({ name: 'GuardianDashboard' });
            } else if (data.role === 'admin') {
              router.push({ name: 'OfficeDashboard' });
            }
          } else {
            console.error('Login failed:', data);
            alert('Login failed:' + data.message);
          }
        } catch (error) {
          console.error('Login failed:', error.message);
        }
      };

      return {
        handleSubmit
      };
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
    align-items: center;
    padding: 2px;
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