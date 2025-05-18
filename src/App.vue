<script setup>
// Ваш скрипт
</script>

<template>
  <div id="app">
    <header class="app-header">
      <nav class="main-nav">
        <router-link to="/" class="nav-link">Экскурсии</router-link>
        <div class="nav-decoration"></div>
      </nav>
    </header>
    
    <main class="app-content">
      <router-view />
    </main>
    
    <footer class="app-footer">
      <p>© 2025 Туристическое приложение. Все права защищены.</p>
    </footer>
  </div>
</template>

<style scoped>
#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #121212;
  color: #e0e0e0;
  font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  line-height: 1.6;
}

.app-header {
  background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
  padding: 1rem 2rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  position: sticky;
  top: 0;
  z-index: 100;
}

.main-nav {
  display: flex;
  gap: 2rem;
  position: relative;
  max-width: 1200px;
  margin: 0 auto;
}

.nav-link {
  color: #e0e0e0;
  text-decoration: none;
  font-weight: 500;
  font-size: 1.1rem;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: all 0.3s ease;
  position: relative;
}

.nav-link:hover {
  color: #3f6285;
  background-color: rgba(255, 255, 255, 0.05);
}

.nav-link.router-link-exact-active {
  color: #3f6285;
}

.nav-link.router-link-exact-active::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 50%;
  transform: translateX(-50%);
  width: 60%;
  height: 2px;
  background-color: #3f6285;
  border-radius: 2px;
}

.nav-decoration {
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 40px;
  height: 40px;
  background-color: #3f6285;
  opacity: 0.2;
  border-radius: 50%;
  filter: blur(8px);
}

.app-content {
  flex: 1;
  padding: 2rem;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
}

.app-footer {
  background: linear-gradient(135deg, #2d2d2d 0%, #1a1a1a 100%);
  padding: 1.5rem;
  text-align: center;
  font-size: 0.9rem;
  color: #888;
  margin-top: auto;
}

/* Адаптивность */
@media (max-width: 768px) {
  .main-nav {
    gap: 1rem;
    justify-content: center;
  }
  
  .app-content {
    padding: 1rem;
  }
  
  .nav-link {
    font-size: 1rem;
    padding: 0.5rem;
  }
  
  .nav-decoration {
    display: none;
  }
}
</style>