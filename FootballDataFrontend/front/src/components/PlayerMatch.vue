<template>
    <div class="playermatch row">
        <div class="row">
            <div class="col-md-12" align="center">
                <span><img v-bind:src="this.player.photo"><h1><em>vs {{ this.match.rivalTeam }}</em></h1></span>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12" align="center">
                <h2>Stats</h2>
                <h3>Round: <em style="color: #2F6690;">{{ this.match.round }}</em></h3>
                <h3>Minutes: <em style="color: #2F6690;">{{ this.match.minutes}}</em></h3>
                <h3>Score: <span :style= "[this.team.id == this.match.winnerId ? {'color':'green'} : this.match.winnerId == -1 ? {'color':'orange'} : {'color':'red'}]">{{ this.match.score }}</span></h3>
                <h3>Offsides: <em style="color: #FFA100;">{{ this.match.offsides }}</em></h3>
                <h3>Saves: <em style="color: #FFA100;">{{ this.match.saves }}</em></h3>
            </div>
        </div>
        <div class="row">
            <div class="col-md-6" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="shots" align="center"></canvas></div>
            <div class="col-md-6" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="passes" align="center"></canvas></div>
        </div>
        <div class="row">
            <div class="col-md-6" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="tackles" align="center"></canvas></div>
            <div class="col-md-6" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="dribbles" align="center"></canvas></div>
        </div>
        <div class="row">
            <div class="col-md-6" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="fouls" align="center"></canvas></div>
            <div class="col-md-6" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="duels" align="center"></canvas></div>
        </div>
        <div class="row">
            <div class="col-md-12" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="cards" align="center"></canvas></div>
        </div>
        <div class="row">
            <div class="col-md-12" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="penalties" align="center"></canvas></div>
        </div>
    </div>
</template>
<script>
import http from '../http-common'
import Chart from 'chart.js'

export default {
  name: 'PlayerMatch',
  data () {
    return {
      match: {},
      team: {},
      rivalTeam: {},
      player: {},
      shotsChart: {},
      passesChart: {},
      tacklesChart: {},
      duelsChart: {},
      dribblesChart: {},
      foulsChart: {},
      cardsChart: {},
      penaltiesChart: {}
    }
  },
  created () {
    http.get('/playerinmatch/match/' + this.$route.params.fixtureId + '/' + this.$route.params.playerId).then((response) => {
      this.match = response.data
      console.log(response.data)
    })
      .catch((e) => {
        console.log(e)
      })

    http.get('/player/' + this.$route.params.playerId).then((response) => {
      this.player = response.data
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
          labels: ['Total Shots', 'Shots On', 'Total Goals', 'Conceded Goals'],
          datasets: [
            {
              label: 'Shots',
              data: [this.match.totalShots, this.match.shotsOn, this.match.totalGoals, this.match.concededGoals],
              base: 0,
              backgroundColor: ['#2F6690', '#FFA100', '#EA526F', '#59C3C3']
            }
          ]
        }
      }
    )
    this.passesChart = new Chart(document.getElementById('passes'),
      {
        type: 'bar',
        data: {
          labels: ['Key Passes', 'Total Passes', 'Assists'],
          datasets: [
            {
              label: 'Passes',
              data: [this.match.keyPasses, this.match.totalPasses, this.match.assists],
              base: 0,
              backgroundColor: ['#2F6690', '#FFA100', '#EA526F']
            }
          ]
        }
      }
    )
    this.tacklesChart = new Chart(document.getElementById('tackles'),
      {
        type: 'pie',
        data: {
          labels: ['Total Tackles', 'Block Tackles', 'Interception Tackles'],
          datasets: [
            {
              data: [this.match.totalTackles, this.match.blockTackles, this.match.interceptionTackles],
              backgroundColor: ['#2F6690', '#FFA100', '#EA526F']
            }
          ]
        }
      }
    )
    this.dribblesChart = new Chart(document.getElementById('dribbles'),
      {
        type: 'pie',
        data: {
          labels: ['Dribbles Attempts', 'Dribbles Success', 'Dribbles Past'],
          datasets: [
            {
              data: [this.match.dribblesAttempts, this.match.dribblesSuccess, this.match.dribblesPast],
              backgroundColor: ['#2F6690', '#FFA100', '#EA526F']
            }
          ]
        }
      }
    )
    this.foulsChart = new Chart(document.getElementById('fouls'),
      {
        type: 'bar',
        data: {
          labels: ['Fouls Drawn', 'Fouls Committed'],
          datasets: [
            {
              label: 'Fouls',
              data: [this.match.foulsDrawn, this.match.foulsCommitted],
              base: 0,
              backgroundColor: ['#2F6690', '#FFA100']
            }
          ]
        }
      }
    )
    this.duelsChart = new Chart(document.getElementById('duels'),
      {
        type: 'bar',
        data: {
          labels: ['Total Duels', 'Duels Won'],
          datasets: [
            {
              label: 'Duels',
              data: [this.match.totalDuels, this.match.duelsWon],
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
    this.penaltiesChart = new Chart(document.getElementById('penalties'),
      {
        type: 'bar',
        data: {
          labels: ['Penalties Committed', 'Penalties Missed', 'Penalties Saved', 'Penalties Scored', 'Penalties Won'],
          datasets: [
            {
              label: 'Penalties',
              data: [this.match.penaltiesCommitted, this.match.penaltiesMissed, this.match.penaltiesSaved, this.match.penaltiesScored, this.match.penaltiesWon],
              base: 0,
              backgroundColor: ['#2F6690', '#FFA100', '#EA526F', '#59C3C3', '#AF9AB2']
            }
          ]
        }
      }
    )
    Chart.defaults.global.defaultFontColor = '#000000'
  }
}
</script>
<style scoped>
#cards{
  position: relative;
  left: 320px;
}
#penalties{
  position: relative;
  left: 320px;
}
</style>
