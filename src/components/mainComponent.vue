<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { onMounted } from 'vue';

const excursionList = ref([]);
const filteredExcursionList = ref([]);
const searchRequest = ref('');
const HistoryList = ref([]);
const isLoading = ref(false);
const router = useRouter();

async function Search() {
  isLoading.value = true;
  try {
    const response = await axios.get('/detailed_tours_20 (2).json');
    excursionList.value = response.data;

    if (searchRequest.value.toLowerCase() === 'test') {
      filteredExcursionList.value = [...excursionList.value];
    } else if (searchRequest.value) {
      filteredExcursionList.value = excursionList.value.filter(excursion =>
        excursion.title.toLowerCase().includes(searchRequest.value.toLowerCase())
      );
    } else {
      filteredExcursionList.value = [...excursionList.value]
        .sort(() => 0.5 - Math.random())
        .slice(0, 6);
    }
  } catch (error) {
    console.error('Ошибка при загрузке данных:', error);
  } finally {
    isLoading.value = false;
  }
}

function GetHistory() {
  HistoryList.value = JSON.parse(localStorage.getItem('tourHistory')) || [];
}

function GoToTour(id) {
  router.push({ name: 'excursion', params: { id } });
}

function deleteHistory(id) {
  const tourHistory = JSON.parse(localStorage.getItem('tourHistory')) || [];
  const updatedHistory = tourHistory.filter(tour => tour.id !== id);
  localStorage.setItem('tourHistory', JSON.stringify(updatedHistory));
  GetHistory();
}

function clearAllHistory() {
  if (confirm('Вы уверены, что хотите очистить всю историю?')) {
    localStorage.removeItem('tourHistory');
    GetHistory();
  }
}

onMounted(() => {
  Search();
  GetHistory();
});
</script>

<template>
  <div class="home-page">
    <div class="search-bar-container">
      <input 
        v-model="searchRequest" 
        @input="Search"
        @keyup.enter="Search"
        type="text" 
        placeholder="Поиск городов, экскурсий..."
        class="search-input"
      >
      <button @click="Search" class="search-button">
        <span class="button-text">Поиск</span>
        <span class="button-icon">🔍</span>
      </button>
    </div>

    <div v-if="isLoading" class="loading-spinner">
      <div class="spinner"></div>
    </div>

    <div v-else class="excursion-results-section">
      <div 
        v-for="excursion in filteredExcursionList" 
        :key="excursion.id"
        class="excursion-card"
        @click="GoToTour(excursion.id)"
      >
        <div class="card-image-placeholder">
          <span class="image-text">{{ excursion.city.charAt(0) }}</span>
        </div>
        <div class="card-content">
          <h3>{{ excursion.title }}</h3>
          <p class="description">{{ excursion.description }}</p>
          <div class="card-details">
            <span class="detail-item">🗓 {{ excursion.date }}</span>
            <span class="detail-item">💰 {{ excursion.price }}₽</span>
            <span class="detail-item">📍 {{ excursion.departure }}</span>
          </div>
          <div class="card-badge" v-if="excursion.price < 1000">Выгодно!</div>
        </div>
      </div>

      <div v-if="!filteredExcursionList.length" class="no-results">
        <p>По запросу "{{ searchRequest }}" ничего не найдено</p>
        <button @click="searchRequest = ''; Search()" class="reset-button">
          Сбросить поиск
        </button>
      </div>
    </div>

    <div class="history-section">
      <div class="history-header">
        <h4>История посещений</h4>
        <button 
          v-if="HistoryList.length" 
          @click="clearAllHistory"
          class="clear-history-button"
        >
          Очистить всё
        </button>
      </div>
      
      <div v-if="HistoryList.length" class="history-list">
        <div 
          v-for="History in HistoryList" 
          :key="History.id"
          class="history-item"
        >
          <div class="history-info" @click="GoToTour(History.id)">
            <div class="history-name">
              <span class="history-icon">📅</span>
              {{ History.name }}
            </div>
            <div class="history-meta">
              <span class="history-date">{{ History.date }}</span>
              <span class="history-id">ID: {{ History.id }}</span>
            </div>
          </div>
          <button 
            @click.stop="deleteHistory(History.id)"
            class="delete-button"
            title="Удалить из истории"
          >
            🗑️
          </button>
        </div>
      </div>
      
      <div v-else class="empty-history">
        <p>Вы пока не посещали экскурсий</p>
      </div>
    </div>
  </div>
</template>

<style scoped>

