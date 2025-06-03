<script setup>

</script>

<template>
<div  class="MainForm">
    <b><p class="WellcomeTetx">Добро пожаловать!</p></b>
    <nav>
        <router-link to="/Cats/Fact"><button class="GetRandomFactBtn">Получить случайный факт</button></router-link>
        <router-link to="/Cats/Image"><button class="GetImageBtn">Получить картинку</button></router-link>
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
    min-height: 100vh;
    justify-content: center;
}

.WellcomeText {
    font-size: 2rem;
    color: #a5d8ff;
    margin-bottom: 2rem;
    text-shadow: 0 2px 10px rgba(165, 216, 255, 0.3);
}

nav {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.GetRandomFactBtn, .GetImageBtn {
    background-color: rgba(40, 42, 54, 0.8);
    color: #e0e0e0;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 15px;
    margin: 0;
    width: 300px;
    font-size: 1.1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.GetRandomFactBtn:hover {
    background-color: rgba(32, 201, 151, 0.2);
    border-color: rgba(32, 201, 151, 0.3);
    transform: translateY(-3px);
}

.GetImageBtn:hover {
    background-color: rgba(77, 171, 247, 0.2);
    border-color: rgba(77, 171, 247, 0.3);
    transform: translateY(-3px);
}

.GetRandomFactBtn:active, .GetImageBtn:active {
    transform: translateY(0);
}
</style>