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
        for (let i = 0; i < 4; i++) {
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
      <input v-model="searchRequest" type="text" value="">
      <button @click="Search"></button>
    </div>
    <div class="excursion-results-section">
      <div class="excursion-list" v-for="excursion in filteredExcursionList" :key="excursion.id">
        <img :src="excursion.image" alt="Динамическое изображение">
        <p>{{ excursion.title }}</p>
        <p>Описание: {{ excursion.description }}</p>
        <p>Дата: {{ excursion.date }}</p>
        <p>Стоимость билета: {{ excursion.price }}₽</p>
        <p>Начало у {{ excursion.departure }}</p>
      </div>
      <div class="history-section">
        <p class="section-title">text2</p>
        <ul class="history-list">
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .excursion-list {
    padding: 15px;
    border-radius: 15px;
    background-color: rgb(59, 59, 59);
    border: 2px solid rgb(36, 36, 36);
    margin: 15px;
  }
  .excursion-results-section {
    display: flex;
    flex-wrap: wrap; 
    gap: 10px; 
  }
  p { 
    color: rgb(255, 255, 255);
  }
</style>
  
  