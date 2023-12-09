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
          <h5 class="fw-bold">Patient Information</h5>
          <p class="ticketInfo">Patient No: {{ PatientInfo.number }}</p>
          <p class="ticketInfo">Patient Name: {{ PatientInfo.name }}</p>
          <p class="ticketInfo">Age: {{ PrelimInfo.age }}</p>
          <br>
          <h5 class="fw-bold">Test Results</h5>
          <p class="ticketInfo">Prediction Model Used: Support Vector Machine (SVM)</p>
          <p class="ticketInfo" v-if="responseData.final_svm_predictions == '1'">Prediction: HIGH CHANCE of CVD</p>
          <p class="ticketInfo" v-else-if="responseData.final_svm_predictions == '0'">Prediction: Low chance of CVD</p>
          <p class="ticketInfo">Probability of CVD: {{ responseData.final_svm_probability }}%</p>
          <p class="ticketInfo">Accuracy of prediction: {{ responseData.final_svm_accuracy }}%</p>
          <br>
          <h5 class="fw-bold">Recommendations</h5>
          <p class="ticketInfo" v-if="responseData.final_svm_predictions == '1'">Admit the patient for confinement for further specialist checking.</p>
          <p class="ticketInfo" v-if="responseData.final_svm_predictions == '0'">Admit the patient to the emergency room for further investigation of symptoms.</p>
        </div>
        <div class="col-12 col-md-8 col-lg-6 col-xl-12">
          <button id="print" @click="printPage" class="btn form-floating btn-lg px-5" type="button">Print Ticket</button>
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
import { MDBNavbar } from 'mdb-vue-ui-kit';

export default {
  components: {
    MDBNavbar,
  },
  data() {
    return {
      PatientInfo: {
        name: '',
        number: '',
      },
      PrelimInfo: {
        age: '',
        gender: '',
        trestbps: '',
        has_history: '',
        cp: ''
      },
      responseData: {
        final_svm_predictions: '',
        final_svm_probability: '',
        final_svm_accuracy: ''
      }
      };
  },
  methods: {
    startOver() {
      this.$router.push('/');
      localStorage.clear()
    },
    printPage() {
      // Create a new window for printing
      const printWindow = window.open('', '_blank');

      // Copy styles from the original document to the new window
      this.copyStylesToWindow(printWindow);

      // Clone the content you want to print
      const printContent = document.querySelector('.print-area').cloneNode(true);

      // Append the cloned content to the new window
      printWindow.document.body.appendChild(printContent);

      // Close the new window after printing
      printWindow.onafterprint = function () {
        printWindow.close();
      };

      // Trigger the print in the new window
      printWindow.print();
    },
    copyStylesToWindow(printWindow) {
      Array.from(document.styleSheets).forEach(sheet => {
        try {
          const rules = sheet.cssRules || sheet.rules;
          if (rules) {
            const styleEl = document.createElement('style');
            styleEl.textContent = Array.from(rules).map(rule => rule.cssText).join('');
            printWindow.document.head.appendChild(styleEl);
          }
        } catch (error) {
          console.error('Error copying styles:', error);
        }
      });
    },
    goToVisualization() {
      this.$router.push('/VisualizationReport');
    },
  },
  mounted() {
    this.PatientInfo = JSON.parse(localStorage.getItem('PatientInfo'));
    this.PrelimInfo = JSON.parse(localStorage.getItem('PrelimInfo'));
    this.responseData = JSON.parse(localStorage.getItem('responseData'));
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
  background: linear-gradient(to bottom, #8a8a8a, #b8b8b8, #d3d3d3, #ececec, #ffffff);
  font-weight: bolder;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  box-shadow: none;
}
.ticketInfo {
  padding-top: 0px;
  font-family:Arial, Helvetica, sans-serif;
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
@media print {
  body * {
    display: none;
  }
  .print-area, .print-area * {
    display: block;
  }
}
</style>