.home-page {
  max-width: 1200px;
  margin: 0 auto;
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

.search-input {
  flex: 1;
  padding: 15px 20px;
  background-color: #1f1f1f;
  border: 1px solid #333;
  border-right: none;
  color: #e0e0e0;
  border-radius: 30px 0 0 30px;
  font-size: 16px;
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.search-input:focus {
  outline: none;
  border-color: #9b00ff;
  box-shadow: 0 0 0 2px rgba(155, 0, 255, 0.2);
}

.search-button {
  padding: 0 25px;
  background: linear-gradient(135deg, #9b00ff 0%, #6a00ff 100%);
  color: #fff;
  border: none;
  border-radius: 0 30px 30px 0;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  display: flex;
  align-items: center;
  gap: 8px;
}

.search-button:hover {
  background: linear-gradient(135deg, #8a00e6 0%, #5a00e6 100%);
  transform: translateY(-1px);
}

.button-icon {
  font-size: 18px;
}

/* Карточки экскурсий */
.excursion-results-section {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 25px;
  margin-bottom: 40px;
}

.excursion-card {
  background: linear-gradient(145deg, #1f1f1f 0%, #252525 100%);
  border: 1px solid #333;
  border-radius: 12px;
  padding: 15px;
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  min-height: 300px;
}

.excursion-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  border-color: #9b00ff;
}

.card-image-placeholder {
  background: linear-gradient(135deg, #9b00ff 0%, #6a00ff 100%);
  height: 120px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 15px;
  position: relative;
  overflow: hidden;
}

.image-text {
  font-size: 60px;
  font-weight: bold;
  color: rgba(255, 255, 255, 0.2);
}

.card-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.excursion-card h3 {
  margin: 0 0 10px;
  font-size: 18px;
  color: #ffffff;
  font-weight: 600;
}

.description {
  color: #b0b0b0;
  font-size: 14px;
  margin-bottom: 15px;
  flex: 1;
}

.card-details {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: auto;
}

.detail-item {
  background: rgba(40, 40, 40, 0.7);
  padding: 5px 10px;
  border-radius: 15px;
  font-size: 12px;
  display: flex;
  align-items: center;
  gap: 5px;
}

.card-badge {
  position: absolute;
  top: 15px;
  right: 15px;
  background: #ff5722;
  color: white;
  padding: 3px 10px;
  border-radius: 15px;
  font-size: 12px;
  font-weight: bold;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
}

/* История */
.history-section {
  background: linear-gradient(145deg, #1e1e1e 0%, #222222 100%);
  padding: 25px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  border: 1px solid #333;
}

.history-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.history-header h4 {
  margin: 0;
  font-size: 18px;
  color: #9b00ff;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 10px;
}

.clear-history-button {
  background: rgba(255, 75, 75, 0.2);
  color: #ff6b6b;
  border: none;
  padding: 5px 15px;
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.clear-history-button:hover {
  background: rgba(255, 75, 75, 0.3);
}

.history-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.history-item {
  background: rgba(40, 40, 40, 0.6);
  border-radius: 8px;
  padding: 15px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  transition: all 0.25s ease;
}

.history-item:hover {
  background: rgba(50, 50, 50, 0.8);
  transform: translateX(5px);
}

.history-info {
  flex: 1;
  cursor: pointer;
}

.history-name {
  font-weight: 500;
  color: #f0f0f0;
  margin-bottom: 5px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.history-meta {
  display: flex;
  gap: 15px;
}

.history-date {
  font-size: 12px;
  color: #aaa;
}

.history-id {
  font-size: 12px;
  color: #888;
  font-family: monospace;
}

.delete-button {
  background: none;
  border: none;
  color: #ff6b6b;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.2s ease;
  padding: 5px;
  border-radius: 50%;
}

.delete-button:hover {
  background: rgba(255, 75, 75, 0.2);
  transform: scale(1.2);
}

.empty-history {
  text-align: center;
  padding: 30px;
  color: #666;
  font-style: italic;
}

.empty-history img {
  width: 100px;
  opacity: 0.5;
  margin-bottom: 15px;
}

/* Загрузка */
.loading-spinner {
  display: flex;
  justify-content: center;
  padding: 50px;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 5px solid rgba(155, 0, 255, 0.2);
  border-radius: 50%;
  border-top-color: #9b00ff;
  animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.no-results {
  grid-column: 1 / -1;
  text-align: center;
  padding: 40px;
}

.no-results-image {
  width: 150px;
  opacity: 0.7;
  margin-bottom: 20px;
}

.reset-button {
  background: rgba(155, 0, 255, 0.1);
  color: #bb86fc;
  border: none;
  padding: 10px 20px;
  border-radius: 20px;
  margin-top: 20px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.reset-button:hover {
  background: rgba(155, 0, 255, 0.2);
}

/* Адаптивность */
@media (max-width: 768px) {
  .home-page {
    padding: 15px;
  }
  
  .search-bar-container {
    flex-direction: column;
  }
  
  .search-input {
    border-radius: 20px;
    margin-bottom: 10px;
    border-right: 1px solid #333;
  }
  
  .search-button {
    border-radius: 20px;
    width: 100%;
    justify-content: center;
  }
  
  .excursion-results-section {
    grid-template-columns: 1fr;
  }
  
  .history-item {
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
  }
  
  .delete-button {
    align-self: flex-end;
  }
}

@media (max-width: 480px) {
  .card-details {
    flex-direction: column;
    gap: 8px;
  }
  
  .history-meta {
    flex-direction: column;
    gap: 5px;
  }
}
</style>