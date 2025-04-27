<script setup>
  import axios from 'axios';
  import { ref } from 'vue';
  import { useRoute } from 'vue-router';
  import { onMounted } from 'vue';

  const excursionList = ref([]);
  const filteredExcursionList = ref([]);
  const searchRequest = ref('');;
  const route = useRoute();

  function Search() {
    filteredExcursionList.value = [];
    excursionList.value = [];
    axios.get('/detailed_tours_20 (2).json')
    .then(function (response) {
      excursionList.value = response.data.tours;

      if (searchRequest.value) {
        const filteredExcursions = excursionList.value.filter(function(excursion) {
          return excursion.title.toLowerCase().includes(searchRequest.value.toLowerCase());
        });
        filteredExcursionList.value = filteredExcursions;

      } else {
        console.log('Поиск не выполнен, так как строка поиска пуста.');
        for (let i = 0; i < 6; i++) {
          filteredExcursionList.value.push(excursionList.value[i]); 
        }
      }
    })
    .catch(function (error) {
      console.error('Ошибка при загрузке данных:', error);
    });
}
onMounted(() => {
  Search();
})

</script>

<template>
  <div class="home-page">
    <div class="search-bar-container">
      <input @input="Search" v-model="searchRequest" type="text" value="" placeholder="Поиск городов, экскурсий..."> 
      <button @click="Search">Поиск</button>
    </div>
    <div class="excursion-results-section">
      <div class="excursion-list" v-if="filteredExcursionList" v-for="excursion in filteredExcursionList" :key="excursion.id">
        <!-- <img :src="excursion.image" alt="Динамическое изображение"> -->
        <h3>{{ excursion.title }}</h3>
        <span>{{ excursion.description }}</span>
        <span>Дата: {{ excursion.date }}</span>
        <span>Стоимость билета: {{ excursion.price }}₽</span>
        <span>Начало у {{ excursion.departure }}</span>
      </div>
      <div v-else>По запросу {{ searchRequest }} не найдено не одной экскурсии</div>
    </div>
    <div class="history-section">
      <p class="section-title">text2</p>
      <ul class="history-list"></ul>
    </div>
  </div>
</template>

<style scoped>

  .home-page {
    max-width: 900px;
    margin: 0 auto;
  }

  .search-bar-container {
    display: flex;
    margin-bottom: 20px;
  }

  .search-bar-container input {
      flex: 1;
      padding: 10px;
      background-color: #1f1f1f;
      border: 1px solid #333;
      border-right: none;
      color: #e0e0e0;
      border-radius: 6px 0 0 6px;
      font-size: 16px;
    }
    .search-bar-container button {
      padding: 10px 20px;
      background-color: #9b00ff;
      color: #fff;
      border: 1px solid #9b00ff;
      border-radius: 0 6px 6px 0;
      font-size: 16px;
      cursor: pointer;
    }

  .excursion-list {
    background-color: #1f1f1f;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: background 0.3s;
    color: #ffffff;
  }

  .excursion-list:hover {
    background-color: #292929;
  }

  .card a {
    color: #bb86fc;
    text-decoration: none;
    font-size: 14px;
    align-self: flex-start;
  }

  .excursion-list span {
    margin: 0 0 20px;
    color: #cccccc;
    font-size: 14px;
  }

  .excursion-list h3 {
    margin: 0 0 10px;
    font-size: 18px;
    color: #ffffff;
  }

  .excursion-results-section {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin-bottom: 30px; 
  }
  
</style>
  
  