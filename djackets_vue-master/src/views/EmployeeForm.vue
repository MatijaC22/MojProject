<template>
    <div id="container">  

        <button type="button" 
                class="btn btn-primary m-2 fload-end" 
                data-bs-toggle="modal" 
                data-bs-target="#exampleModal" 
                @click="addClick()">
            Add Company Informations
        </button>

        <table class="table table-striped">
            <thead>
            <tr>
                <th>
                    <div class="d-flex flex-row">
                        <input class="form-control m-2"
                                v-model="CompanyIDFilter"
                                v-on:keyup="FilterFn()"
                                placeholder="Filter">

                        <button type="button" class="btn btn-light"
                                @click="sortResult('CompanyID',true)">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-down-square-fill" viewBox="0 0 16 16">
                                <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v5.793l2.146-2.147a.5.5 0 0 1 .708.708l-3 3a.5.5 0 0 1-.708 0l-3-3a.5.5 0 1 1 .708-.708L7.5 10.293V4.5a.5.5 0 0 1 1 0z"/>
                                </svg>
                        </button>
                        <button type="button" class="btn btn-light"
                                @click="sortResult('CompanyID',false)">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-up-square-fill" viewBox="0 0 16 16">
                                <path d="M2 16a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2zm6.5-4.5V5.707l2.146 2.147a.5.5 0 0 0 .708-.708l-3-3a.5.5 0 0 0-.708 0l-3 3a.5.5 0 1 0 .708.708L7.5 5.707V11.5a.5.5 0 0 0 1 0z"/>
                                </svg>
                        </button>
                    </div>
                    CompanyID
                </th>
                <th>
                    <div class="d-flex flex-row">
                        <input class="form-control m-2"
                                v-model="CompanyNameFilter"
                                v-on:keyup="FilterFn()"
                                placeholder="Filter">
                        <button type="button" class="btn btn-light"
                                @click="sortResult('CompanyName',true)">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-down-square-fill" viewBox="0 0 16 16">
                                <path d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v5.793l2.146-2.147a.5.5 0 0 1 .708.708l-3 3a.5.5 0 0 1-.708 0l-3-3a.5.5 0 1 1 .708-.708L7.5 10.293V4.5a.5.5 0 0 1 1 0z"/>
                                </svg>
                        </button>
                        <button type="button" class="btn btn-light"
                                @click="sortResult('CompanyName',false)">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-up-square-fill" viewBox="0 0 16 16">
                                <path d="M2 16a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2zm6.5-4.5V5.707l2.146 2.147a.5.5 0 0 0 .708-.708l-3-3a.5.5 0 0 0-.708 0l-3 3a.5.5 0 1 0 .708.708L7.5 5.707V11.5a.5.5 0 0 0 1 0z"/>
                                </svg>
                        </button>
                    </div>
                    CompanyName
                </th>
                <th>
                    Options
                </th>
            </tr>
            </thead>

            <tbody>
                <tr v-for="com in Companies"> 
                    <td>{{com.CompanyID}}</td>
                    <td>{{com.CompanyName}}</td>
                    <td> 
                        <button type="button" 
                                class="btn btn-light mr-1" 
                                data-bs-toggle="modal" 
                                data-bs-target="#exampleModal" 
                                @click="editClick(com)">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                            <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                            <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                            </svg>
                        </button>

                        <button type="button" 
                                @click="deleteClick(com.CompanyID)"
                                class="btn btn-light mr-1">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
                            <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                            </svg>
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>

        <div class="modal fade" id="exampleModal" tabindex="-1"
                aria-labelledby="exampleModalLabel" aria-hidden="true"
                >
            <div class="modal-dialog modal-lg modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLabel">{{modalTitle}}</h5>
                            <button type="button" 
                                    class="btn-close" 
                                    data-bs-dismiss="modal"
                                    aria-label="Close">  
                            </button>  
                    </div>

                    <div class="modal-body">
                        <div class="input-group mb-3">
                            <span class="input-group-text">Company Name</span>
                            <input type="text" class="form-control" v-model="CompanyName">
                        </div>

                        <button type="button" 
                                @click="createClick()"
                                v-if="CompanyID==0" 
                                class="btn btn-primary">
                            Create
                        </button>

                        <button type="button" 
                                @click="updateClick()"
                                v-if="CompanyID!=0" 
                                class="btn btn-primary">
                            Upadate
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
</template>

