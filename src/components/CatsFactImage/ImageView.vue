<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { onMounted } from 'vue';

const imageUrl = ref('');
const tags = ref(['']);
const selectedTag = ref('');

function GetImage() {
    imageUrl.value = '';
    console.log(selectedTag.value);
    if (selectedTag.value != "") {
        axios.get('https://cataas.com/cat/'+ selectedTag.value +'?position=center&json=true')
  .then(response => {
    console.log(response.data.url)
    imageUrl.value = response.data.url;

  })
  .catch(error => {
    console.error('Ошибка:', error.message);
  });
    }
    else {
      axios.get('https://cataas.com/cat?json=true')
  .then(response => {
    console.log(response.data.url)
    imageUrl.value = response.data.url;

  })
  .catch(error => {
    console.error('Ошибка:', error.message);
  });
    }
}

function GetTags () {
    axios.get('https://cataas.com/api/tags')
  .then(response => {
    console.log(response.data);
    tags.value = response.data;
  })
  .catch(error => {
    console.log(error);
  })
}

onMounted(() => {
    GetImage();
    GetTags();
})
</script>

<template>
<div  class="MainForm">
    <b><p class="TextForm">Случайная картинка котика</p></b>
    <div class="Image">
        <img v-if="imageUrl" :src="imageUrl" alt="Динамическое изображение">
        <p v-else>Загрузка...</p>
        <button class="ReloadBtn" @click="GetImage">Другая каринка</button>
    </div>
    <div>
    <label for="tag-select">Выбери тег:</label>
    <select id="tag-select" v-model="selectedTag">
      <option v-for="(tag, index) in tags" :key="index" :value="tag">
        {{ tag }}
      </option>
    </select>
  </div>
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

.Image {
    background-color: rgba(40, 42, 54, 0.8);
    max-width: 600px;
    padding: 25px;
    border-radius: 15px;
    display: flex;
    flex-direction: column;
    text-align: center;
    align-items: center;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.Image img {
    height: 300px;
    width: 300px;
    border-radius: 25px;
    border: 2px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    transition: transform 0.3s ease;
}

.Image img:hover {
    transform: scale(1.02);
}

.ReloadBtn {
    background-color: #4dabf7;
    color: white;
    border: none;
    margin-top: 25px;
    border-radius: 8px;
    padding: 12px 25px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(77, 171, 247, 0.2);
}

.ReloadBtn:hover {
    background-color: #339af0;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(77, 171, 247, 0.3);
}

select {
    background-color: rgba(40, 42, 54, 0.8);
    color: #e0e0e0;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    padding: 8px 15px;
    margin-top: 1rem;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
}

select:hover {
    border-color: rgba(77, 171, 247, 0.5);
}

select:focus {
    outline: none;
    border-color: #4dabf7;
    box-shadow: 0 0 0 2px rgba(77, 171, 247, 0.2);
}

label {
    margin-right: 10px;
    color: #a5d8ff;
}
</style>