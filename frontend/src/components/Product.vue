<template>
  <div class="component product col-md-4">
    <div v-if="!editMode">
      <p>id: {{ prod.id }}</p>
      <router-link :to="detailLink"><h2>{{ prod.name }}</h2></router-link>
      <p>{{ prod.description }}</p>
      <p>Price: {{ prod.price }}</p>
    </div>
    <div v-if="editMode">
      <div>
        <label>Product Name</label>
        <input class="form-control" type="text" v-model="prod.name">
        <label>Product Description</label>
        <input class="form-control" type="textbox" v-model="prod.description">
        <label>Price</label>
        <input class="form-control" type="text" v-model="prod.price">
      </div>
      <div>
        <button class="btn btn-primary" @click="saveProduct(prod.id)">Save</button>
      </div>
    </div>
    <hr>
    <div class="row">
      <div  class="col-md-4 " v-for="image in prod.images" :key="image.id">
        <img  class="prod-image" :src="image.url">
        <span @click="deleteImage(image.id)" class="glyphicon glyphicon-remove-circle"></span>
      </div>
    </div>
    <hr>
    <div class="row">
      <div class="col-md-12">
        <button class="btn btn-primary" @click="editMode = !editMode">Edit</button>
        <button class="btn btn-primary" @click="deleteProduct">Delete</button>
        <button class="btn btn-primary" @click="toggleImageAdd">Add Image</button>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <app-image-add v-if="showImageAddForm" :prod="prod" @imageAdded="handleImageAdded"></app-image-add>
      </div>
    </div>

  </div>
</template>

<script>
  import ImageAdd from './ImageAdd.vue'

  export default {
    name: 'product',
    props: ['prod'],
    components: {
      appImageAdd: ImageAdd
    },
    data: function () {
      return {
        showImageAddForm: false,
        editMode: false,
        detailLink: '/product/' + this.prod.id
      }
    },
    methods: {
      deleteProduct: function () {
        this.$http.delete('http://localhost:5000/v1/product/' + this.prod.id)
          .then(response => {
            console.log(response.body)
            this.$emit('productDeleted')
          }, error => {
            console.log(error)
          })
      },
      toggleImageAdd: function () {
        this.showImageAddForm = !this.showImageAddForm
      },
      handleImageAdded: function (image) {
        this.toggleImageAdd()
        this.prod.images.push(image)
        console.log(this.prod.images)
      },
      deleteImage: function (id) {
        console.log(id)
        this.$http.delete('http://localhost:5000/v1/image/' + id)
          .then(response => {
            console.log(response.body)
            for (var i = 0; i < this.prod.images.length; i++) {
              if (this.prod.images[i].id === id) {
                this.prod.images.splice(i, 1)
                break
              }
            }
          }, error => {
            console.log(error)
          })
      },
      saveProduct: function (id) {
        this.$http.put('http://localhost:5000/v1/product/' + id, this.prod)
          .then(response => {
            console.log(response.body)
            this.editMode = !this.editMode
          }, error => {
            console.log(error)
          })
      }
    }
  }
</script>

<style scoped>
h1, h2 {
  font-weight: bold;
  font-size: 150%;
}

a {
  color: #42b983;
}

.product {
  text-align: left;
  min-height: 70vh;
}

.prod-image {
  max-width: 90px;
  max-height: 90px;
}

.img-container {
  display: inline-block;
}

.prod-div {
  border: 1px solid black;
}

</style>
