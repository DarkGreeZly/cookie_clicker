<template>
  <nav class="py-3 px-8 border-b border-200">
    <div class="max-w-5xl mx-auto">
          <div class="flex items-center justify-between">
              <div class="menu-left">
                  <p class="text-s font-bold">{{ this.user_name }}</p>
              </div>
                <button class="py-4 px-6 bg-emerald-600 text-white rounded-lg hover:bg-emerald-500" @click="this.save_data()">
                  Save
                </button>
                <button class="py-4 px-6 bg-emerald-600 text-white rounded-lg hover:bg-emerald-500" @click="this.load_data()">
                  Load
                </button>
              <div class="menu-right">
                <p class="text-s font-bold">{{ this.score }}</p>
              </div>
          </div>
      </div>
  </nav>
  <main>
      <button class="px-8 md-" @click="this.cookie_click()">
        <img class="object-scale-down max-h-full drop-shadow-md rounded-md m-auto" src='../assets/cookie.png'/>
      </button>
  </main>
</template>
<script>
import axios from 'axios'


export default {
  name: 'HomeView',

  data() {
    return {
      user_name: '',
      score: 0,
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
    },
    async cookie_click() {
      this.score += 1
    },
    async save_data() {
      axios
          .post('/save', {
              score: this.score,
              username: this.user_name
            }, {
            headers: {
              'Content-Type': 'application/json'
            }
          })
          .then(response => {
            console.log('data', response.data)
            this.score = 0
          })
          .catch(error => {
            console.log('error', error)
          })
    },
    async load_data() {
      axios
          .get('/load', {
                    headers: {
                    'Authorization': `Bearer ${this.access_token}`
                    }})
              .then(response => {
                console.log('data', response.data)
                this.score += response.data;
              })
              .catch(error => {
                console.log('error', error)
                })
    }
  }

}
</script>