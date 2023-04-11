<template>
  <div class="mainpage row">
    <div><img v-bind:src="teamOne.logo" /></div>
    <div><img v-bind:src="teamOne.logo" /></div>
    <div class="col-md-8">
    </div>
    <div class ="col-md-6">
      <br>
      <h4>Teams List</h4>
      <ul class="list-group">
        <li class = "list-group-item"
        :class="{ active: index == currentIndex }"
        v-for="(team,index) in teams"
        :key="index"
        @click="setActiveTeam(team,index)"
        >
          {{ team.name }}
          <img v-bind:src="team.logo" />
        </li>
      </ul>
    </div>
    <div class="col-md-6">
      <div v-if="currentTeam">
        <br><br>
        <h4>Team Details:</h4>
        <div>
          <label><strong>Name: </strong></label>{{ currentTeam.name }}
          <br>
          <label><strong>Wins: </strong></label>{{ currentTeam.totalWins }}
          <br>
          <label><strong>Draws: </strong></label>{{ currentTeam.totalDraws }}
          <br>
          <label><strong>Loses: </strong></label>{{ currentTeam.totalLoses }}
          <br>
        </div>

        <br>
        <router-link :to="'/team/' + currentTeam.id" class = "btn btn-info">
          See team
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import http from '../http-common'

export default {
  name: 'MainPage',
  data () {
    return {
      teams: [],
      currentTeam: null,
      currentIndex: -1,
      name: '',
      teamOne: {}
    }
  },
  methods: {
    setActiveTeam (team, index) {
      this.currentTeam = team
      this.currentIndex = index
    }
  },
  mounted () {
    http.get('/teams').then((response) => {
      this.teams = response.data
      this.teamOne = this.teams[0]
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
