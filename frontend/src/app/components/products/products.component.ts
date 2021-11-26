import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {

  isLogged = false;
  token = "null";

  constructor(private router: Router) {
    const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
    if (currentUser != null) {
      this.token = currentUser.token;
      this.isLogged = true;
    }
    console.log("token:" +this.token)
    console.log(this.isLogged)
  }

  ngOnInit(): void {
    const search = document.getElementById("search"); //pass the id of the input of searchbar
    const productName = document.querySelectorAll(".product-details h2"); //name of card

    const btns = document.querySelectorAll('.btn');
    const storeProducts = document.querySelectorAll<HTMLElement>('.store-product' );

    search!.addEventListener("keyup", filterProducts);

    function filterProducts(e:any){
      const text = e.target.value.toLowerCase();
      console.log(productName[0]);

      productName.forEach(function(product) {
        const item = product.firstChild!.textContent;
        if (item!.toLowerCase().indexOf(text) != -1) {
          product.parentElement!.parentElement!.style.display = "block"
        } else {
          product.parentElement!.parentElement!.style.display = "none"
        }
      })
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
        console.log(filter);

        storeProducts.forEach((product)=> {
          if (filter === 'all'){
            product.style.display = 'block'
          } else {
            if (product.classList.contains(filter)){
              product.style.display = 'block'
            } else {
              product.style.display = 'none'
            }
          }
        });
      });
    }
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
