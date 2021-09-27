<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Banks</h1>
        <hr><br><br>
        <br><br>
        <router-link to='/'>
        <button class="btn btn-success btn-sm">Mortgage Calculator</button>
        </router-link>
        <div v-if="is_edit==false" class="addGroup">
          <input v-model="addBankForm.bank_name" placeholder="Bank name" class='input-field'>
          <input v-model="addBankForm.interest_rate" placeholder="Interest rate" class='input-field'>
          <input v-model="addBankForm.maximum_loan" placeholder="Maximum loan" class='input-field'>
          <input v-model="addBankForm.minimum_down_payment" placeholder="Down payment" class='input-field'>
          <input v-model="addBankForm.loan_term" placeholder="Loan term" class='input-field'>
          <button @click="onSubmit">Submit</button>
        </div>
        <div v-else-if="is_edit==true" class="editGroup">
          <input v-model="editForm.bank_name" placeholder="Bank name" class='input-field'>
          <input v-model="editForm.interest_rate" placeholder="Interest rate" class='input-field'>
          <input v-model="editForm.maximum_loan" placeholder="Maximum loan" class='input-field'>
          <input v-model="editForm.minimum_down_payment" placeholder="Down payment" class='input-field'>
          <input v-model="editForm.loan_term" placeholder="Loan term" class='input-field'>
          <button @click="onSubmitUpdate">Submit</button>
        </div>

        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Bank Name</th>
              <th scope="col">Interest rate</th>
              <th scope="col">Maximum loan</th>
              <th scope="col">Minimum down payment</th>
              <th scope="col">Loan term</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(bank, index) in banks" :key="index">
              <td>{{ bank.bank_name }}</td>
              <td>{{ bank.interest_rate }}</td>
              <td>{{ bank.maximum_loan }}</td>
              <td>{{ bank.minimum_down_payment }}</td>
              <td>{{ bank.loan_term }}</td>
              <div class="btn-group">
                <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          @click="editBank(bank)">
                      Edit
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteBank(bank)">
                      Delete
                  </button>
                  </div>
            </tr>
          </tbody>
        </table>
        
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import "bootstrap"
import "bootstrap/dist/css/bootstrap.min.css"

export default {
  name: 'ManageBanks',
  data() {
    return {
      is_edit: false,
      banks: [],
      addBankForm: {
        bank_name: '',
        interest_rate: '',
        maximum_loan: '',
        minimum_down_payment: '',
        loan_term: '',
      },
      editForm: {
        id: '',
        bank_name: '',
        interest_rate: '',
        maximum_loan: '',
        minimum_down_payment: '',
        loan_term: '',
      },
    };
  },
  methods: {
      getBanks() {
        const path = 'http://localhost:5000/banks';
        axios.get(path)
          .then((res) => {
            this.banks = res.data.banks;
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      },
      addBank(payload) {
        const path = 'http://localhost:5000/banks';
        axios.post(path, payload)
          .then(() => {
            this.getBanks();
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error);
            this.getBanks();
          });
      },
      initForm() {
        this.addBankForm.bank_name = '';
        this.addBankForm.interest_rate = '';
        this.addBankForm.maximum_loan = '';
        this.addBankForm.minimum_down_payment = '';
        this.addBankForm.loan_term = '';

        this.editForm.id = '';
        this.editForm.bank_name = '';
        this.editForm.interest_rate = '';
        this.editForm.maximum_loan = '';
        this.editForm.minimum_down_payment = '';
        this.editForm.loan_term = '';
      },
      onSubmit(evt) {
        evt.preventDefault();
        const payload = {
          bank_name: this.addBankForm.bank_name,
          interest_rate: this.addBankForm.interest_rate,
          maximum_loan: this.addBankForm.maximum_loan,
          minimum_down_payment: this.addBankForm.minimum_down_payment,
          loan_term: this.addBankForm.loan_term
        };
        this.addBank(payload);
        this.initForm();
      },
      onReset(evt) {
        evt.preventDefault();
        this.initForm();
      },
      editBank(bank) {
        this.editForm = bank;
        this.is_edit = true
      },
      onSubmitUpdate(evt) {
        evt.preventDefault();
        const payload = {
          bank_name: this.editForm.bank_name,
          interest_rate: this.editForm.interest_rate,
          maximum_loan: this.editForm.maximum_loan,
          minimum_down_payment: this.editForm.minimum_down_payment,
          loan_term: this.editForm.loan_term
        };
        this.updateBank(payload, this.editForm.id);
      },
      updateBank(payload, bankID) {
        const path = `http://localhost:5000/banks/${bankID}`;
        axios.put(path, payload)
          .then(() => {
            this.getBanks();
            this.is_edit = false;
          })
          .catch((error) => {
            console.error(error);
            this.getBanks();
          });
      },
      onResetUpdate(evt) {
        evt.preventDefault();
        this.initForm();
        this.getBanks(); // why?
      },
      removeBank(bankID) {
        const path = `http://localhost:5000/banks/${bankID}`;
        axios.delete(path)
          .then(() => {
            this.getBanks();       })
          .catch((error) => {
            console.error(error);
            this.getBanks();
          });
      },
      onDeleteBank(bank) {
        this.removeBank(bank.id);
      },
    },
    created() {
      this.getBanks();
    },
  };

</script>

<style>
.table {
  margin: 0 auto;
  width: 100%;
  border: collapse;
}
.col-sm-10 {
  width: 100%;
}
</style>
