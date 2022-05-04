import { createRouter, createWebHashHistory } from 'vue-router'
import ToDo from '../components/ToDo'

const routes = [
  {
    path: '/',
    name: 'Todo',
    component: ToDo
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
