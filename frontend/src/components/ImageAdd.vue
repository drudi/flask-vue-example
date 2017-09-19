<template>
  <div class="component image col-md-10">
    <div>
      <label>Image type</label>
      <input class="form-control" type="text" v-model="image.type">
      <label>Image URL</label>
      <input class="form-control" type="textbox" v-model="image.url">
    </div>

    <div>
      <button class="btn btn-primary" @click="addImage">Save</button>
    </div>

  </div>
</template>

<script>
  export default {
    name: 'imageAdd',
    props: ['prod'],
    data: function () {
      return {
        image: {},
        product: {}
      }
    },
    methods: {
      addImage: function () {
        this.image.product_id = this.prod.id
        this.$http.post('http://localhost:5000/v1/image', this.image)
          .then(response => {
            // this.image = {}
            console.log(response.body)
            this.$emit('imageAdded', this.image)
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
}

a {
  color: #42b983;
}

.image {
  text-align: left;
  min-height: 40vh;
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
