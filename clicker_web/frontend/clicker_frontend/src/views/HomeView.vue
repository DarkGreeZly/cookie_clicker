<template>
  <nav class="py-3 px-8 border-b border-200">
    <div class="max-w-5xl mx-auto">
          <div class="flex items-center justify-between">
              <div class="menu-left">
                  <p class="text-s font-bold">{{ this.user_name }}</p>
              </div>
                <button class="py-4 px-6 bg-emerald-600 text-white rounded-lg hover:bg-emerald-500">
                  Save
                </button>
                <button class="py-4 px-6 bg-emerald-600 text-white rounded-lg hover:bg-emerald-500">
                  Load
                </button>
              <div class="menu-right">
                <p class="text-s font-bold">0.00</p>
              </div>
          </div>
      </div>
  </nav>
  <main>
    <form v-on:submit.prevent="submitForm">
      <button class="px-8 md-">
        <img class="object-scale-down max-h-full drop-shadow-md rounded-md m-auto" src='../assets/cookie.png'/>
      </button>
    </form>
  </main>
</template>
<script>
import axios from 'axios'


export default {
  name: 'HomeView',

  data() {
    return {
      user_name: '',
      score: '',
      access_token: ''
    }
  },
  mounted() {
    this.get_user_name()
  },

  methods: {
    async get_user_name() {
      this.access_token = localStorage.getItem('token');
      axios
          .get('/user/me/', {
                headers: {
                'Authorization': `Bearer ${this.access_token}`
                }})
          .then(response => {
            console.log('data', response.data)
            this.user_name = response.data.username;
          })
          .catch(error => {
            console.log('error', error)
            })
    }
  }

}
</script>