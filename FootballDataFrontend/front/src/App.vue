<template>
  <div id="app">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <router-link to="/" style="margin-left: 22%; margin-bottom: -65px; margin-top: -60px;"><img style="height: 15%; width: 15%;" src="./assets/logo.png"/></router-link>
    </nav>
    <div class="container mt-3">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
</style>
