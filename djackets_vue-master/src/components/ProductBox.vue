<template>
    
    <div class="card" style="width: 18rem;">
        <img v-bind:src="product.get_thumbnail">
        <div class="card-body">
            <h5 class="card-title">{{ product.name }}</h5>
            <h5 class="card-title">${{ product.price }}</h5>
            <p class="card-text">{{ product.description }}</p>
            <router-link v-bind:to="product.get_absolute_url" class="btn btn-primary">View details</router-link>
        </div>
    </div>
    
</template>

<script>
export default {
    name: 'ProductBox',
    props: {
        product: Object
    }
}
</script>

<style scoped>

  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>