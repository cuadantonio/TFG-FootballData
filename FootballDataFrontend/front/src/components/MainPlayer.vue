<template>
  <div class="mainpage row">
    <div class="row">
      <div class="col-md-12" align="center">
      <img v-bind:src="this.player.photo">
      <br>
      <br>
      <h1><em>{{ this.player.name }}</em></h1>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12" align="center">
        <h2>Stats</h2>
        <h3>Number: <em style="color: #2F6690;">{{ this.player.number }}</em></h3>
        <h3>Position: <em style="color: #2F6690;">{{ this.player.position }}</em></h3>
        <h3>Rating: <em style="color: #2F6690;">{{ this.player.rating }}</em></h3>
        <h3>Age: <em style="color: #FFA100;">{{ this.player.age }}</em></h3>
        <h3>Height: <em style="color: #FFA100;">{{ this.player.height }}</em></h3>
        <h3>Weight: <em style="color: #FFA100;">{{ this.player.weight }}</em></h3>
        <h3>Is injured?: <em style="color: #FFA100;">{{ this.player.isInjured }}</em></h3>
        <h3>Biwenger Points: <em style="color: #EA526F;">{{ this.player.biwengerPoints }}</em></h3>
        <h3>Biwenger Price: <em style="color: #EA526F;">{{ this.player.biwengerPrice }}</em></h3>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="shots" align="center"></canvas></div>
    </div>
    <div class="row">
      <div class="col-md-6" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="defense" align="center"></canvas></div>
      <div class="col-md-6" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="goalkeeperDefense" align="center"></canvas></div>
    </div>
    <div class="row">
      <div class="col-md-12" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="duels" align="center"></canvas></div>
    </div>
    <div class="row">
      <div class="col-md-6" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="dribbles" align="center"></canvas></div>
      <div class="col-md-6" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="fouls" align="center"></canvas></div>
    </div>
    <div class="row">
      <div class="col-md-6" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="passes" align="center"></canvas></div>
      <div class="col-md-6" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="penalties" align="center"></canvas></div>
    </div>
    <div class = "row">
      <div class="col-md-12" style="height: 50%; width: 50%; left: 100;" align="center"><canvas id="cards" align="center"></canvas></div>
    </div>
    <div class="row">
      <div class ="col-md-6" align="center" id="matchList">
      <br>
      <h4>Matches List</h4>
      <ul class="list-group" align="center">
        <li class = "list-group-item"
        :class="{ active: indexMatch == currentIndexMatch }"
        v-for="(match,indexMatch) in playerMatches"
        :key="indexMatch"
        >
          <router-link :to="'/playermatch/' + match.fixtureId + '/' + match.playerId + '/' + match.teamId + '/' + match.rivalTeamId"><p align="center">Round {{ match.round }} vs {{ match.rivalTeam }} Score: <span :style= "[match.teamId == match.winnerId ? {'color':'green'} : match.winnerId == -1 ? {'color':'orange'} : {'color':'red'}]">{{ match.score }}</span></p></router-link>
        </li>
      </ul>
      </div>
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
      player: {},
      playerMatches: [],
      currentIndexMatch: -1,
      shotsChart: {},
      shots: [],
      defenseChart: {},
      tackles: '',
      blocks: '',
      goalkeeperDefenseChart: {},
      saves: '',
      concededGoals: '',
      duelsChart: {},
      duels: [],
      dribblesChart: {},
      dribblesSuccess: '',
      dribblesAttempts: '',
      foulsChart: {},
      foulsCommitted: '',
      foulsDrawn: '',
      passesChart: {},
      passes: [],
      penaltiesChart: {},
      penalties: [],
      cardsChart: {},
      yellowCards: '',
      redCards: '',
      yellowRedCards: '',
      teamInMatch: {}
    }
  },
  methods: {
  },
  created () {
    http.get('/player/' + this.$route.params.id).then((response) => {
      this.player = response.data
      console.log(response.data)
    })
      .catch((e) => {
        console.log(e)
      })
    http.get('/playerinmatch/matches/' + this.$route.params.id).then((response) => {
      this.playerMatches = response.data
      console.log(response.data)
    })
      .catch((e) => {
        console.log(e)
      })
    this.$forceUpdate()
  },
  updated () {
    this.shots = [this.player.shotsOn, this.player.totalShots, this.player.goals]
    this.tackles = this.player.tackles
    this.blocks = this.player.blocks
    this.saves = this.player.saves
    this.concededGoals = this.player.concededGoals
    this.duels = [this.player.totalDuels, this.player.duelsWon]
    this.dribblesAttempts = this.player.dribblesAttempts
    this.dribblesSuccess = this.player.dribblesSuccess
    this.foulsCommitted = this.player.foulsCommitted
    this.foulsDrawn = this.player.foulsDrawn
    this.passes = [this.player.passes, this.player.passesAccuracy, this.player.assists]
    this.penalties = [this.player.penaltiesCommited, this.player.penaltiesMissed, this.player.penaltiesSaved, this.player.penaltiesScored, this.player.penaltiesWon]
    this.yellowCards = this.player.yellowCards
    this.redCards = this.player.redCards
    this.yellowRedCards = this.player.yellowredCards
    this.shotsChart = new Chart(document.getElementById('shots'),
      {
        type: 'bar',
        data: {
          labels: ['Shots On', 'Total Shots', 'Goals'],
          datasets: [
            {
              label: 'Shots',
              data: this.shots,
              base: 0,
              backgroundColor: ['#2F6690', '#FFA100', '#EA526F']
            }
          ]
        }
      }
    )
    this.defenseChart = new Chart(document.getElementById('defense'),
      {
        type: 'pie',
        data: {
          labels: ['Tackles', 'Blocks'],
          datasets: [
            {
              data: [this.tackles, this.blocks],
              backgroundColor: ['#AF9AB2', '#59C3C3']
            }
          ]
        }
      }
    )
    this.goalkeeperDefenseChart = new Chart(document.getElementById('goalkeeperDefense'),
      {
        type: 'pie',
        data: {
          labels: ['Saves', 'Conceded Goals'],
          datasets: [
            {
              data: [this.saves, this.concededGoals],
              backgroundColor: ['#AF9AB2', '#59C3C3']
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
              data: this.duels,
              base: 0,
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
          labels: ['Dribbles Attempts', 'Dribbles Success'],
          datasets: [
            {
              data: [this.dribblesAttempts, this.dribblesSuccess],
              backgroundColor: ['#AF9AB2', '#59C3C3']
            }
          ]
        }
      }
    )
    this.foulsChart = new Chart(document.getElementById('fouls'),
      {
        type: 'pie',
        data: {
          labels: ['Fouls Committed', 'Fouls Drawn'],
          datasets: [
            {
              data: [this.foulsCommitted, this.foulsDrawn],
              backgroundColor: ['#AF9AB2', '#59C3C3']
            }
          ]
        }
      }
    )
    this.passesChart = new Chart(document.getElementById('passes'),
      {
        type: 'bar',
        data: {
          labels: ['Total Passes', 'Passes Accuracy', 'Assists'],
          datasets: [
            {
              label: 'Passes',
              data: this.passes,
              base: 0,
              backgroundColor: ['#2F6690', '#FFA100', '#EA526F']
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
              data: this.penalties,
              base: 0,
              backgroundColor: ['#2F6690', '#FFA100', '#EA526F', '#59C3C3', '#AF9AB2']
            }
          ]
        }
      }
    )
    this.cardsChart = new Chart(document.getElementById('cards'),
      {
        type: 'pie',
        data: {
          labels: ['Yellow Cards', 'Red Cards', 'Yellow-Red Cards'],
          datasets: [
            {
              data: [this.yellowCards, this.redCards, this.yellowRedCards],
              backgroundColor: ['#2F6690', '#FFA100', '#EA526F']
            }
          ]
        }
      }
    )
    Chart.defaults.global.defaultFontColor = '#fff'
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

#matchList{
  position: relative;
  left: 320px;
}
#shots{
  position: relative;
  left: 320px;
}
#duels{
  position: relative;
  left: 320px;
}
#cards{
  position: relative;
  left: 320px;
}
</style>
