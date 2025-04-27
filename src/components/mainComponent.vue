<script setup>
  import axios from 'axios';
  import { ref } from 'vue';
  import { useRoute } from 'vue-router';
  import { onMounted } from 'vue';

  const excursionList = ref([]);
  const filteredExcursionList = ref([]);
  const searchRequest = ref('');
  const HistoryList = ref([]);
  const route = useRoute();

  // Функция для поиска туров
  function Search() {
    filteredExcursionList.value = [];
    excursionList.value = [];
    axios.get('/detailed_tours_20 (2).json')
    .then(function (response) {
      excursionList.value = response.data;

      if (searchRequest.value == 'TEST'){
        filteredExcursionList.value = excursionList.value;
      } else if (searchRequest.value) {
        const filteredExcursions = excursionList.value.filter(function(excursion) {
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

  // Функция для получения истории туров
  function GetHistory() {
  // Загружаем историю туров из localStorage
  const history = JSON.parse(localStorage.getItem('tourHistory')) || [];

  // Записываем её в переменную HistoryList
  HistoryList.value = history;

  console.log("История туров:", HistoryList.value);
}


  // Функция для перехода к туру и сохранения его в историю
  function GoToTour(name, id, date) {
    // Загружаем текущую историю из localStorage
    let tourHistory = JSON.parse(localStorage.getItem('tourHistory')) || [];

    // Проверяем, чтобы тур с таким ID не был уже в истории (если не хочешь дублировать)
    const existingTour = tourHistory.find(tour => tour.id === id);
    if (!existingTour) {
      // Добавляем новый тур в историю
      tourHistory.push({ id, name ,date});
    }

    // Сохраняем обновленную историю в localStorage
    localStorage.setItem('tourHistory', JSON.stringify(tourHistory));

    console.log("Запись истории в localStorage:", tourHistory);
    GetHistory();
  }

  // Функция для удаления истории туров
  function deleteHistory(id) {
    let tourHistory = JSON.parse(localStorage.getItem('tourHistory')) || [];

    // Фильтруем историю, исключая тур с заданным id
    tourHistory = tourHistory.filter(tour => tour.id !== id);

    // Сохраняем обновленную историю в localStorage
    localStorage.setItem('tourHistory', JSON.stringify(tourHistory));

    console.log(`Тур с ID "${id}" удалён из истории`);
    GetHistory();
  }

  // Загружаем данные при монтировании компонента
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
      <div class="excursion-list" @click="GoToTour(excursion.title, excursion.id, excursion.date)" v-if="filteredExcursionList" v-for="excursion in filteredExcursionList" :key="excursion.id">
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
      <h4>История посещений:</h4>
        <div v-if="HistoryList.length > 0">
          <div class="historyblock" v-for="History in HistoryList" :key="History.id">
            <div>
              <p @click="GoToTour(History.name, History.id, History.date)">{{ History.name }} </p>
              <p>{{ History.date }}</p>
            </div>
            <button @click="deleteHistory(History.id)">Удалить</button>
          </div>
        </div>
      <p v-else>История пуста</p>
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
    transition: 0.3s;
    color: #ffffff;
  }

  .excursion-list:hover {
    background-color: #292929;

    margin: -10px;
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
  .history {
      background-color: #1e1e1e;
      padding: 15px;
      border-radius: 6px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.7);
      border: 1px solid #333;
    }
    .history h4 {
      margin-top: 0;
      font-size: 16px;
      margin-bottom: 10px;
      color: #fff;
    }

    .historyblock {
      padding: 8px 0;
      border-bottom: 1px solid #333;
      color: #ccc;
      
    }

    .historyblock p {
      transition: 0.1s;
    }

    .historyblock p:hover {
      opacity: 0.3;
    }
    .history li:last-child {
      border-bottom: none;
    }
  
  .historyblock {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .historyblock button{
    background-color: rgb(0, 170, 255);
    border: 1.5px solid rgb(4, 121, 180);
    border-radius: 15px;
    padding: 7px;
    transition: 0.5s;
  }

  .historyblock button:hover{
    background-color: rgb(255, 0, 0);
    border: 1.5px solid rgb(204, 0, 0);
    padding:3px;
    margin-right: 2px;
  }


</style>
  
  