<script setup>
  import axios from 'axios';
  import { ref } from 'vue';
  import { useRoute } from 'vue-router';

  const excursionList = ref([]);
  const searchRequest = ref('');
  import { onMounted } from 'vue';


  function Search () {
    
    axios.get('/detailed_tours_20 (2).json')
    .then(function (response) {
      excursionList.value = response.data.tours;
      console.log(excursionList.value);
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
      <p class="section-titles">text</p>
      <div class="excursion-list" v-for="excursion in excursionList">
        <img :src="excursion.image" alt="Динамическое изображение">
        <p>{{ excursion.title }}</p>
        <p>Описание: {{ excursion.description }}</p>
        <p>Дата: {{ excursion.date }}</p>
        <p>{{ excursion.price }}</p>
        <p>Начало у {{ excursion.departure }}</p>
        <p>{{ excursion.title }}</p>
      </div>
      br
      <div class="history-section">
        <p class="section-title">text2</p>
        <ul class="history-list">

        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
  
  