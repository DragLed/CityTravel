<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { onMounted } from 'vue';

const excursionList = ref([]);
const filteredExcursionList = ref([]);
const searchRequest = ref('');
const HistoryList = ref([]);
const router = useRouter();

function Search() {
  filteredExcursionList.value = [];
  excursionList.value = [];
  axios.get('/detailed_tours_20 (2).json')
    .then(function (response) {
      excursionList.value = response.data;

      if (searchRequest.value == 'TEST') {
        filteredExcursionList.value = excursionList.value;
      } else if (searchRequest.value) {
        const filteredExcursions = excursionList.value.filter(function (excursion) {
          return excursion.title.toLowerCase().includes(searchRequest.value.toLowerCase());
        });
        filteredExcursionList.value = filteredExcursions;
      } else {
        console.log('Поиск не выполнен, так как строка поиска пуста.');
        for (let i = 0; i < 6; i++) {
          let a = Math.floor(Math.random() * excursionList.value.length);
          filteredExcursionList.value.push(excursionList.value[a]);
        }
      }
    })
    .catch(function (error) {
      console.error('Ошибка при загрузке данных:', error);
    });
}

function GetHistory() {
  const history = JSON.parse(localStorage.getItem('tourHistory')) || [];
  HistoryList.value = history;
  console.log("История туров:", HistoryList.value);
}

function GoToTour(id) {
  GetHistory();
  router.push({ name: 'excursion', params: { id: id } });
}

function deleteHistory(id) {
  let tourHistory = JSON.parse(localStorage.getItem('tourHistory')) || [];
  tourHistory = tourHistory.filter(tour => tour.id !== id);
  localStorage.setItem('tourHistory', JSON.stringify(tourHistory));
  console.log(`Тур с ID "${id}" удалён из истории`);
  GetHistory();
}

onMounted(() => {
  Search();
  GetHistory();
});

</script>


<template>
  <div class="home-page">
    <div class="search-bar-container">
      <input @input="Search" v-model="searchRequest" type="text" value="" placeholder="Поиск городов, экскурсий...">
      <button @click="Search">Поиск</button>
    </div>
    <div class="excursion-results-section">
      <div class="excursion-list" @click="GoToTour(excursion.id)" v-if="filteredExcursionList"
        v-for="excursion in filteredExcursionList" :key="excursion.id">
        <!-- <img :src="excursion.image" alt="Динамическое изображение"> -->
        <h3>{{ excursion.title }}</h3>
        <span>{{ excursion.description }}</span>
        <span>Дата: {{ excursion.date }}</span>
        <span>Стоимость билета: {{ excursion.price }}₽</span>
        <span>Начало у {{ excursion.departure }}</span>
      </div>
      <div v-else>По запросу {{ searchRequest }} не найдено не одной экскурсии</div>
    </div>
    <div class="history">
  <h4>История посещений</h4>
  <div class="history-container">
    <div v-if="HistoryList.length > 0">
      <div class="historyblock" v-for="History in HistoryList" :key="History.id">
        <div class="history-info">
          <div class="history-name">{{ History.name }}</div>
          <div class="history-id">ID: {{ History.id }} • {{ History.date }}</div>
        </div>
        <div class="history-actions">
          <button class="history-btn history-btn-view" @click="GoToTour(History.id)">Открыть</button>
          <button class="history-btn history-btn-delete" @click="deleteHistory(History.id)">Удалить</button>
        </div>
      </div>
    </div>
    <div v-else class="empty-history">
      Вы пока не посещали экскурсий
    </div>
  </div>
</div>
  </div>
</template>


<style scoped>
.home-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  color: #e0e0e0;
  font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

