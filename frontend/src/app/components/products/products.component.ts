import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";
import axios from "axios";

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {

  isLogged = false;
  token = "null";
  state = {products: []}

  constructor(private router: Router) {
    const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
    if (currentUser != null) {
      this.token = currentUser.token;
      this.isLogged = true;
    }

  }

  ngOnInit(): void {
    this.getProducts()

    const search = document.getElementById("search"); //pass the id of the input of searchbar
    const products = document.getElementsByClassName("product_name")
    const btns = document.querySelectorAll('.btn');
    const storeProducts = document.getElementsByClassName("product_card")

    search!.addEventListener("keyup", filterProducts);

    function filterProducts(e:any){
      const text = e.target.value.toLowerCase();
      for (let i = 0; i < products.length; i++) {
        // @ts-ignore
        const item = products.item(i).firstChild!.textContent;
        if (item!.toLowerCase().indexOf(text) != -1) {
          // @ts-ignore
          products.item(i).parentElement!.parentElement!.style.display = "block"
        } else {
          // @ts-ignore
          products.item(i).parentElement!.parentElement!.style.display = "none"
        }
      }
    }

    for (let i = 0; i < btns.length; i++) {

      btns[i].addEventListener('click', (e) => {
        for(let x=0; x<btns.length; x++)
        {
          btns[x].classList.remove('active');
        }
        btns[i].classList.add('active');

        e.preventDefault()

        // @ts-ignore
        const filter = e.target.dataset.filter;

        for (let x = 0; x < storeProducts.length; x++) {
          // @ts-ignore
          console.log(storeProducts.item(x).classList)
          if (filter === 'all'){
            // @ts-ignore
            storeProducts.item(x).style.display = 'block'
          } else {
            // @ts-ignore
            if (storeProducts.item(x).classList.contains(filter)){
              // @ts-ignore
              storeProducts.item(x).style.display = 'block'
            } else {
              // @ts-ignore
              storeProducts.item(x).style.display = 'none'
            }
          }

        }

      });
    }
  }
  loadPorducts(name: String) {

  }
  getProducts(){

    const path = 'https://ubending4.herokuapp.com/api/search'
    const params = {
      name: '',
      from: 0,
      jump: 20
    }
    axios.post(path, params)
      .then((res) => {
        // @ts-ignore
        this.state.products = res.data
        console.log(res.data)
      })
      .catch((error) => {
        console.error(error)
      })
  }

  onClickSignIn(){
    // @ts-ignore
    this.$router.replace({path: '/', query: {}})
  }

  menuToggle(){
    const toggleMenu = document.querySelector('.menu')
    toggleMenu!.classList.toggle('active')
  }

  resetToken() {
    localStorage.removeItem('currentUser')
    this.router.navigate(['/login-signup'])
  }

  myProducts() {
    this.router.navigate(['/user-products'])
  }

  editProfile() {
    this.router.navigate(['/user-profile'])
  }

}
