import {Component, OnInit} from '@angular/core';
import axios from 'axios'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit{
  title = 'frontend';
  state = {products: []}
  constructor() {
    this.getProducts()
  }

  ngOnInit() {
  }
  getProducts(){
    const path = 'http://127.0.0.1:5000/user/1/products'
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
  url:string = "../assets/img2.jpg"
  url1:string = "../assets/img2.jpg"
  url2:string = "../assets/img2.jpg"
  url3:string = "../assets/img2.jpg"
  url4:string = "../assets/img2.jpg"

  changeImage(event:any){
    this.url = event.target.src;
  }

  changeImage1(event:any){
    this.url1 = event.target.src;
  }

  changeImage2(event:any){
    this.url2 = event.target.src;
  }

  changeImage3(event:any){
    this.url3 = event.target.src;
  }

  changeImage4(event:any){
    this.url4 = event.target.src;
  }

}


