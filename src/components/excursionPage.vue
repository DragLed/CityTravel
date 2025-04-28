<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRoute } from 'vue-router';
import { onMounted } from 'vue';

const route = useRoute();
const excursionId = parseInt(route.params.id);
const excursion = ref(null);
const HistoryList = ref([]);

function loadExcursionData() {
  axios.get('/detailed_tours_20 (2).json')
    .then(function (response) {
      if (response.data && Array.isArray(response.data)) {
        if (response.data.length >= excursionId && excursionId > 0) {
          excursion.value = response.data[excursionId - 1];
        } else {
          console.error('Экскурсия с указанным ID не найдена');
        }
      } else {
        console.error('Получены некорректные данные');
      }
    })
    .catch(function (error) {
      console.error('Ошибка при загрузке данных:', error);
    });
}
function GoToTour(name, id, date) {
  let tourHistory = JSON.parse(localStorage.getItem('tourHistory')) || [];
  const existingTour = tourHistory.find(tour => tour.id === id);
  if (!existingTour) {
    tourHistory.push({ name, id, date})
  }
  localStorage.setItem('tourHistory', JSON.stringify(tourHistory));
  console.log("Запись истории в localStorage:", tourHistory);
  GetHistory()
  const isExcursionWithId5Exists = HistoryList.value.some(excursion => excursion.id === id);
  if (isExcursionWithId5Exists) {
    alert("Вы уже записаны на " + name)
} else {
    alert("Вы записались на " + name)
}
  
};

function GetHistory() {
  const history = JSON.parse(localStorage.getItem('tourHistory')) || [];
  HistoryList.value = history;
  console.log("История туров:", HistoryList.value);
}

onMounted(() => {
  loadExcursionData();
  GetHistory()
});
</script>


<template>
  <div class="maincontainer" v-if="excursion">
    <h1>{{ excursion.title }}</h1>

    <div class="excursion-info">
      <div class="info-section">
        <h2>Основная информация</h2>
        <p><strong>Город:</strong> {{ excursion.city }}</p>
        <p><strong>Дата:</strong> {{ excursion.date }}</p>
        <p><strong>Время:</strong> {{ excursion.time_start }} - {{ excursion.time_end }}</p>
        <p><strong>Дистанция:</strong> {{ excursion.distance_km }} км</p>
        <p><strong>Цена:</strong> {{ excursion.price }} руб.</p>
      </div>

      <div class="info-section">
        <h2>Места</h2>
        <p><strong>Место сбора:</strong> {{ excursion.arrival }}</p>
        <p><strong>Место отправления:</strong> {{ excursion.departure }}</p>
      </div>

      <div class="info-section">
        <h2>Описание</h2>
        <p class="short-description">{{ excursion.description }}</p>
        <p class="full-description">{{ excursion.full_description }}</p>
      </div>
      <div class="info-section" v-if="excursion.sights && excursion.sights.length">
        <h2>Достопримечательности</h2>
        <ul class="sights-list">
          <li v-for="(sight, index) in excursion.sights" :key="index">
            {{ sight }}
          </li>
        </ul>
        <p class="sights-count">Всего объектов: {{ excursion.sights.length }}</p>
      </div>

      <div class="info-section">
        <h2>Дополнительно</h2>
        <p><strong>Транспорт:</strong> {{ excursion.transport }}</p>
      </div>
      <div class="info-section-btn">
        <p>Хотите записаться на экскурсию?</p>
        <button @click="GoToTour(excursion.title, excursion.id,  excursion.date)">Записаться</button>
      </div>
    </div>
  </div>
  <div v-else-if="excursion === null" class="loading">
    Загрузка данных экскурсии...
  </div>
  <div v-else class="error">
    Не удалось загрузить данные экскурсии
  </div>
</template>


<style scoped>
.maincontainer {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  animation: fadeIn 0.5s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.excursion-info {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.info-section {
  background: #222222;
  padding: 15px;
  border-radius: 8px;
  border: 2px solid #303030;
  transition: all 0.3s ease;
  transform: translateY(0);
  position: relative;
  overflow: hidden;
}

.info-section::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(52,152,219,0.1) 0%, transparent 100%);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.info-section:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.1);
  border-color: #3498db;
}

.info-section:hover::after {
  opacity: 1;
}

h1 {
  color: #3f6285;
  animation: pulse 2s infinite alternate;
}

@keyframes pulse {
  from {
    text-shadow: 0 0 5px rgba(63, 98, 133, 0.5);
  }
  to {
    text-shadow: 0 0 15px rgba(63, 98, 133, 0.8);
  }
}

h2 {
  color: #3f6285;
  margin-bottom: 10px;
}

.sights-list {
  list-style-type: disc;
  padding-left: 20px;
}

.sights-list li {
  transition: all 0.2s ease;
  padding: 3px 0;
}

.sights-list li:hover {
  color: #3498db;
  padding-left: 5px;
  transform: scale(1.02);
}

.short-description {
  font-style: italic;
  color: #555;
  transition: color 0.3s ease;
}

.short-description:hover {
  color: #ddd;
}

.full-description {
  margin-top: 10px;
  line-height: 1.6;
  transition: all 0.3s ease;
}

.full-description:hover {
  letter-spacing: 0.3px;
}

.loading,
.error {
  text-align: center;
  padding: 50px;
  font-size: 1.2em;
}

.loading {
  color: #3498db;
  animation: blink 1.5s infinite;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.error {
  color: #e74c3c;
}

.info-section-btn {
  background: #222222;
  padding: 15px;
  border-radius: 8px;
  border: 2px solid #303030;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  transition: all 0.3s ease;
}

.info-section-btn:hover {
  border-color: #3498db;
}

.info-section-btn p {
  margin-bottom: 10px;
  transition: color 0.3s ease;
}

.info-section-btn:hover p {
  color: #3498db;
}

.info-section-btn button {
  border-radius: 15px;
  padding: 7px 15px;
  background-color: #3498db;
  border: 2px solid #227ab4;
  color: white;
  cursor: pointer;
  transition: all 0.3s ease;
  transform: scale(1);
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

.info-section-btn button:hover {
  background-color: #2980b9;
  transform: scale(1.05);
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
}

.sights-count {
  font-style: italic;
  color: #777;
  transition: all 0.3s ease;
}

.sights-count:hover {
  color: #3498db;
  transform: scale(1.02);
}

p, li {
  transition: color 0.2s ease;
}

p:hover, li:hover {
  color: #ddd;
}
</style>