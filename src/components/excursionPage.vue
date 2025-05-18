<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const excursionId = parseInt(route.params.id);
const excursion = ref(null);
const HistoryList = ref([]);
const isLoading = ref(true);
const showAllSights = ref(false);
const weather = ref(null);
const error = ref('');

const API_KEY = '14cc090ee66620b128659eaa01ba47e4';

async function loadExcursionData() {
  isLoading.value = true;
  try {
    const response = await axios.get('/detailed_tours_20 (2).json');
    if (response.data && Array.isArray(response.data)) {
      excursion.value = response.data.find(item => item.id === excursionId) || null;
    }
  } catch (err) {
    console.error('Ошибка при загрузке экскурсии:', err);
  } finally {
    isLoading.value = false;
  }
  if (excursion.value && excursion.value.city) {
    try {
      const weatherResponse = await axios.get(
        `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(
          excursion.value.city
        )}&units=metric&lang=ru&appid=${API_KEY}`
      );
      weather.value = weatherResponse.data;
      error.value = '';
    } catch (err) {
      weather.value = null;
      error.value = 'Город не найден. Проверьте правильность написания.';
    }
  }
}


function GoToTour(name, id, date) {
  const tourHistory = JSON.parse(localStorage.getItem('tourHistory')) || [];
  const existingTour = tourHistory.find(tour => tour.id === id);

  if (!existingTour) {
    tourHistory.push({ name, id, date });
    localStorage.setItem('tourHistory', JSON.stringify(tourHistory));
    showNotification(`Вы записались на "${name}"`, 'success');
  } else {
    showNotification(`Вы уже записаны на "${name}"`, 'info');
  }
  GetHistory();
}

function GetHistory() {
  HistoryList.value = JSON.parse(localStorage.getItem('tourHistory')) || [];
}

function showNotification(message, type = 'success') {
  const notification = document.createElement('div');
  notification.className = `notification ${type}`;
  notification.textContent = message;
  document.body.appendChild(notification);

  setTimeout(() => {
    notification.classList.add('fade-out');
    setTimeout(() => notification.remove(), 500);
  }, 3000);
}

function toggleSights() {
  showAllSights.value = !showAllSights.value;
}

onMounted(() => {
  loadExcursionData();
  GetHistory();
});
</script>


