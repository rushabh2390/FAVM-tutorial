import { createRouter, createWebHistory } from 'vue-router'
import ToDo from '@/components/ToDo'

const routes = [
  {
    path: '/',
    name: 'todo',
    component: ToDo
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
