import { Component, OnInit } from '@angular/core';
import axios from 'axios'

@Component({
  selector: 'app-user-products',
  templateUrl: './user-products.component.html',
  styleUrls: ['./user-products.component.css']
})

export class UserProductsComponent implements OnInit{
  state = {products: []}
  constructor() {
    this.getProducts()
  }

  ngOnInit() {
  }
  getProducts(){
    const path = 'https://ubending3.herokuapp.com/user/1/products'
    axios.get(path)
      .then((res) => {
        // @ts-ignore
        this.state.products =  res.data
        console.log(this.state.products)
      })
      .catch((error) => {
        console.error(error)
      })
  }
  url:string = "/assets/sneaker.jpg"
  url1:string = "../assets/img2.jpg"
  url2:string = "../assets/img2.jpg"
  url3:string = "../assets/img2.jpg"
  url4:string = "../assets/img2.jpg"

  changeImage(event:any){
    this.url = event.target.src;
  }

}
