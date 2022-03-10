<template>
<div class="nav-bar">
            <nav class="navbar navbar-expand-lg">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#"><img src="/slike/matijaLogo.jpg" /></a> 
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <i class="fas fa-bars"></i>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav ms-auto">
                            <!-- ms-auto gura navigacijski bar u desnu stranu -->
                            <li class="nav-item">
                                <a class="nav-link" href="#top">HOME</a>
                            </li>
                            <li class="nav-item">
                                <router-link style="text-decoration: none; color: inherit;" to="/AboutMe"><a class="nav-link" href="#about" v-on:click="showShop= false">ABOUT ME</a></router-link>
                            </li>
                            <li class="nav-item">
                                <router-link style="text-decoration: none; color: inherit;" to="/Experience"><a class="nav-link" href="#resume" v-on:click="showShop= false">RESUME</a></router-link>
                            </li>
                            <li class="nav-item">
                                <router-link style="text-decoration: none; color: inherit;" to="/EmployeeForm"><a class="nav-link" href="#form" v-on:click="showShop= false">EMPLOYEE FORM</a></router-link>
                            </li>
                            <li class="nav-item">
                                <router-link style="text-decoration: none; color: inherit;" to="/" ><a class="nav-link" href="#form" v-on:click="showShop= true">SHOP</a></router-link>
                            </li>
                            
                            <li class="nav-item">
                                <a class="nav-link" href="#services">SERVICES</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#contact">CONTACT</a>
                            </li>

                        </ul>
                    </div>
                </div>
            </nav>
</div>
<!-- ////////// -->
<!-- <div class="nav-bar">
            <nav class="navbar navbar-expand-lg">
                <div class="container-fluid">
                    <router-link to="/" class="navbar-item" ><i class='fas fa-shopping-bag' style="color:#404040;" ></i></router-link>
                    
                    <form method="get" action="/search" style="height:100%;     width:30%; display: block; margin:0; padding:5px;" >
                      <input type="text" class="input" placeholder="What are you looking for?" name="query" style="height:100%;     width:90%;     margin:0; padding:auto; border-radius:3% 0% 0% 3%;">
                      <button class="button is-success" style="background:#00CC00; height:100%;     width:7%;     margin:0; padding:auto; border-radius:0% 10% 10% 0%;">
                        <span class="icon">
                          <i class="fas fa-search"></i>
                        </span>
                      </button>
                    </form>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <i class="fas fa-bars"></i>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav ms-auto">
                            
                            <li class="nav-item">
                                <router-link to="/frontend" class="btn btn-primary" style="background:#000; border:#404040; font-size: 16px; height:95%;     width:95%; text-align:center;   margin: 0px; padding:2px;">FRONT <br> END</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link to="/backend" class="btn btn-primary" style="background:#000; border:#404040; font-size: 16px; height:95%;     width:95%; text-align: center;   margin: 0; padding:2px; outline: none;">BACK <br> END</router-link>
                            </li>
                            <li class="nav-item">
                                <template v-if="$store.state.isAuthenticated">
                                  <router-link to="/my-account" class="btn btn-primary" style="background:white; border:white; color:black; font-size: 16px; height:90%;     width:90%; text-align: center;   margin:0; padding-top:6px;">MY ACCOUNT</router-link>
                                </template>
                                <template v-else >
                                  <router-link to="/log-in" class="btn btn-primary" style="background:white; border:white; color:black; font-size: 16px; height:95%;     width:95%; text-align: center;   margin:0; padding:2px;">LOG IN</router-link>
                                </template>                             </li>
                            <li class="nav-item">
                                <router-link to="/cart" class="btn btn-primary" style=" background:#00CC00; border:#00CC00; font-size: 16px; ">
                                  <span class="icon"><i class="fas fa-shopping-cart" style="height:80%; width:80%; " ></i></span>
                                  <span >Cart ({{ cartTotalLength }})</span>
                                </router-link>                            
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
</div> -->




