<template>
  <div id="app" class="page-container">
    <img alt="Vue logo" src="./assets/logo.png" class="logo">
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'App',
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.logo {
  height: 75px;
}
.page-container {
  max-width: 900px;
  margin: 0 auto;
}
</style>
