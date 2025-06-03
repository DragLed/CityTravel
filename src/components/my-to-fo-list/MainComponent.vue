<script setup>
import { ref } from 'vue'

const message = ref('');
const noteList = ref([]);

const createTask = () => {
  if (message.value.trim() !== "") {
    noteList.value.push(message.value);
    console.log("Добавлена заметка: <" + message.value + ">");
    message.value = ''; 
  } else {
    alert("Введите текст в поле для ввода");
  }
}

function Delete(i){
    noteList.value.splice(i,1);
}
</script>

<template>
  <div class="To-Do-Container">
    <h1>📝 My To-Do List</h1>
    <div class="Input">
      <input 
        type="text" 
        placeholder="Новая задача" 
        v-model="message"
        @keyup.enter="createTask"  
      >
      <button @click="createTask">Добавить задачу</button>
    </div>
    <div class="taskList">
      <div 
        class="Note" 
        v-for="(note, i) in noteList" 
        :key="i"
      >
        <p>{{ note }}</p>
        <button @click="Delete(i)">Del</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Основные стили */
.To-Do-Container {
  max-width: 600px;
  margin: 0 auto;
  padding: 2rem;
  background-color: #1e1e1e;
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  color: #f0f0f0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h1 {
  text-align: center;
  margin-bottom: 1.5rem;
  color: #7c3aed;
  font-size: 2.2rem;
  text-shadow: 0 0 8px rgba(124, 58, 237, 0.4);
}

/* Стили для поля ввода */
.Input {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 2rem;
}

input {
  flex: 1;
  padding: 0.8rem 1rem;
  border: none;
  border-radius: 8px;
  background-color: #2d2d2d;
  color: #f0f0f0;
  font-size: 1rem;
  transition: all 0.3s ease;
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.2);
}

input:focus {
  outline: none;
  box-shadow: 0 0 0 2px #7c3aed, inset 0 1px 3px rgba(0, 0, 0, 0.2);
  transform: translateY(-1px);
}

input::placeholder {
  color: #888;
}

button {
  padding: 0.8rem 1.2rem;
  background-color: #7c3aed;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.2s ease;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

button:hover {
  background-color: #6d28d9;
  transform: translateY(-1px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}

button:active {
  transform: translateY(0);
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
}

/* Стили для списка задач */
.taskList {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.Note {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #2d2d2d;
  border-radius: 8px;
  animation: fadeIn 0.3s ease-out forwards;
  transform-origin: top;
  transition: all 0.2s ease;
}

.Note:hover {
  background-color: #3a3a3a;
  transform: scale(1.01);
}

.Note p {
  margin: 0;
  flex: 1;
  word-break: break-word;
}

.Note button {
  background-color: #dc2626;
  padding: 0.5rem 0.8rem;
  margin-left: 1rem;
}

.Note button:hover {
  background-color: #b91c1c;
}

/* Анимации */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.03);
  }
  100% {
    transform: scale(1);
  }
}

/* Анимация при добавлении задачи */
.Note:first-child {
  animation: fadeIn 0.3s ease-out, pulse 0.5s ease 0.3s;
}
</style>