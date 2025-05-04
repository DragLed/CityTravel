<template>
    <div class="p-4 max-w-md mx-auto">
      <h1 class="text-2xl font-bold mb-4">Погода по городу</h1>
  
      <input
        v-model="city"
        @keyup.enter="getWeather"
        class="border rounded p-2 w-full mb-4"
        placeholder="Введите город (на русском)"
      />
  
      <button
        @click="getWeather"
        class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      >
        Узнать погоду
      </button>
  
      <div v-if="c" class="mt-6">
        <h2 class="text-xl font-semibold">{{ weather.name }}</h2>
        <div class="flex items-center gap-4 mt-2">
          <img
            :src="`https://openweathermap.org/img/wn/${weather.weather[0].icon}@2x.png`"
            :alt="weather.weather[0].description"
          />
          <div>
            <p class="text-lg capitalize">{{ weather.weather[0].description }}</p>
            <p class="text-xl font-bold">{{ Math.round(weather.main.temp) }}°C</p>
          </div>
        </div>
      </div>
  
      
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  
  // 🔐 ВСТАВЬ СЮДА СВОЙ КЛЮЧ
  const API_KEY = '14cc090ee66620b128659eaa01ba47e4'
  
  const city = ref('')
  const weather = ref(null)
  const error = ref('')
  
  
  </script>
  
  <style scoped>
  body {
    font-family: sans-serif;
  }
  </style>
  