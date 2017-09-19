<template>
  <div class="component product col-md-4">
    <div>
      <label>Product Name</label>
      <input class="form-control" type="text" v-model="product.name">
      <label>Product Description</label>
      <input class="form-control" type="textbox" v-model="product.description">
      <label>Price</label>
      <input class="form-control" type="text" v-model="product.price">
    </div>

    <div>
      <button class="btn btn-primary" @click="addProduct">Save</button>
    </div>

  </div>
</template>

<script>
  export default {
    name: 'productAdd',
    data: function () {
      return {
        product: {}
      }
    },
    methods: {
      addProduct: function () {
        this.$http.post('http://localhost:5000/v1/product', this.product)
          .then(response => {
            this.product = {}
            console.log(response.body)
            this.$emit('productAdded')
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

.product {
  text-align: left;
  height: 50vh;
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
