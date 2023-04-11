<template>
  <div class="mainteam row">
    <div id="barChart_1"></div>
    <div class="col-md-12" align="center">
      <img v-bind:src="this.team.logo">
      <br>
      <br>
      <h1><em>{{ this.team.name }}</em></h1>
    </div>
    <div class ="col-md-6 float-right">
      <br>
      <h4>Players List</h4>
      <ul class="list-group">
        <li class = "list-group-item"
        :class="{ active: index == currentIndex }"
        v-for="(player,index) in players"
        :key="index"
        >
          <span>{{ player.name }}</span>
          <img class = "players" v-bind:src="player.photo" align="right"/>
        </li>
      </ul>
    </div>
    <div class ="col-md-6">
      <br>
      <h4>Matches List</h4>
      <ul class="list-group">
        <li class = "list-group-item"
        :class="{ active: indexMatch == currentIndexMatch }"
        v-for="(match,indexMatch) in matches"
        :key="indexMatch"
        >
          <p align="center">Round {{ match.round }} vs {{ match.rivalTeam }} Score: <span :style= "[team.id == match.winnerId ? {'color':'green'} : match.winnerId == -1 ? {'color':'orange'} : {'color':'red'}]">{{ match.score }}</span></p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import http from '../http-common'
import bb, {bar} from 'billboard.js'

export default {
  name: 'MainTeam',
  data () {
    return {
      team: {},
      players: [],
      currentPlayer: null,
      currentIndex: -1,
      name: '',
      matches: [],
      currentMatch: null,
      currentIndexMatch: -1,
      chart: bb.generate({
        data: {
          columns: [
            ['data1', 30, 200, 100, 400, 150, 250],
            ['data2', 130, 100, 140, 200, 150, 50]
          ],
          type: bar() // for ESM specify as: bar()
        },
        bar: {
          width: {
            ratio: 0.5
          }
        },
        bindto: '#barChart_1',
        interaction: {
          enabled: false
        }
      })
    }
  },
  methods: {
    setActivePlayer (player, index) {
      this.currentPlayer = player
      this.currentIndex = index
    },
    setActiveMatch (match, indexMatch) {
      this.currentMatch = match
      this.currentIndexMatch = indexMatch
    }
  },
  mounted () {
    http.get('/players/' + this.$route.params.id).then((response) => {
      this.players = response.data
      console.log(response.data)
    })
      .catch((e) => {
        console.log(e)
      })

    http.get('/matches/' + this.$route.params.id).then((response) => {
      this.matches = response.data
      console.log(response.data)
    })
      .catch((e) => {
        console.log(e)
      })

    http.get('/teams/' + this.$route.params.id).then((response) => {
      this.team = response.data
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
.players{
  width: 100px;
  height: 100px;
}
</style>
