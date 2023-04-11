<template>
    <div class = "mainpage">
        <table class = "table">
            <tbody>
                <tr>
                    <th><router-link :to="'/team/' + teamOne.id"><img v-bind:src="teamOne.logo"/></router-link></th>
                    <th><router-link :to="'/team/' + teamTwo.id"><img v-bind:src="teamTwo.logo"/></router-link></th>
                    <th><router-link :to="'/team/' + teamThree.id"><img v-bind:src="teamThree.logo"/></router-link></th>
                    <th><router-link :to="'/team/' + teamOne.id"><img v-bind:src="teamOne.logo"/></router-link></th>
                </tr>
                <tr>
                    <th><router-link :to="'/team/' + teamOne.id"><img v-bind:src="teamOne.logo"/></router-link></th>
                    <th><router-link :to="'/team/' + teamOne.id"><img v-bind:src="teamOne.logo"/></router-link></th>
                    <th><router-link :to="'/team/' + teamOne.id"><img v-bind:src="teamOne.logo"/></router-link></th>
                    <th><router-link :to="'/team/' + teamOne.id"><img v-bind:src="teamOne.logo"/></router-link></th>
                </tr>
                <tr>
                    <th><router-link :to="'/team/' + teamOne.id"><img v-bind:src="teamOne.logo"/></router-link></th>
                    <th><router-link :to="'/team/' + teamOne.id"><img v-bind:src="teamOne.logo"/></router-link></th>
                    <th><router-link :to="'/team/' + teamOne.id"><img v-bind:src="teamOne.logo"/></router-link></th>
                    <th><router-link :to="'/team/' + teamOne.id"><img v-bind:src="teamOne.logo"/></router-link></th>
                </tr>
                <tr>
                    <th><router-link :to="'/team/' + teamOne.id"><img v-bind:src="teamOne.logo"/></router-link></th>
                    <th><router-link :to="'/team/' + teamOne.id"><img v-bind:src="teamOne.logo"/></router-link></th>
                    <th><router-link :to="'/team/' + teamOne.id"><img v-bind:src="teamOne.logo"/></router-link></th>
                    <th><router-link :to="'/team/' + teamOne.id"><img v-bind:src="teamOne.logo"/></router-link></th>
                </tr>
                <tr>
                    <th><router-link :to="'/team/' + teamOne.id"><img v-bind:src="teamOne.logo"/></router-link></th>
                    <th><router-link :to="'/team/' + teamOne.id"><img v-bind:src="teamOne.logo"/></router-link></th>
                    <th><router-link :to="'/team/' + teamOne.id"><img v-bind:src="teamOne.logo"/></router-link></th>
                    <th><router-link :to="'/team/' + teamOne.id"><img v-bind:src="teamOne.logo"/></router-link></th>
                </tr>
            </tbody>
        </table>
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
      teamOne: {},
      teamTwo: {},
      teamThree: {},
      teamFour: {},
      teamFive: {},
      teamSix: {},
      teamSeven: {},
      teamEight: {},
      teamNine: {},
      teamTen: {},
      teamEleven: {},
      teamTwelve: {},
      teamThirteen: {},
      teamFourteen: {},
      teamFifteen: {},
      teamSixteen: {},
      teamSeventeen: {},
      teamEighteen: {},
      teamNineteen: {},
      teamTwenty: {}

    }
  },
  methods: {
  },
  mounted () {
    http.get('/teams').then((response) => {
      this.teams = response.data
      this.teamOne = this.teams[0]
      this.teamTwo = this.teams[1]
      this.teamThree = this.teams[2]
      this.teamFour = this.teams[3]
      this.teamFive = this.teams[4]
      this.teamSix = this.teams[5]
      this.teamSeven = this.teams[6]
      this.teamEight = this.teams[7]
      this.teamNine = this.teams[8]
      this.teamTen = this.teams[9]
      this.teamEleven = this.teams[10]
      this.teamTwelve = this.teams[11]
      this.teamThirteen = this.teams[12]
      this.teamFourteen = this.teams[13]
      this.teamFifteen = this.teams[14]
      this.teamSixteen = this.teams[15]
      this.teamSeventeen = this.teams[16]
      this.teamEighteen = this.teams[17]
      this.teamNineteen = this.teams[18]
      this.teamTwelve = this.teams[19]
      console.log(response.data)
    })
      .catch((e) => {
        console.log(e)
      })
  }
}
</script>

<style>
.table th{
    padding: 75px;
}
</style>
