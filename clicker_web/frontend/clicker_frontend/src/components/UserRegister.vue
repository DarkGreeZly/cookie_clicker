<template>
    <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-sm">
            <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Register your account</h2>
        </div>

        <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
            <form class="space-y-6" @submit.prevent="register">
                <div>
                    <label for="user_name" class="block text-sm font-medium leading-6 text-gray-900">User name</label>
                    <div class="mt-2">
                    <input id="user_name" name="user_name" type="text" required v-model="user_name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    </div>
                </div>

                <div>
                    <div class="flex items-center justify-between">
                    <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
                    </div>
                    <div class="mt-2">
                    <input id="password" name="password" type="password" required v-model="password" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    </div>
                </div>

                <div>
                    <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Register</button>
                </div>
            </form>
            <p class="mt-10 text-center text-sm text-gray-500">
              Already have an account?
              <a href="/login" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Log in</a>
            </p>
        </div>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    name: 'UserRegister',
    data() {
      return {
        user_name: '',
        password: '',
        score: 0
      };
    },
    methods: {
      async register() {
        await axios
                  .post('/register', {
                    user_name: this.user_name,
                    password: this.password,
                    score: this.score
                  },
                  {
            headers: {
              'Content-Type': 'application/json'
            }
          })
          .then(response => {
            console.log('response', response)
            this.$router.push('/login');
          })
          .catch(error => {
            console.log('error', error)
          })
      }
    }
  };
</script>