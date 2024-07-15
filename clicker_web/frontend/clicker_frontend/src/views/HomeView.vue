<template>
  <main>
    <button class="px-8 md-">
      <img class="object-scale-down max-h-full drop-shadow-md rounded-md m-auto" src='../assets/cookie.png'/>
    </button>
  </main>
</template>

<script>
import axios from 'axios'

const Telegram = window.Telegram.WebApp;

export default {
  name: 'HomeView',

  data() {
    return {
      telegram_id: '',
      user_name: '',
    }
  }

}
</script>