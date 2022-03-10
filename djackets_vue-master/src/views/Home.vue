<template>
  <div class="home">
    
    <section class="text-center" style="background:linear-gradient(rgba(0,0,0,0.3),rgba(0,0,0,0.3)),url(/slike/shopbackground1.jpeg);  background-position: center; background-size: cover; text-align:center; height:250px; border-bottom:2px solid #404040;">
        <div class="hero-body has-text-centered">
            <p class="title mb-6" style="padding: 50px 30px 0 0; color:black;">
                <strong>Welcome to Unique Shop</strong>
            </p>
            
            <p class="subtitle" style="color:yellow	">
                Add to cart how many hours per day of which software language <span style="color:red">(TOTAL 8)</span> <br> You can choose more but it will cost more :)
            </p>
        </div>
    </section>
    

    <div class="columns is-multiline">
      <div class="column is-12">
          <br>
          <h1 class="is-size-2 has-text-centered" style="text-align:center;">Latest products:</h1>
          <br>
      </div>

      <div class="container">
        <ProductBox 
            v-for="product in latestProducts"
            v-bind:key="product.id"
            v-bind:product="product" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import ProductBox from '@/components/ProductBox'

export default {
  name: 'Home',
  data() {
    return {
      latestProducts: []
    }
  },
  components: {
    ProductBox
  },
  mounted() {
    this.getLatestProducts()

    document.title = 'Home | Shop'
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)
      
      await axios
        .get('api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style scoped>
 .title{
   font-size:50px;
   
 }
  .container{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
    } 
  
</style>