.search-bar-container {
  display: flex;
  margin-bottom: 30px;
  position: relative;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

.search-bar-container input {
  flex: 1;
  padding: 12px 20px;
  background-color: #1f1f1f;
  border: 1px solid #333;
  border-right: none;
  color: #e0e0e0;
  border-radius: 30px 0 0 30px;
  font-size: 16px;
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.search-bar-container input:focus {
  outline: none;
  border-color: #9b00ff;
  box-shadow: 0 0 0 2px rgba(155, 0, 255, 0.2);
}

.search-bar-container button {
  padding: 12px 25px;
  background: linear-gradient(135deg, #9b00ff 0%, #6a00ff 100%);
  color: #fff;
  border: none;
  border-radius: 0 30px 30px 0;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.search-bar-container button:hover {
  background: linear-gradient(135deg, #8a00e6 0%, #5a00e6 100%);
  transform: translateY(-1px);
}

.excursion-results-section {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 25px;
  margin-bottom: 40px;
}

.excursion-list {
  background: linear-gradient(145deg, #1f1f1f 0%, #252525 100%);
  border: 1px solid #333;
  border-radius: 12px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  position: relative;
  overflow: hidden;
}

.excursion-list::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(155, 0, 255, 0.1) 0%, transparent 100%);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.excursion-list:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  border-color: #9b00ff;
}

.excursion-list:hover::before {
  opacity: 1;
}

.excursion-list h3 {
  margin: 0 0 15px;
  font-size: 18px;
  color: #ffffff;
  font-weight: 600;
  position: relative;
  z-index: 1;
}

.excursion-list span {
  margin: 0 0 12px;
  color: #b0b0b0;
  font-size: 14px;
  position: relative;
  z-index: 1;
}

.history {
  background: #1e1e1e;
  border-radius: 12px;
  padding: 25px;
  margin-top: 40px;
  border: 1px solid #2e2e2e;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}

.history h4 {
  margin: 0 0 20px;
  font-size: 18px;
  color: #9b00ff;
  font-weight: 600;
  display: flex;
  align-items: center;
}

.history h4::before {
  content: "🕒";
  margin-right: 10px;
  font-size: 20px;
}

.history-container {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.historyblock {
  background: rgba(40, 40, 40, 0.6);
  border-radius: 8px;
  padding: 15px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  transition: all 0.25s ease;
  border-left: 3px solid transparent;
}

.historyblock:hover {
  background: rgba(50, 50, 50, 0.8);
  border-left: 3px solid #9b00ff;
  transform: translateX(5px);
}

.history-info {
  flex: 1;
}

.history-name {
  font-weight: 500;
  color: #f0f0f0;
  margin-bottom: 5px;
  display: flex;
  align-items: center;
}

.history-name::before {
  content: "📍";
  margin-right: 8px;
  opacity: 0.7;
}

.history-id {
  font-size: 12px;
  color: #888;
  font-family: monospace;
}

.history-actions {
  display: flex;
  gap: 10px;
}

.history-btn {
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
}

.history-btn-view {
  background: rgba(155, 0, 255, 0.15);
  color: #bb86fc;
}

.history-btn-view:hover {
  background: rgba(155, 0, 255, 0.25);
}

.history-btn-delete {
  background: rgba(255, 75, 75, 0.15);
  color: #ff6b6b;
}

.history-btn-delete:hover {
  background: rgba(255, 75, 75, 0.25);
}

.empty-history {
  text-align: center;
  padding: 30px;
  color: #666;
  font-style: italic;
  background: rgba(30, 30, 30, 0.5);
  border-radius: 8px;
  margin-top: 15px;
}

.empty-history::before {
  content: "😕";
  font-size: 24px;
  display: block;
  margin-bottom: 10px;
}

/* Анимация появления элементов */
@keyframes historyItemAppear {
  from {
    opacity: 0;
    transform: translateX(-10px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.historyblock {
  animation: historyItemAppear 0.3s ease-out forwards;
}

/* Адаптивность */
@media (max-width: 600px) {
  .historyblock {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }
  
  .history-actions {
    align-self: flex-end;
  }
  
  .history-btn {
    padding: 5px 10px;
  }
}
</style>