import Vue from 'vue'
import Router from 'vue-router'
import MainTeam from '@/components/MainTeam'
import MainPlayer from '@/components/MainPlayer'
import FrontPage from '@/components/FrontPage'
import TeamMatch from '@/components/TeamMatch'
import PlayerMatch from '@/components/PlayerMatch'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/team/:id',
      name: 'MainTeam',
      component: MainTeam
    },
    {
      path: '/player/:id',
      name: 'MainPlayer',
      component: MainPlayer
    },
    {
      path: '/',
      name: 'FrontPage',
      component: FrontPage
    },
    {
      path: '/teammatch/:fixtureId/:teamId/:rivalTeamId',
      name: 'TeamMatch',
      component: TeamMatch
    },
    {
      path: '/playermatch/:fixtureId/:playerId/:teamId/:rivalTeamId',
      name: 'PlayerMatch',
      component: PlayerMatch
    }
  ]
})
