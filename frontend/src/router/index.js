import Vue from 'vue'
import Router from 'vue-router'
import Products from '@/components/Products'
import ProductDetail from '@/components/ProductDetail'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Products',
      component: Products
    },
    {
      path: '/product/:id',
      name: 'ProductDetail',
      component: ProductDetail
    }
  ]
})
