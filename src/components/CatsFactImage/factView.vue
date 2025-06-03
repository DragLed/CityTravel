<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { onMounted } from 'vue';

const Fact = ref('');

function Getfact() {
    Fact.value = '';
    axios.get('https://meowfacts.herokuapp.com')
  .then(response => {
    console.log(response.data.data[0]);
    Fact.value = response.data.data[0];
  })
  .catch(error => {
    console.error('Ошибка:', error.message);
  });

}



onMounted(() => {
    Getfact();
})

</script>

<template>
<div  class="MainForm">
    <b><p class="TextForm">Случайный факт о котах</p></b>
    <div class="Fact">
        <p v-if="Fact" class="Catfact">{{ Fact }}</p>
        <p v-else>Загрузка...</p>
        <button class="ReloadBtn" @click="Getfact">Ещё факт</button>
    </div>
    <nav>
    </nav>
</div>
</template>

<style scoped>
.MainForm {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    font-size: 18px;
    color: #e0e0e0;
}

.TextForm {
    color: #a5d8ff;
    margin-bottom: 1.5rem;
}

.Fact {
    background-color: rgba(40, 42, 54, 0.8);
    max-width: 600px;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.Catfact {
    line-height: 1.6;
    margin-bottom: 1.5rem;
    color: #f8f9fa;
}

.ReloadBtn {
    background-color: #20c997;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 25px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(32, 201, 151, 0.2);
}

.ReloadBtn:hover {
    background-color: #12b886;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(32, 201, 151, 0.3);
}
</style>