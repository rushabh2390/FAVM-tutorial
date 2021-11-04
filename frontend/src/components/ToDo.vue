<template>
<div class="container">
  <div class="row">
    <div class="col">
      <div class="card" style="width: 18rem;">
        <div class="card-body">
          <div class="card-title">
              <label for="title">Todo Title</label>
              <input type="text" id="title" name="todo" v-model="title" />
          </div>
          <div class="card-text">
              <label for="title">Todo Description</label>
              <textarea id="new-todo-input" name="description" v-model="description" /></div>
          <button type="submit" class="btn btn-primary" @click="addtodo()"> Submit </button>
        </div>
      </div>
  </div>
</div>
  <div class="row">
    <div class="col">
      <br/>
      <table class="table table-bordered " border="0">
        <thead class="thead-dark">
          <tr>
                <th>Sr. No.</th>
                <th> Title </th>
                <th> Description </th>
                <th> Delete </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(todo, index) in todoslist" :key="todo.index" style="height:1em;">
              <td>{{ (index+1) }}</td>
              <td>{{ todo.title }}</td>
              <td>{{ todo.description }}</td>
              <td><button class="btn btn-danger" @click="deletetodo(todo.title)">Delete</button></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

</div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      todoslist: [],
      title: '',
      description: '',
      errorsearch: []
    }
  },
  async created () {
    this.gettodo()
  },
  methods: {
    async gettodo () {
      try {
        const headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
        const response = await axios.get('http://127.0.0.1:8000/api/todo', {headers})
        this.todoslist = response.data
      } catch (error) {
        this.todoslist = []
        this.errorsearch = error.response.data
        return error.response
      }
    },
    async deletetodo (title) {
      try {
        const response = await axios.delete(`http://127.0.0.1:8000/api/todo/${title}`)
        alert(response.data)
        this.gettodo()
      } catch (error) {
        this.errorsearch = error.response.data
        return error.response
      }
    },
    async addtodo () {
      try {
        const addTitle = { title: this.title, description: this.description }
        const headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
        const response = await axios.post('http://127.0.0.1:8000/api/todo', addTitle, {headers})
        console.log(response.data)
        alert(response.data)
        this.gettodo()
      } catch (error) {
        this.errorsearch = error.response.data
        return error.response
      }
    }
  }
}
</script>