<!-- ////////////////// -->
<div class="static" id="wrapper" v-if="showShop" >
  <section class="header-main">
    <div class="container-fluid" style="background:#000; ">
      
        <div class="container-bar"  >
          <div class="col-sm" style="padding-left:70px; padding-top:5px; padding-botom:5px; margin-bottom:5px; ">
            <router-link to="/" class="navbar-item" ><i class='fas fa-shopping-bag' style="color:#404040;" ></i></router-link>
          </div>
          <div class="col-sm">
            <form method="get" action="/search" style="height:90%;     width:93%; display: block; margin:0; padding:5px;" >
              
              <input type="text" class="input" placeholder="What are you looking for?" name="query"         style="height:100%;     width:90%;     margin:0; padding:auto; border-radius:3% 0% 0% 3%;">
              
              <button class="button is-success" style="background:#00CC00; height:100%;     width:7%;     margin:0; padding:auto; border-radius:0% 10% 10% 0%;">
                <span class="icon">
                  <i class="fas fa-search"></i>
                </span>
              </button>
            </form> 
          </div>
          <div class="col-sm">
            <div class="row"> 
              <div class="col-sm">
              <!-- moj dio -->
              <router-link to="/contact-us" class="btn btn-primary">CONTACT US</router-link>

              </div> 
              <div class="col-sm" style="text-align: center; padding:0; ">
                <router-link to="/frontend" class="btn btn-primary" style="background:#000; border:#404040; font-size: 16px; height:95%;     width:95%; text-align:center;   margin: 0px; padding:2px; ">FRONT <br> END</router-link>
              </div>     
              <div class="col-sm" style="text-align: center; padding:0;">
                <router-link to="/backend" class="btn btn-primary" style="background:#000; border:#404040; font-size: 16px; height:95%;     width:95%; text-align: center;   margin: 0; padding:2px; outline: none;">BACK <br> END</router-link>
              </div>
              <div class="col-sm" style="text-align: center; padding:0; height:90%; width:90%;"> 
                <template v-if="$store.state.isAuthenticated">
                  <router-link to="/my-account" class="btn btn-primary" style="background:white; border:white; color:black; font-size: 16px; height:90%;     width:90%; text-align: center;   margin:0; padding-top:6px;">MY ACCOUNT {{userName}}</router-link>
                </template>
                <template v-else >
                  <router-link to="/log-in" class="btn btn-primary" style="background:white; border:white; color:black; font-size: 16px; height:95%;     width:95%; text-align: center;   margin:0; padding:2px;">LOG IN</router-link>
                </template>     
              </div>
              <div class="col-sm" style="text-align: center;  ">
                <router-link to="/cart" class="btn btn-primary" style=" background:#00CC00; border:#00CC00; font-size: 16px; ">
                  <span class="icon"><i class="fas fa-shopping-cart" style="height:80%; width:80%; " ></i></span>
                  <span>Cart ({{cartTotalLength}})</span>
                  
                </router-link>     
              </div>
            </div>
          </div>
        </div>
    </div>
  </section>
</div>

  <div class="is-loading-bar has-text-centered"  style="text-align:center;" v-bind:class="{'is-loading': $store.state.isLoading }">
    <div class="lds-dual-ring"></div>
  </div>

  <section class="section">
      <router-view/>
  </section>

</template>



<script>
import axios from 'axios'

export default {
  data() {
    return {
      showMobileMenu: false,
      showShop:true,
      cart: {
        items: []
      },
      /// user je za username prikazati ali za sada to radi ko k
      User:'',
      
    }
  },

  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }    
  },
  
  mounted() {
    this.cart = this.$store.state.cart  
    ////////////////////////////////////
    this.User = this.$store.state.nameUser
    //console.log(this.User)
    //this.refreshData()
  },

  computed: {
      cartTotalLength() {
          let totalLength = 0
          for (let i = 0; i < this.cart.items.length; i++) {
              totalLength += parseInt(this.cart.items[i].quantity)
          }       
          return totalLength
      },
      userName(){
        let name =this.User
        //this.User=this.$store.state.nameUser
        return  name
      }
  },

}
</script>

<style lang="scss">
// @import '../../node_modules/bulma';

.fa-shopping-bag{
  font-size: 3em; 
  color:black;
}
.container-bar{
  display: grid;
  grid-template-columns: 1fr 5fr 3fr;
}

// ------------------------

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #00CC00;
  border-color: #00CC00 transparent #00CC00 transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>
