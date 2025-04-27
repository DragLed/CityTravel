<script setup>

</script>

<!-- src/App.vue -->
<template>
    <div id="app">
      <nav>
        <router-link to="/">Home</router-link> |
        <router-link to="/excursion">Excursion</router-link>
      </nav>
      <router-view />
    </div>
  </template>

<style scoped>
  #app {
    background-color: #121212;
    width: 100%;
    height: 100vh;
    color: #e0e0e0;
    margin: 0;
    padding: 20px;
  }
</style>