<template>
  <div class="excursion-page">
    <div v-if="isLoading" class="loading-spinner">
      <div class="spinner"></div>
      <p>Загрузка данных экскурсии...</p>
    </div>

    <div v-else-if="!excursion" class="error-message">
      <h2>Экскурсия не найдена</h2>
      <p>К сожалению, запрашиваемая экскурсия не существует или была удалена.</p>
      <router-link to="/" class="back-link">← Вернуться на главную</router-link>
    </div>

    <div v-else class="excursion-container">
      
      <div class="excursion-header">
        <h1>{{ excursion.title }}</h1>
        <div class="excursion-meta">
          <span class="meta-item">📍 {{ excursion.city }}</span>
          <span class="meta-item">📅 {{ excursion.date }}</span>
          <span class="meta-item">⏱️ {{ excursion.time_start }} - {{ excursion.time_end }}</span>
        </div>
      </div>

      <!-- <div class="excursion-gallery">
        <div class="main-image"></div>
        <div class="thumbnails">
          <div class="thumbnail" v-for="i in 3" :key="i"></div>
        </div>
      </div> -->

      <div class="excursion-content">
        <div class="content-section">
          <h2>Описание экскурсии</h2>
          <p class="short-description">{{ excursion.description }}</p>
          <p class="full-description">{{ excursion.full_description }}</p>
        </div>

        <div class="content-grid">
          <div class="info-card">
            <h3>Основная информация</h3>
            <ul class="info-list">
              <li><strong>Дистанция:</strong> {{ excursion.distance_km }} км</li>
              <li><strong>Цена:</strong> {{ excursion.price }} руб.</li>
              <li><strong>Транспорт:</strong> {{ excursion.transport }}</li>
            </ul>
          </div>

          <div class="info-card">
            <h3>Места</h3>
            <ul class="info-list">
              <li><strong>Место сбора:</strong> {{ excursion.arrival }}</li>
              <li><strong>Место отправления:</strong> {{ excursion.departure }}</li>
            </ul>
          </div>

          <div class="info-card">
            <h3>Погода</h3>
            <ul class="info-list" v-if="weather">
              <li>
                <h2 class="text-xl font-semibold">{{ weather.name }}</h2>
              </li>
              <li>
                <div class="flex items-center gap-4 mt-2">
                  <img :src="`https://openweathermap.org/img/wn/${weather.weather[0].icon}@2x.png`"
                    :alt="weather.weather[0].description" />
                  <div>
                    <span class="text-lg capitalize">{{ weather.weather[0].description }}  </span>
                    <span class="text-xl font-bold">+{{ Math.round(weather.main.temp) }}°C</span>
                  </div>
                </div>
              </li>
            </ul>
            <div v-else-if="error" class="text-red-500 mt-4">{{ error }}</div>
            <div v-else class="text-gray-500 mt-4">Загрузка погоды...</div>
          </div>

          <div class="info-card full-width" v-if="excursion.sights && excursion.sights.length">
            <h3>Достопримечательности <button @click="toggleSights" class="toggle-sights">
                {{ showAllSights ? 'Скрыть' : 'Показать все' }}
              </button></h3>
            <ul class="sights-list" :class="{ 'show-all': showAllSights }">
              <li v-for="(sight, index) in excursion.sights" :key="index">
                <span class="sight-number">{{ index + 1 }}.</span> {{ sight }}
              </li>
            </ul>
            <p class="sights-count">Всего объектов: {{ excursion.sights.length }}</p>
          </div>
        </div>

        <div class="action-section">
          <div class="price-tag">
            <span class="price">{{ excursion.price }} руб.</span>
            <span class="per-person">за человека</span>
          </div>
          <button @click="GoToTour(excursion.title, excursion.id, excursion.date)" class="book-button">
            Записаться на экскурсию
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.excursion-page {
  max-width: 1200px;
  margin: 0 auto;

  color: #e0e0e0;
  font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

.loading-spinner {
  text-align: center;
  padding: 50px;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 5px solid rgba(155, 0, 255, 0.2);
  border-radius: 50%;
  border-top-color: #9b00ff;
  animation: spin 1s ease-in-out infinite;
  margin: 0 auto 20px;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.error-message {
  text-align: center;
  padding: 50px;
  color: #ff6b6b;
}

.error-message h2 {
  font-size: 28px;
  margin-bottom: 15px;
}

.back-link {
  display: inline-block;
  margin-top: 20px;
  color: #9b00ff;
  text-decoration: none;
  font-weight: 500;
}

.back-link:hover {
  text-decoration: underline;
}

.excursion-header {
  margin-bottom: 30px;
  text-align: center;
}

.excursion-header h1 {
  font-size: 32px;
  color: #ffffff;
  margin-bottom: 15px;
  position: relative;
  display: inline-block;
}

.excursion-header h1::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 100px;
  height: 3px;
  background: linear-gradient(90deg, #9b00ff, #6a00ff);
  border-radius: 3px;
}

.excursion-meta {
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
}

.meta-item {
  background: rgba(40, 40, 40, 0.7);
  padding: 8px 15px;
  border-radius: 20px;
  font-size: 14px;
  display: flex;
  align-items: center;
  gap: 5px;
}

.excursion-gallery {
  margin-bottom: 30px;
  border-radius: 12px;
  overflow: hidden;
}

.main-image {
  height: 400px;
  background: linear-gradient(135deg, #2d2d2d 0%, #1a1a1a 100%);
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255, 255, 255, 0.1);
  font-size: 72px;
  font-weight: bold;
}

.thumbnails {
  display: flex;
  gap: 10px;
  padding: 10px;
  background: #1e1e1e;
}

.thumbnail {
  width: 80px;
  height: 60px;
  background: #2d2d2d;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.thumbnail:hover {
  transform: scale(1.05);
}

.excursion-content {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.content-section {
  background: #222222;
  padding: 25px;
  border-radius: 12px;
}

.content-section h2 {
  color: #9b00ff;
  margin-top: 0;
  margin-bottom: 20px;
  font-size: 24px;
  position: relative;
  padding-bottom: 10px;
}

.content-section h2::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 50px;
  height: 2px;
  background: #9b00ff;
}

.short-description {
  font-style: italic;
  color: #b0b0b0;
  margin-bottom: 15px;
}

.full-description {
  line-height: 1.7;
}

.content-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.info-card {
  background: #222222;
  padding: 20px;
  border-radius: 12px;
  border-left: 4px solid #9b00ff;
}

.info-card h3 {
  margin-top: 0;
  margin-bottom: 15px;
  color: #ffffff;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.info-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.info-list li {
  margin-bottom: 10px;
  padding-bottom: 10px;
  border-bottom: 1px dashed #333;
}

.info-list li:last-child {
  margin-bottom: 0;
  padding-bottom: 0;
  border-bottom: none;
}

.full-width {
  grid-column: 1 / -1;
}

.sights-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 10px;
  max-height: 200px;
  overflow: hidden;
  transition: max-height 0.5s ease;
}

.sights-list.show-all {
  max-height: 1000px;
}

.sights-list li {
  background: rgba(40, 40, 40, 0.5);
  padding: 10px;
  border-radius: 5px;
  display: flex;
  gap: 5px;
}

.sight-number {
  color: #9b00ff;
  font-weight: bold;
}

.toggle-sights {
  background: none;
  border: none;
  color: #9b00ff;
  cursor: pointer;
  font-size: 14px;
  text-decoration: underline;
}

.sights-count {
  font-style: italic;
  color: #777;
  margin-top: 15px;
}

.action-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: linear-gradient(90deg, #1e1e1e 0%, #222222 100%);
  padding: 20px;
  border-radius: 12px;
  margin-top: 30px;
}

.price-tag {
  text-align: center;
}

.price {
  font-size: 32px;
  font-weight: bold;
  color: #9b00ff;
  display: block;
}

.per-person {
  font-size: 14px;
  color: #aaa;
}

.book-button {
  background: linear-gradient(135deg, #9b00ff 0%, #6a00ff 100%);
  color: white;
  border: none;
  padding: 15px 30px;
  border-radius: 30px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(155, 0, 255, 0.3);
}

.book-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(155, 0, 255, 0.4);
}

.notification {
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 15px 25px;
  border-radius: 8px;
  color: white;
  font-weight: 500;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  z-index: 1000;
  animation: slideIn 0.3s ease-out;
}

.notification.success {
  background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
}

.notification.info {
  background: linear-gradient(135deg, #2196F3 0%, #0D47A1 100%);
}

.notification.error {
  background: linear-gradient(135deg, #F44336 0%, #B71C1C 100%);
}

.fade-out {
  animation: fadeOut 0.5s ease-out forwards;
}

@keyframes slideIn {
  from {
    transform: translateX(100%);
    opacity: 0;
  }

  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes fadeOut {
  from {
    transform: translateX(0);
    opacity: 1;
  }

  to {
    transform: translateX(100%);
    opacity: 0;
  }
}

/* Адаптивность */
@media (max-width: 768px) {
  .excursion-page {
    padding: 15px;
  }

  .excursion-header h1 {
    font-size: 26px;
  }

  .meta-item {
    font-size: 12px;
    padding: 5px 10px;
  }

  .main-image {
    height: 250px;
  }

  .content-grid {
    grid-template-columns: 1fr;
  }

  .action-section {
    flex-direction: column;
    gap: 20px;
  }

  .book-button {
    width: 100%;
  }
}

@media (max-width: 480px) {
  .excursion-header h1 {
    font-size: 22px;
  }

  .excursion-meta {
    flex-direction: column;
    align-items: center;
    gap: 10px;
  }

  .sights-list {
    grid-template-columns: 1fr;
  }
}
</style>