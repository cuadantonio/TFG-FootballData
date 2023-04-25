<template>
    <div class="teammatch row">
        <div class="row">
            <div class="col-md-12" align="center">
                <span><img v-bind:src="this.team.logo"><h1><em>vs {{ this.match.rivalTeam }}</em></h1></span>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12" align="center">
                <h2>Stats</h2>
                <h3>Round: <em style="color: #2F6690;">{{ this.match.round }}</em></h3>
                <h3>Side: <em style="color: #2F6690;">{{ this.match.side }}</em></h3>
                <h3>Score: <span :style= "[this.team.id == this.match.winnerId ? {'color':'green'} : this.match.winnerId == -1 ? {'color':'orange'} : {'color':'red'}]">{{ this.match.score }}</span></h3>
                <h3>Fouls: <em style="color: #FFA100;">{{ this.match.fouls }}</em></h3>
                <h3>Corners: <em style="color: #FFA100;">{{ this.match.corners }}</em></h3>
                <h3>Offsides: <em style="color: #FFA100;">{{ this.match.offsides }}</em></h3>
                <h3>Ball lPossession: <em style="color: #59C3C3;">{{ this.match.ballPossession }}</em></h3>
                <h3>Goalkeeper Saves: <em style="color: #59C3C3;">{{ this.match.goalkeeperSaves }}</em></h3>
            </div>
        </div>
        <div class="row">
            <div class="col-md-6" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="shots" align="center"></canvas></div>
            <div class="col-md-6" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="passes" align="center"></canvas></div>
        </div>
        <div class="row">
            <div class="col-md-12" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="cards" align="center"></canvas></div>
        </div>
    </div>
</template>
<script>
import http from '../http-common'
import Chart from 'chart.js'

export default {
  name: 'TeamMatch',
  data () {
    return {
      match: {},
      team: {},
      rivalTeam: {},
      shotsChart: {},
      passesChart: {},
      cardsChart: {}
    }
  },
  created () {
    http.get('/match/' + this.$route.params.fixtureId + '/' + this.$route.params.teamId).then((response) => {
      this.match = response.data
      console.log(response.data)
    })
      .catch((e) => {
        console.log(e)
      })

    http.get('/teams/' + this.$route.params.teamId).then((response) => {
      this.team = response.data
      console.log(response.data)
    })
      .catch((e) => {
        console.log(e)
      })
    http.get('/teams/' + this.$route.params.rivalTeamId).then((response) => {
      this.rivalTeam = response.data
      console.log(response.data)
    })
      .catch((e) => {
        console.log(e)
      })
    this.$forceUpdate()
  },
  updated () {
    this.shotsChart = new Chart(document.getElementById('shots'),
      {
        type: 'bar',
        data: {
          labels: ['Shots On Goal', 'Shots Off Goal', 'Shots Inside Box', 'Shots Outside Box', 'Shots Blocked', 'Total Shots'],
          datasets: [
            {
              label: 'Shots',
              data: [this.match.shotsOnGoal, this.match.shotsOffGoal, this.match.shotsInsidebox, this.match.shotsOutsidebox, this.match.blockedShots, this.match.totalShots],
              base: 0,
              backgroundColor: ['#2F6690', '#FFA100', '#EA526F', '#59C3C3', '#AF9AB2', '#2F6690']
            }
          ]
        }
      }
    )
    this.passesChart = new Chart(document.getElementById('passes'),
      {
        type: 'bar',
        data: {
          labels: ['Accurate Passes', 'Total Passes'],
          datasets: [
            {
              label: 'Passes',
              data: [this.match.passesAccurate, this.match.totalPasses],
              base: 0,
              backgroundColor: ['#2F6690', '#FFA100']
            }
          ]
        }
      }
    )
    this.cardsChart = new Chart(document.getElementById('cards'),
      {
        type: 'pie',
        data: {
          labels: ['Yellow Cards', 'Red Cards'],
          datasets: [
            {
              data: [this.match.yellowCards, this.match.redCards],
              backgroundColor: ['#2F6690', '#FFA100']
            }
          ]
        }
      }
    )
    Chart.defaults.global.defaultFontColor = '#fff'
  }
}
</script>
<style scoped>
#cards{
  position: relative;
  left: 320px;
}
</style>
