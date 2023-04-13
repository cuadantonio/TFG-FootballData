<template>
  <div class="mainteam row">
    <div class="col-md-12" align="center">
      <img v-bind:src="this.team.logo">
      <br>
      <br>
      <h1><em>{{ this.team.name }}</em></h1>
    </div>
    <div class="col-md-12" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="results" align="center"></canvas></div>
    <div></div>
    <div class="col-md-6" align="center"><canvas id="goals" align="center"></canvas></div>
    <div class="col-md-6" align="center"><canvas id="goalsAverage" align="center"></canvas></div>
    <div class="col-md-6" align="center"><canvas id="cards" align="center"></canvas></div>
    <div class="col-md-6" align="center"><canvas id="scores" align="center"></canvas></div>
    <div class ="col-md-6 float-right">
      <br>
      <h4>Players List</h4>
      <ul class="list-group">
        <li class = "list-group-item"
        :class="{ active: index == currentIndex }"
        v-for="(player,index) in players"
        :key="index"
        >
          <span class="playerName">{{ player.name }}</span>
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
import Chart from 'chart.js'

export default {
  name: 'MainTeam',
  data () {
    return {
      results: [],
      resultsChart: {},
      team: {},
      players: [],
      currentPlayer: null,
      currentIndex: -1,
      name: '',
      matches: [],
      currentMatch: null,
      currentIndexMatch: -1,
      goalsFor: [],
      goalsAgainst: [],
      goalsChart: {},
      goalsForAverage: [],
      goalsAgainstAverage: [],
      goalsAverageChart: {},
      yellowCards: '',
      redCards: '',
      cardsChart: {},
      homeCleanSheets: '',
      awayCleanSheets: '',
      homeFailedToScore: '',
      awayFailedToScore: '',
      scoresChart: {}
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
  created () {
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
    this.$forceUpdate()
  },
  updated () {
    this.results.push(this.team.totalWins)
    this.results.push(this.team.totalLoses)
    this.results.push(this.team.totalDraws)
    this.goalsFor.push(this.team.homeGoalsFor)
    this.goalsFor.push(this.team.awayGoalsFor)
    this.goalsFor.push(this.team.totalGoalsFor)
    this.goalsAgainst.push(this.team.homeGoalsAgainst)
    this.goalsAgainst.push(this.team.awayGoalsAgainst)
    this.goalsAgainst.push(this.team.totalGoalsAgainst)
    this.goalsForAverage.push(this.team.homeGoalsForAverage)
    this.goalsForAverage.push(this.team.awayGoalsForAverage)
    this.goalsForAverage.push(this.team.totalGoalsForAverage)
    this.goalsAgainstAverage.push(this.team.homeGoalsAgainstAverage)
    this.goalsAgainstAverage.push(this.team.awayGoalsAgainstAverage)
    this.goalsAgainstAverage.push(this.team.totalGoalsAgainstAverage)
    this.yellowCards = this.team.totalYellowCards
    this.redCards = this.team.totalRedCards
    this.homeCleanSheets = this.team.homeCleanSheets
    this.awayCleanSheets = this.team.awayCleanSheets
    this.homeFailedToScore = this.team.homeFailedToScore
    this.awayFailedToScore = this.team.awayFailedToScore
    this.resultsChart = new Chart(document.getElementById('results'),
      {
        type: 'bar',
        data: {
          labels: ['Wins', 'Defeats', 'Draws'],
          datasets: [
            {
              label: 'Results',
              data: this.results,
              base: 0,
              backgroundColor: ['green', '#FF0000', 'ED830C']
            }
          ]
        }
      }
    )
    this.goalsChart = new Chart(document.getElementById('goals'),
      {
        type: 'bar',
        data: {
          labels: ['Home', 'Away', 'Total'],
          datasets: [
            {
              label: 'Goals For',
              data: this.goalsFor,
              base: 0,
              backgroundColor: '#0C67F0'
            },
            {
              label: 'Goals Against',
              data: this.goalsAgainst,
              base: 0,
              backgroundColor: '#E68805'
            }
          ]
        }
      })
    this.goalsAverageChart = new Chart(document.getElementById('goalsAverage'),
      {
        type: 'bar',
        data: {
          labels: ['Home', 'Away', 'Total'],
          datasets: [
            {
              label: 'Goals For Average',
              data: this.goalsForAverage,
              base: 0,
              backgroundColor: '#0C67F0'
            },
            {
              label: 'Goals Against Average',
              data: this.goalsAgainstAverage,
              base: 0,
              backgroundColor: '#E68805'
            }
          ]
        }
      })
    this.cardsChart = new Chart(document.getElementById('cards'),
      {
        type: 'pie',
        data: {
          labels: ['Yellow Cards', 'Red Cards'],
          datasets: [
            {
              data: [this.yellowCards, this.redCards],
              base: 0,
              backgroundColor: ['#DEE605', '#ED1A02']
            }
          ]
        }
      })
    this.scoresChart = new Chart(document.getElementById('scores'),
      {
        type: 'pie',
        data: {
          labels: ['Home Clean Sheets', 'Away Clean Sheets', 'Home Failed To Score', 'Away Failed To Score'],
          datasets: [
            {
              data: [this.homeCleanSheets, this.awayCleanSheets],
              backgroundColor: ['#0C67F0', '#E68805']
            },
            {
              data: [this.homeFailedToScore, this.awayFailedToScore],
              backgroundColor: ['#0C67F0', '#E68805']
            }
          ]
        }
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
  border: 2px solid #000;
}
.players{
  width: 60px;
  height: 60px;
  border: 1px solid #000;
  border-radius: 10px;
}
.playerName{
  position: relative;
  top: 15px;
}
#results{
  position: relative;
  left: 320px;
}
</style>
