<template>
  <div id="app">
    <to-do></to-do>
  </div>
</template>

<script>
import ToDo from './components/ToDo'
export default {
  components: { ToDo },
  name: 'App',
  Components: {
    ToDo
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
