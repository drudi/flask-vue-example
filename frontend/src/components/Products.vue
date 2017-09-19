<template>
  <div class="component">
    <h1>Products</h1>
    <div class="row">
      <button class="btn btn-primary" @click="getProducts()">Refresh products</button>
      <button class="btn btn-primary" @click="toggleAddProduct()">Add Product</button>
    </div>
    <app-product-add v-if="showAddForm" @productAdded="productAdded"></app-product-add>
    <app-image-add v-if=" showImageAddForm" @imageAdded="imageAdded"></app-image-add>
    <div class="row">
      <div>
        <app-product v-for="product in products" :prod="product" @productDeleted="getProducts"></app-product>
      </div>
    </div>
    <!-- <product v-for="product in products"></product> -->
  </div>
</template>

<script>
  import Product from './Product.vue'
  import ProductAdd from './ProductAdd.vue'

  export default {
    name: 'products',
    components: {
      appProduct: Product,
      appProductAdd: ProductAdd
    },
    data: function () {
      return {
        products: [],
        showAddForm: false,
        showImageAddForm: false
      }
    },
    created: function () {
      this.getProducts()
    },
    methods: {
      getProducts: function () {
        console.log('getProducts was called')
        this.$http.get('http://localhost:5000/v1/product')
          .then(response => {
            return response.json()
          })
          .then(data => {
            this.products = data.products
          })
      },
      toggleAddProduct: function () {
        this.showAddForm = !this.showAddForm
      },
      productAdded: function () {
        this.toggleAddProduct()
        this.getProducts()
      },
      toggleAddImage: function () {
        this.showImageAddForm = !this.showImageAddForm
      },
      imageAdded: function () {
        this.toggleAddImage
      }
    }
  }
</script>

<style scoped>
h1, h2 {
  font-weight: bold;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
