<template>
  <div class="mainpage row">
    <div class="col-md-12" align="center">
        <img v-bind:src="this.player.photo">
      <br>
      <br>
      <h1><em>{{ this.player.name }}</em></h1>
      <h4>Number: <em>{{this.player.number}}</em></h4>
      <h4>Goals: <em>{{this.player.goals}}</em></h4>
      <h4>Passes: <em>{{this.player.passes}}</em></h4>
      <h4>Conceded goals: <em>{{this.player.concededGoals}}</em></h4>
      <h4>Saves: <em>{{this.player.saves}}</em></h4>
      <br>
      <br>
      <h1>Fantasy Manager Stats</h1>
      <h4>Mister Fantasy Points: <em>{{this.player.misterFantasyPoints}}</em></h4>
      <h4>Mister Fantasy Price: <em>{{this.player.misterFantasyPrice}}</em></h4>
      <h4>Futmondo Points: <em>{{this.player.futmondoPoints}}</em></h4>
      <h4>Futmondo Price: <em>{{this.player.futmondoPrice}}</em></h4>
      <h4>Comunio Points: <em>{{this.player.comunioPoints}}</em></h4>
      <h4>Comunio Price: <em>{{this.player.comunioPrice}}</em></h4>
      <h4>Biwenger Points: <em>{{this.player.biwengerPoints}}</em></h4>
      <h4>Biwenger Price: <em>{{this.player.biwengerPrice}}</em></h4>
      <h4>La Liga Fantasy Points: <em>{{this.player.laligaPoints}}</em></h4>
      <h4>La Liga Fantasy Price: <em>{{this.player.laligaPrice}}</em></h4>
    </div>
  </div>
</template>

<script>
import http from '../http-common'

export default {
  name: 'MainTeam',
  data () {
    return {
      player: {}
    }
  },
  methods: {
  },
  mounted () {
    http.get('/player/' + this.$route.params.id).then((response) => {
      this.player = response.data
      console.log(response.data)
    })
      .catch((e) => {
        console.log(e)
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.list-group {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>
