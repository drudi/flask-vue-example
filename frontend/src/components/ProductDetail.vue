<template>
  <div class="component">
    <router-link to="/"><< Back to Products</router-link>
    <h1>Product Detail</h1>
    <div class="row">
      <button class="btn btn-primary" @click="toggleAddProduct()">Add Child Product</button>
    </div>
    <div class="row">
      <div>
        <app-product :prod="product"></app-product>
      </div>
    </div>
    <hr>
    <div class="row">
      <app-sub-product-add v-if="showAddForm" @productAdded="productAdded" :parent_id="id"></app-sub-product-add>
    </div>
    <hr>
    <h2>Subproducts</h2>
    <div class="row">
        <app-product :prod="child" v-for="child in children" :key="child.id"></app-product>
    </div>



    <!-- <product v-for="product in products"></product> -->
  </div>
</template>

<script>
  import Product from './Product.vue'
  import SubProductAdd from './SubProductAdd.vue'

  export default {
    name: 'productDetail',
    components: {
      appProduct: Product,
      appSubProductAdd: SubProductAdd
    },
    data: function () {
      return {
        products: [],
        showAddForm: false,
        showProducts: true,
        id: this.$route.params.id,
        product: {},
        children: []
      }
    },
    computed: {

    },
    created: function () {
      this.getProduct()
      this.getChildren()
    },
    methods: {
      getProduct: function () {
        console.log('getProduct was called')
        this.$http.get('http://localhost:5000/v1/product/' + this.id)
          .then(response => {
            return response.json()
          })
          .then(data => {
            console.log(data)
            this.product = data
          })
      },
      getChildren: function () {
        this.$http.get('http://localhost:5000/v1/product/' + this.id + '/children')
          .then(response => {
            return response.json()
          })
          .then(data => {
            console.log(data)
            this.children = data.products
          })
      },
      toggleAddProduct: function () {
        this.showAddForm = !this.showAddForm
      },
      productAdded: function () {
        this.toggleAddProduct()
        this.getChildren()
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