<script>
    
import axios from 'axios'

export default {
    name: 'EmployeeForm',
    data() {
             return{
                    Companies:[], /*decalring empty array which will be populated using the get api method*/
                    modalTitle:"",
                    CompanyName:"",
                    CompanyID:0,
                    CompanyNameFilter:"",
                    CompanyIDFilter:"",
                    CompanyWithoutFilter:[],

                    JobOffer:[],
                    JobOfferWithoutFilter:[],
                    

                }
    },
    
    methods:{ /*method to consume the get api method*/             
                async refreshData(){
                    this.$store.commit('setIsLoading', true)
                    await axios.get("api/v1/Company") /*consume the api ---- variables je variables.js di je url page stranica*/
                    //await axios.get("/api/v1/Company") /*consume the api ---- variables je variables.js di je url page stranica*/
                    .then((response)=>{
                        this.Companies=response.data; /*once the response recieve we will assign the data to the departments array*/
                        this.CompaniesWithoutFilter=response.data;
                        
                    }).catch(error => {
                     console.log(error)
                    })
                    await axios.get("api/v1/JobOffer") /*consume the api ---- variables je variables.js di je url page stranica*/
                    .then((response)=>{
                        this.JobOffer=response.data; /*once the response recieve we will assign the data to the departments array*/
                        this.JobOfferWithoutFilter=response.data;
                        
                    }).catch(error => {
                     console.log(error)
                    })
                    this.$store.commit('setIsLoading', false)
                    // da si vidim sto mi ima unutra
                    //console.log(this.JobOffer)
                    //console.log(this.Companies)
                },
                
                addClick(){
                    this.modalTitle="Add Company";
                    this.CompanyID=0;
                    this.CompanyName="";
                },
                editClick(com){
                    this.modalTitle="Edit Company";
                    this.CompanyID=com.CompanyID;
                    this.CompanyName=com.CompanyName;
                },
                async createClick(){
                    // await axios.post("http://127.0.0.1:8000/Company",{
                    await axios.post("api/v1/Company",{
                        CompanyName:this.CompanyName
                    })
                    .then((response)=>{
                        this.refreshData();
                        alert(response.data);
                    })    
                    console.log(this.CompanyName)
                },
                async updateClick(){
                    await axios.put("api/v1/Company",{
                        CompanyID:this.CompanyID,
                        CompanyName:this.CompanyName
                    })
                    .then((response)=>{
                        this.refreshData();
                        alert(response.data);
                    }) 
                                   
                },
                deleteClick(id){
                    if(!confirm("Are you sure?")){
                        return;
                    }
                    axios.delete("api/v1/Company/"+id) 
                    .then((response)=>{
                        this.refreshData();
                        alert(response.data);
                    });
                },
                FilterFn(){
                    var CompanyIDFilter=this.CompanyIDFilter;
                    var CompanyNameFilter=this.CompanyNameFilter;

                    this.Companies=this.CompaniesWithoutFilter.filter(
                        function(el){
                            return el.CompanyID.toString().toLowerCase().includes(
                                CompanyIDFilter.toString().trim().toLowerCase()
                            )&&
                            el.CompanyName.toString().toLowerCase().includes(
                                CompanyNameFilter.toString().trim().toLowerCase()
                            )
                        });
                },
                sortResult(prop,asc){
                    this.Companies=this.CompaniesWithoutFilter.sort(function(a,b){
                        if(asc){
                            return (a[prop]>b[prop])?1:((a[prop]<b[prop])?-1:0);
                        }
                        else{
                            return (b[prop]>a[prop])?1:((b[prop]<a[prop])?-1:0);
                        }
                    })
                },
            
                   
    },
    mounted:function(){ /*there is a lifecycle method called mounted which will be called when this component is in scope we will call the refresh method here*/
        this.refreshData(); /*navodno se lovi na variables(this)*/
    },
}
</script>

<style>
#container{
    margin-left: 80px;
}

</style>
