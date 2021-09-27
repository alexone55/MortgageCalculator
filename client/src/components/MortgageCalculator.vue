<template>
  <div class="hello">
    <h1>Mortgage Calculator</h1>
    <input v-model="initialLoan" placeholder="Initial Loan" class='input-field'>
    <input v-model="downPayment" placeholder="Down Payment" class='input-field'>
    <select v-model="selectBank" class='input-field'>
      <option  v-for="bank in banks" :value="bank" :key="bank.id">{{ bank.bank_name }} </option>
    </select>
    <button @click="countOfMonth">Submit</button>
  <div>
    Your monthly pay: {{ monthly }}
  </div>
   <router-link to='/ManageBanks'>
  <button class="banks-button">Manage Banks</button>
  </router-link>
  </div>

</template>

<script>
import axios from 'axios';

export default {
  name: 'MortgageCalculator',
  data () {
    return {
      initialLoan: '',
      downPayment: '',
      selectBank: '',
      banks: [],
      monthly: 0
    }
  },
  methods: {
    getBanks() {
      const path = ' http://localhost:5000/banks'
      axios.get(path)
      .then((res) => {
          this.banks = res.data.banks;
      })
      .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
      })
    },
    countOfMonth: function () {
      console.log(this.selectBank)
      var n = this.selectBank.loan_term * 12
      this.monthly = this.initialLoan * (this.selectBank.interest_rate / 12 * (1 + this.selectBank.interest_rate / 12) ** n) /
      ((1 + this.selectBank.interest_rate / 12) ** n - 1)
    }
  },
  created () {
    this.getBanks();
  },
}
</script>

<style scoped>
.input-field {
  background-color: #3CBC8D;
  color: white;
  border: 1px solid;
  border-radius: 3px;
  padding: 5px;
  margin: 5px
}
.banks-button {
  margin-top: 10px;
  padding: 5px
}
</style>
