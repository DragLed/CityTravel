<script setup>
// Ваш скрипт
</script>

<template>
  <div id="app">
    <header class="app-header">
      <nav class="main-nav">
        <router-link to="/excursion" class="nav-link">Экскурсии</router-link>
        <router-link to="/Cats" class="nav-link">Коты</router-link>
        <router-link to="/My-To-Do-List" class="nav-link">📝 My To-Do List</router-link>
        <div class="nav-decoration"></div>
      </nav>
    </header>
    
    <main class="app-content">
      <router-view />
    </main>
    
    <footer class="app-footer">

    </footer>
  </div>
</template>

<style scoped>
#app {
  min-height: 100vh;
  background: #121218; /* Основной тёмный фон */
  color: #e0e0e0;
  display: flex;
  flex-direction: column;
}

.app-header {
  padding: 1.5rem 2rem;
  background: rgba(20, 20, 25, 0.8);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.2);
}

.app-content {
  flex: 1;
  padding: 2rem;
  background: linear-gradient(to bottom, rgba(18, 18, 24, 0.9), rgba(15, 15, 20, 0.95));
}

.app-footer {
  padding: 1.5rem;
  background: rgba(20, 20, 25, 0.8);
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  text-align: center;
  color: rgba(224, 224, 224, 0.6);
  font-size: 0.9rem;
}

/* Дополнительные стили для контента */
.app-content {
  color: #f0f0f0;
}

/* Стили для навигации (уже есть в вашем коде) */
.main-nav {
  position: relative;
  display: flex;
  gap: 1.5rem;
  padding: 1rem 2rem;
  background: rgba(30, 30, 36, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.05);
  max-width: max-content;
  margin: 0 auto;
}

.nav-link {
  position: relative;
  text-decoration: none;
  color: #e0e0e0;
  font-weight: 500;
  font-size: 1.1rem;
  padding: 0.5rem 1rem;
  transition: all 0.3s ease;
  z-index: 1;
  border-radius: 8px;
}

.nav-link:hover {
  color: #ffffff;
  background: rgba(60, 60, 70, 0.6);
}

.nav-link.router-link-exact-active {
  color: #4dabf7;
  font-weight: 600;
}

.nav-decoration {
  position: absolute;
  bottom: -5px;
  left: 0;
  height: 2px;
  background: linear-gradient(90deg, #4dabf7, #20c997);
  border-radius: 2px;
  transition: all 0.3s ease;
  z-index: 0;
}

.nav-link:hover::after {
  content: '';
  position: absolute;
  bottom: -3px;
  left: 50%;
  transform: translateX(-50%);
  width: 60%;
  height: 2px;
  background: #4dabf7;
  border-radius: 2px;
}

.nav-link.router-link-exact-active::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: calc(100% + 12px);
  height: calc(100% + 8px);
  border: 2px solid rgba(77, 171, 247, 0.3);
  border-radius: 10px;
  z-index: -1;
}

.main-nav {
  --glow-color: rgba(77, 171, 247, 0.1);
  box-shadow: 0 0 15px var(--glow-color), 
              0 4px 20px rgba(0, 0, 0, 0.3);
}

/* Дополнительные элементы для единообразия */
a {
  color: #4dabf7;
  text-decoration: none;
  transition: color 0.2s ease;
}

a:hover {
  color: #6bc0ff;
}

button {
  background-color: #4dabf7;
  color: white;
  border: none;
  padding: 0.6rem 1.2rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}

button:hover {
  background-color: #3a9ce6;
  transform: translateY(-1px);
}

input, textarea, select {
  background-color: rgba(40, 42, 54, 0.8);
  color: #e0e0e0;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 6px;
  padding: 0.5rem 0.8rem;
}

input:focus, textarea:focus, select:focus {
  outline: none;
  border-color: #4dabf7;
  box-shadow: 0 0 0 2px rgba(77, 171, 247, 0.2);
}
</style>